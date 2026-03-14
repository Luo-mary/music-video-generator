#!/usr/bin/env python3
"""
Music Video Generator Workflow
-------------------------------
1. Select band members (roles + animal characters)
2. Generate music from prompt (MiniMax Music API - music-2.5+)
3. Generate multiple video clips with consistent characters (MiniMax Video API - Hailuo)
4. Concatenate clips and merge with music (ffmpeg)

Usage:
    python src/main.py --prompt "A happy upbeat pop song" --band-size 4
    python src/main.py --prompt "A rock ballad" --band-size 5 --assign vocalist=luna_cat guitarist=blaze_fox
    python src/main.py --list-characters
    python src/main.py --list-roles
"""

import os
import math
import argparse
import requests
import json
import time
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from characters import (
    build_band, build_band_prompt, build_closeup_prompt,
    list_characters, list_roles, get_band_roles,
    ANIMAL_CHARACTERS, BAND_ROLES,
)

# Config
OUTPUT_DIR = Path(__file__).parent.parent / "output"
SCRIPT_DIR = Path(__file__).parent.parent
CLIP_DURATION = 6  # seconds per Hailuo clip

# Load env vars
load_dotenv(SCRIPT_DIR / ".env")


def build_scene_sequence(band: list[dict], num_clips: int) -> list[str]:
    """Build a sequence of prompts that alternate between wide shots and close-ups.

    Every prompt includes full character descriptions for visual consistency.
    The sequence follows a pattern:
      - Wide/group shots for establishing scenes
      - Close-ups rotating through each band member
      - Dynamic/action shots for energy
    """
    prompts = []

    # Scene modifiers for wide/group shots
    wide_scenes = [
        "Wide establishing shot, camera slowly zooming in, dramatic stage lighting with spotlights.",
        "Wide shot from audience perspective, the crowd cheering, confetti falling from above.",
        "Low angle wide shot looking up at the band, powerful stage presence, lens flare effects.",
        "Side-angle wide shot, colorful spotlights sweeping across the stage, smoke machine haze.",
        "Overhead bird's-eye view looking down at the stage, radial light patterns.",
        "Wide dynamic shot, all band members jumping in sync, explosive energy, strobe lights.",
    ]

    # Build the full band description once (used in every prompt for consistency)
    band_description = build_band_prompt(band)

    for i in range(num_clips):
        cycle_pos = i % (len(band) + 2)  # +2 for wide shots in the cycle

        if cycle_pos == 0:
            # Opening/recurring wide shot
            scene = wide_scenes[i // (len(band) + 2) % len(wide_scenes)]
            prompts.append(f"{band_description} {scene}")

        elif cycle_pos <= len(band):
            # Close-up of each band member in rotation
            member = band[cycle_pos - 1]
            prompts.append(build_closeup_prompt(member,
                scene="Energetic performance moment, the character is fully immersed in the music."))

        else:
            # Action/dynamic wide shot
            scene = wide_scenes[(i // (len(band) + 2) + 3) % len(wide_scenes)]
            prompts.append(f"{band_description} {scene}")

    return prompts


class MusicVideoGenerator:
    def __init__(self):
        self.output_dir = OUTPUT_DIR
        self.output_dir.mkdir(exist_ok=True)
        self.clips_dir = self.output_dir / "clips"
        self.clips_dir.mkdir(exist_ok=True)

        self.api_key = os.getenv("MINIMAX_API_KEY", "")
        self.base_url = "https://api.minimax.io/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_music(self, prompt: str) -> tuple[str, float]:
        """Generate music and return (path, duration_seconds)."""
        print(f"\n🎵 Generating music...")
        print(f"   Prompt: {prompt}")

        if not self.api_key:
            print("⚠️ No MINIMAX_API_KEY found")
            return "", 0

        try:
            response = requests.post(
                f"{self.base_url}/music_generation",
                headers=self.headers,
                json={
                    "model": "music-2.5+",
                    "prompt": prompt,
                    "lyrics_optimizer": True,
                    "output_format": "hex",
                    "audio_setting": {
                        "sample_rate": 44100,
                        "bitrate": 256000,
                        "format": "mp3"
                    }
                },
                timeout=600
            )

            data = response.json()
            status_code = data.get("base_resp", {}).get("status_code", -1)

            if status_code == 0:
                audio_hex = data.get("data", {}).get("audio", "")
                if audio_hex:
                    music_path = self.output_dir / "music.mp3"
                    music_path.write_bytes(bytes.fromhex(audio_hex))
                    duration_ms = data.get("extra_info", {}).get("music_duration", 0)
                    duration_s = duration_ms / 1000
                    print(f"   ✅ Music saved: {music_path} ({duration_s:.1f}s)")
                    return str(music_path), duration_s
            else:
                status_msg = data.get("base_resp", {}).get("status_msg", "unknown")
                print(f"   ⚠️ Music API error: {status_code} - {status_msg}")

        except Exception as e:
            print(f"   ⚠️ Error: {e}")

        return "", 0

    def _submit_video_task(self, prompt: str, model: str) -> str:
        """Submit a video generation task, return task_id."""
        response = requests.post(
            f"{self.base_url}/video_generation",
            headers=self.headers,
            json={"model": model, "prompt": prompt},
            timeout=60
        )
        data = response.json()
        task_id = data.get("task_id", "")
        if not task_id:
            status_msg = data.get("base_resp", {}).get("status_msg", "unknown")
            print(f"      ⚠️ Failed to submit task: {status_msg}")
        return task_id

    def _download_video(self, file_id: str, save_path: Path) -> bool:
        """Download video by file_id."""
        resp = requests.get(
            f"{self.base_url}/files/retrieve",
            headers=self.headers,
            params={"file_id": file_id},
            timeout=30
        )
        data = resp.json()
        url = data.get("file", {}).get("download_url", "")
        if url:
            content = requests.get(url, timeout=120)
            save_path.write_bytes(content.content)
            return True
        return False

    def generate_video_clips(self, prompts: list[str], model: str) -> list[str]:
        """Generate video clips from a list of prompts.

        Submits tasks in batches to respect rate limits, polls until done.
        """
        num_clips = len(prompts)
        print(f"\n🎬 Generating {num_clips} video clips...")

        # Submit all tasks in batches
        BATCH_SIZE = 5
        tasks = []
        for i, prompt in enumerate(prompts):
            if i > 0 and i % BATCH_SIZE == 0:
                print(f"   ⏸️  Pausing 60s for rate limit (batch {i // BATCH_SIZE + 1})...")
                time.sleep(60)

            print(f"   📤 Submitting clip {i+1}/{num_clips}...")
            task_id = ""
            for retry in range(3):
                task_id = self._submit_video_task(prompt, model)
                if task_id:
                    break
                wait = 30 * (retry + 1)
                print(f"      ⏸️  Rate limited, retrying in {wait}s...")
                time.sleep(wait)

            if task_id:
                tasks.append((i, task_id))
                print(f"      Task ID: {task_id}")
            else:
                print(f"      ⚠️ Clip {i+1} skipped after retries")

            time.sleep(2)

        if not tasks:
            print("   ⚠️ No tasks submitted successfully")
            return []

        # Poll all tasks until done
        print(f"\n   ⏳ Waiting for {len(tasks)} clips to generate...")
        pending = dict(tasks)
        completed = {}
        failed = set()

        while pending:
            time.sleep(10)
            still_pending = {}
            for idx, task_id in pending.items():
                resp = requests.get(
                    f"{self.base_url}/query/video_generation",
                    headers=self.headers,
                    params={"task_id": task_id},
                    timeout=30
                )
                data = resp.json()
                status = data.get("status", "")

                if status == "Success":
                    file_id = data.get("file_id", "")
                    completed[idx] = file_id
                    print(f"      ✅ Clip {idx+1} ready")
                elif status == "Fail":
                    failed.add(idx)
                    print(f"      ❌ Clip {idx+1} failed: {data.get('error_message', '')}")
                else:
                    still_pending[idx] = task_id

            pending = still_pending
            if pending:
                print(f"      ⏳ {len(pending)} clips still processing, {len(completed)} done...")

        # Download all completed clips
        print(f"\n   📥 Downloading {len(completed)} clips...")
        clip_paths = []
        for idx in sorted(completed.keys()):
            clip_path = self.clips_dir / f"clip_{idx:03d}.mp4"
            if self._download_video(completed[idx], clip_path):
                encoded_path = self.clips_dir / f"clip_{idx:03d}_enc.mp4"
                subprocess.run([
                    "ffmpeg", "-y", "-i", str(clip_path),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-r", "24", "-movflags", "+faststart",
                    "-an", str(encoded_path)
                ], capture_output=True)
                clip_paths.append(str(encoded_path))
                print(f"      ✅ Clip {idx+1} downloaded")
            else:
                print(f"      ⚠️ Clip {idx+1} download failed")

        return clip_paths

    def merge_final_video(self, clip_paths: list[str], music_path: str) -> str:
        """Concatenate clips and merge with music using ffmpeg."""
        print(f"\n🎞️ Building final music video...")

        if not clip_paths:
            print("   ⚠️ No clips to merge")
            return ""

        concat_file = self.output_dir / "concat.txt"
        with open(concat_file, "w") as f:
            for path in clip_paths:
                f.write(f"file '{path}'\n")

        concat_video = self.output_dir / "concat_video.mp4"
        print("   🔗 Concatenating clips...")
        result = subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", str(concat_file),
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            str(concat_video)
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"   ⚠️ Concat failed: {result.stderr[-200:]}")
            return ""

        final_path = self.output_dir / "final_video.mp4"
        print("   🎶 Merging music with video...")
        result = subprocess.run([
            "ffmpeg", "-y",
            "-i", str(concat_video),
            "-i", music_path,
            "-c:v", "copy", "-c:a", "aac", "-b:a", "256k",
            "-shortest",
            "-movflags", "+faststart",
            str(final_path)
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"   ⚠️ Merge failed: {result.stderr[-200:]}")
            return ""

        probe = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(final_path)],
            capture_output=True, text=True
        )
        duration = float(probe.stdout.strip()) if probe.stdout.strip() else 0
        print(f"   ✅ Final video: {final_path} ({duration:.1f}s)")

        concat_file.unlink(missing_ok=True)
        concat_video.unlink(missing_ok=True)

        return str(final_path)

    def run(self, prompt: str, band: list[dict], video_model: str = "MiniMax-Hailuo-2.3"):
        """Run the full workflow."""
        print("\n" + "=" * 60)
        print("  🎸 Music Video Generator (MiniMax Edition)")
        print("=" * 60)

        # Display band lineup
        print("\n🎤 Band Lineup:")
        for m in band:
            char = m["character"]
            role = m["role"]
            print(f"   {role['name']:20s} → {char['name']} ({char['species']})")

        # Step 1: Generate music
        music_path, music_duration = self.generate_music(prompt)
        if not music_path:
            print("\n❌ Music generation failed. Aborting.")
            return ""

        # Step 2: Build scene sequence with consistent character prompts
        num_clips = max(1, math.ceil(music_duration / CLIP_DURATION))
        print(f"\n   📊 Music is {music_duration:.1f}s — need {num_clips} clips ({CLIP_DURATION}s each)")

        prompts = build_scene_sequence(band, num_clips)

        # Step 3: Generate video clips
        clip_paths = self.generate_video_clips(prompts, video_model)
        if not clip_paths:
            print("\n❌ Video generation failed. Aborting.")
            return ""

        # Step 4: Merge clips + music into final video
        final_path = self.merge_final_video(clip_paths, music_path)

        if final_path:
            print("\n" + "=" * 60)
            print(f"  ✅ Done! Final music video: {final_path}")
            print("=" * 60 + "\n")
        else:
            print("\n❌ Failed to create final video.")

        return final_path


def parse_assignments(assign_list: list[str]) -> dict[str, str]:
    """Parse assignment strings like 'vocalist=luna_cat' into a dict."""
    assignments = {}
    if not assign_list:
        return assignments
    for item in assign_list:
        if "=" not in item:
            print(f"⚠️ Invalid assignment format: {item} (expected role=character)")
            continue
        role_id, char_id = item.split("=", 1)
        if role_id not in BAND_ROLES:
            print(f"⚠️ Unknown role: {role_id}")
            print(f"   Available roles: {', '.join(BAND_ROLES.keys())}")
            continue
        if char_id not in ANIMAL_CHARACTERS:
            print(f"⚠️ Unknown character: {char_id}")
            print(f"   Use --list-characters to see available characters")
            continue
        assignments[role_id] = char_id
    return assignments


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Music Video Generator — Cartoon Animal Band (MiniMax)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 4-piece band with default animals
  python src/main.py --prompt "A happy pop song" --band-size 4

  # 5-piece band with custom character assignments
  python src/main.py --prompt "A rock anthem" --band-size 5 \\
    --assign vocalist=thunder_wolf guitarist=spike_hedgehog

  # List all available characters and roles
  python src/main.py --list-characters
  python src/main.py --list-roles
        """
    )
    parser.add_argument("--prompt", type=str, help="Music prompt")
    parser.add_argument("--band-size", type=int, default=4, choices=range(3, 9),
                        help="Number of band members (3-8, default: 4)")
    parser.add_argument("--assign", nargs="*", metavar="ROLE=CHARACTER",
                        help="Assign animals to roles (e.g. vocalist=luna_cat drummer=rocky_bear)")
    parser.add_argument("--video-model", type=str, default="MiniMax-Hailuo-2.3",
                        choices=["MiniMax-Hailuo-2.3", "MiniMax-Hailuo-02"],
                        help="Video model to use")
    parser.add_argument("--list-characters", action="store_true",
                        help="List all available animal characters")
    parser.add_argument("--list-roles", action="store_true",
                        help="List all available band roles")
    args = parser.parse_args()

    if args.list_characters:
        print("\n🐾 Available Animal Characters:\n")
        print(list_characters())
        print(f"\n   Total: {len(ANIMAL_CHARACTERS)} characters\n")
        exit(0)

    if args.list_roles:
        print("\n🎸 Available Band Roles:\n")
        print(list_roles())
        print(f"\n   Total: {len(BAND_ROLES)} roles\n")
        print("   Default roles by band size:")
        from characters import BAND_PRESETS
        for size, roles in BAND_PRESETS.items():
            print(f"     {size} members: {', '.join(roles)}")
        print()
        exit(0)

    if not args.prompt:
        parser.error("--prompt is required (unless using --list-characters or --list-roles)")

    # Build the band
    assignments = parse_assignments(args.assign)
    band = build_band(args.band_size, assignments)

    generator = MusicVideoGenerator()
    generator.run(args.prompt, band, args.video_model)
