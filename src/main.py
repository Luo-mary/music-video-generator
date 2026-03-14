#!/usr/bin/env python3
"""
Music Video Generator Workflow
-------------------------------
1. Select band members (roles + animal characters + gender matching)
2. Generate reference images for each character (MiniMax Image API - image-01)
3. Generate music from prompt (MiniMax Music API - music-2.5+)
4. Generate video clips with subject reference for consistency (MiniMax Video API - S2V-01)
5. Concatenate clips and merge with music (ffmpeg)

Usage:
    python src/main.py --prompt "A happy pop song" --band-size 4 --vocal-gender female
    python src/main.py --prompt "A rock anthem" --assign vocalist=luna_cat guitarist=blaze_fox
    python src/main.py --list-characters
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
    ANIMAL_CHARACTERS, BAND_ROLES, BAND_PRESETS,
)

# Config
OUTPUT_DIR = Path(__file__).parent.parent / "output"
SCRIPT_DIR = Path(__file__).parent.parent
CLIP_DURATION = 6  # seconds per video clip

# Load env vars
load_dotenv(SCRIPT_DIR / ".env")


def build_scene_sequence(band: list[dict], num_clips: int) -> list[dict]:
    """Build a sequence of clip configs (prompt + which member to use as subject reference).

    Returns list of dicts: {"prompt": str, "subject_member": dict or None}
    - Wide shots: subject_member = None (no subject ref, just text prompt)
    - Close-ups: subject_member = the specific band member
    """
    wide_scenes = [
        "Wide establishing shot, camera slowly zooming in, dramatic colorful stage lighting.",
        "Wide shot from audience view, cartoon crowd cheering, confetti falling, fun atmosphere.",
        "Low angle wide shot looking up at the band, powerful fun stage presence, lens flare.",
        "Side-angle wide shot, colorful spotlights sweeping, fun smoke effects on stage.",
        "Overhead bird's-eye view of the stage, radial neon light patterns, festive mood.",
        "Wide dynamic shot, all band members jumping together, explosive joyful energy.",
    ]

    band_prompt = build_band_prompt(band)
    clips = []

    for i in range(num_clips):
        cycle_pos = i % (len(band) + 2)

        if cycle_pos == 0:
            # Wide/group shot
            scene = wide_scenes[i // (len(band) + 2) % len(wide_scenes)]
            clips.append({
                "prompt": f"{band_prompt} {scene}",
                "subject_member": None,
            })
        elif cycle_pos <= len(band):
            # Close-up of individual member
            member = band[cycle_pos - 1]
            clips.append({
                "prompt": build_closeup_prompt(member,
                    "Energetic joyful performance, fully immersed in the music, having fun."),
                "subject_member": member,
            })
        else:
            # Dynamic wide shot
            scene = wide_scenes[(i // (len(band) + 2) + 3) % len(wide_scenes)]
            clips.append({
                "prompt": f"{band_prompt} {scene}",
                "subject_member": None,
            })

    return clips


class MusicVideoGenerator:
    def __init__(self):
        self.output_dir = OUTPUT_DIR
        self.output_dir.mkdir(exist_ok=True)
        self.clips_dir = self.output_dir / "clips"
        self.clips_dir.mkdir(exist_ok=True)
        self.refs_dir = self.output_dir / "character_refs"
        self.refs_dir.mkdir(exist_ok=True)

        self.api_key = os.getenv("MINIMAX_API_KEY", "")
        self.base_url = "https://api.minimax.io/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    # ── Step 1: Generate Reference Images ─────────────────────

    def generate_character_images(self, band: list[dict]) -> dict[str, str]:
        """Generate reference images for each band member using image-01.

        Returns dict mapping character_id -> image_url.
        """
        print(f"\n🎨 Step 1: Generating character reference images...")

        ref_urls = {}
        for m in band:
            char_key = f"{m['character_id']}_{m['gender']}"
            print(f"   🖌️  Generating {m['character_name']} ({m['gender']})...")

            try:
                response = requests.post(
                    f"{self.base_url}/image_generation",
                    headers=self.headers,
                    json={
                        "model": "image-01",
                        "prompt": m["image_prompt"],
                        "aspect_ratio": "3:4",
                        "response_format": "url",
                        "n": 1,
                    },
                    timeout=120
                )

                data = response.json()
                status_code = data.get("base_resp", {}).get("status_code", -1)

                if status_code == 0:
                    urls = data.get("data", {}).get("image_urls", [])
                    if urls:
                        ref_urls[char_key] = urls[0]
                        # Also save locally
                        img_resp = requests.get(urls[0], timeout=60)
                        img_path = self.refs_dir / f"{char_key}.png"
                        img_path.write_bytes(img_resp.content)
                        print(f"      ✅ Saved: {img_path}")
                    else:
                        print(f"      ⚠️ No image URL returned")
                else:
                    status_msg = data.get("base_resp", {}).get("status_msg", "unknown")
                    print(f"      ⚠️ Image API error: {status_code} - {status_msg}")

                time.sleep(2)  # Rate limit

            except Exception as e:
                print(f"      ⚠️ Error: {e}")

        print(f"   ✅ Generated {len(ref_urls)}/{len(band)} character images")
        return ref_urls

    # ── Step 2: Generate Music ────────────────────────────────

    def generate_music(self, prompt: str) -> tuple[str, float]:
        """Generate music and return (path, duration_seconds)."""
        print(f"\n🎵 Step 2: Generating music...")
        print(f"   Prompt: {prompt}")

        if not self.api_key:
            print("   ⚠️ No MINIMAX_API_KEY found")
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

    # ── Step 3: Generate Video Clips ──────────────────────────

    def _submit_video_task(self, prompt: str, model: str,
                           subject_image_url: str = None) -> str:
        """Submit a video generation task.

        If subject_image_url is provided, uses S2V-01 with subject reference
        for character consistency. Otherwise uses standard text-to-video.
        """
        payload = {"prompt": prompt}

        if subject_image_url:
            payload["model"] = "S2V-01"
            payload["subject_reference"] = [{
                "type": "character",
                "image": [subject_image_url],
            }]
        else:
            payload["model"] = model

        response = requests.post(
            f"{self.base_url}/video_generation",
            headers=self.headers,
            json=payload,
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

    def generate_video_clips(self, clip_configs: list[dict],
                              ref_urls: dict[str, str],
                              fallback_model: str) -> list[str]:
        """Generate video clips from clip configs.

        For close-ups with a subject_member and available reference image,
        uses S2V-01 subject reference mode for character consistency.
        """
        num_clips = len(clip_configs)
        print(f"\n🎬 Step 3: Generating {num_clips} video clips...")

        BATCH_SIZE = 5
        tasks = []

        for i, config in enumerate(clip_configs):
            if i > 0 and i % BATCH_SIZE == 0:
                print(f"   ⏸️  Pausing 60s for rate limit (batch {i // BATCH_SIZE + 1})...")
                time.sleep(60)

            member = config["subject_member"]
            subject_url = None

            if member:
                char_key = f"{member['character_id']}_{member['gender']}"
                subject_url = ref_urls.get(char_key)
                clip_type = f"close-up of {member['character_name']}"
            else:
                clip_type = "wide/group shot"

            print(f"   📤 Clip {i+1}/{num_clips} ({clip_type})...")

            task_id = ""
            for retry in range(3):
                task_id = self._submit_video_task(
                    config["prompt"], fallback_model, subject_url)
                if task_id:
                    break
                wait = 30 * (retry + 1)
                print(f"      ⏸️  Rate limited, retrying in {wait}s...")
                time.sleep(wait)

            if task_id:
                tasks.append((i, task_id))
                print(f"      Task ID: {task_id}")
            else:
                print(f"      ⚠️ Clip {i+1} skipped")

            time.sleep(2)

        if not tasks:
            print("   ⚠️ No tasks submitted")
            return []

        # Poll all tasks
        print(f"\n   ⏳ Waiting for {len(tasks)} clips...")
        pending = dict(tasks)
        completed = {}

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
                    completed[idx] = data.get("file_id", "")
                    print(f"      ✅ Clip {idx+1} ready")
                elif status == "Fail":
                    print(f"      ❌ Clip {idx+1} failed: {data.get('error_message', '')}")
                else:
                    still_pending[idx] = task_id

            pending = still_pending
            if pending:
                print(f"      ⏳ {len(pending)} processing, {len(completed)} done...")

        # Download and re-encode
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

    # ── Step 4: Merge Final Video ─────────────────────────────

    def merge_final_video(self, clip_paths: list[str], music_path: str) -> str:
        """Concatenate clips and merge with music using ffmpeg."""
        print(f"\n🎞️ Step 4: Building final music video...")

        if not clip_paths:
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

    # ── Step 5: Lip-sync via Sync.so ─────────────────────────

    def lip_sync(self, video_path: str, audio_path: str) -> str:
        """Apply AI lip-sync to the final video using Sync.so API.

        Requires SYNC_API_KEY in .env. If not set, skips lip-sync.
        The API needs publicly accessible URLs, so we upload to a temp host.
        """
        sync_api_key = os.getenv("SYNC_API_KEY", "")
        if not sync_api_key:
            print("\n👄 Step 5: Lip-sync skipped (no SYNC_API_KEY)")
            print("   To enable, add SYNC_API_KEY to .env (get one at https://sync.so)")
            return video_path

        print(f"\n👄 Step 5: Applying lip-sync via Sync.so...")

        try:
            # Sync.so needs URLs — use file upload to get accessible URLs
            # Upload video
            print("   📤 Uploading video to Sync.so...")
            upload_headers = {
                "x-api-key": sync_api_key,
            }

            with open(video_path, "rb") as vf:
                upload_resp = requests.post(
                    "https://api.sync.so/v2/upload",
                    headers=upload_headers,
                    files={"file": ("video.mp4", vf, "video/mp4")},
                    timeout=300
                )

            if upload_resp.status_code not in (200, 201):
                print(f"   ⚠️ Video upload failed: {upload_resp.text[:200]}")
                return video_path

            video_upload = upload_resp.json()
            video_url = video_upload.get("url", "")
            video_asset_id = video_upload.get("id", "")

            # Upload audio
            print("   📤 Uploading audio to Sync.so...")
            with open(audio_path, "rb") as af:
                upload_resp = requests.post(
                    "https://api.sync.so/v2/upload",
                    headers=upload_headers,
                    files={"file": ("audio.mp3", af, "audio/mpeg")},
                    timeout=300
                )

            if upload_resp.status_code not in (200, 201):
                print(f"   ⚠️ Audio upload failed: {upload_resp.text[:200]}")
                return video_path

            audio_upload = upload_resp.json()
            audio_url = audio_upload.get("url", "")
            audio_asset_id = audio_upload.get("id", "")

            # Create lip-sync generation job
            print("   🎬 Creating lip-sync job...")
            gen_headers = {
                "x-api-key": sync_api_key,
                "Content-Type": "application/json",
            }

            # Build input — prefer assetId if available, fall back to url
            video_input = {"type": "video"}
            if video_asset_id:
                video_input["assetId"] = video_asset_id
            else:
                video_input["url"] = video_url

            audio_input = {"type": "audio", "refId": "audio_track"}
            if audio_asset_id:
                audio_input["assetId"] = audio_asset_id
            else:
                audio_input["url"] = audio_url

            gen_resp = requests.post(
                "https://api.sync.so/v2/generate",
                headers=gen_headers,
                json={
                    "model": "lipsync-2",
                    "input": [video_input, audio_input],
                    "options": {
                        "sync_mode": "cut_off",
                    },
                },
                timeout=60
            )

            if gen_resp.status_code not in (200, 201):
                print(f"   ⚠️ Job creation failed: {gen_resp.text[:200]}")
                return video_path

            job = gen_resp.json()
            job_id = job.get("id", "")
            print(f"   📋 Job ID: {job_id}")

            # Poll for completion
            max_attempts = 120  # 20 min max
            for attempt in range(max_attempts):
                time.sleep(10)

                status_resp = requests.get(
                    f"https://api.sync.so/v2/generate/{job_id}",
                    headers={"x-api-key": sync_api_key},
                    timeout=30
                )

                status_data = status_resp.json()
                status = status_data.get("status", "")

                if status == "COMPLETED":
                    output_url = status_data.get("outputUrl", "")
                    if output_url:
                        # Download lip-synced video
                        lipsync_path = self.output_dir / "final_video_lipsync.mp4"
                        dl_resp = requests.get(output_url, timeout=300)
                        lipsync_path.write_bytes(dl_resp.content)
                        print(f"   ✅ Lip-synced video: {lipsync_path}")
                        return str(lipsync_path)
                    else:
                        print("   ⚠️ No output URL in completed job")
                        return video_path

                elif status in ("FAILED", "REJECTED"):
                    error = status_data.get("error", "unknown")
                    print(f"   ❌ Lip-sync failed: {error}")
                    return video_path

                elif attempt % 6 == 0:
                    print(f"   ⏳ Lip-sync processing... ({status})")

            print("   ⚠️ Lip-sync timed out")
            return video_path

        except Exception as e:
            print(f"   ⚠️ Lip-sync error: {e}")
            return video_path

    # ── Main Pipeline ─────────────────────────────────────────

    def run(self, prompt: str, band: list[dict],
            video_model: str = "MiniMax-Hailuo-2.3"):
        """Run the full pipeline."""
        print("\n" + "=" * 60)
        print("  🎸 Music Video Generator (MiniMax Edition)")
        print("=" * 60)

        # Display band lineup
        print("\n🎤 Band Lineup:")
        for m in band:
            gender_icon = "♀" if m["gender"] == "female" else "♂"
            print(f"   {m['role']['name']:20s} → {m['character_name']} "
                  f"({m['species']}) {gender_icon}")

        # Step 1: Generate reference images
        ref_urls = self.generate_character_images(band)

        # Step 2: Generate music
        music_path, music_duration = self.generate_music(prompt)
        if not music_path:
            print("\n❌ Music generation failed. Aborting.")
            return ""

        # Step 3: Generate video clips
        num_clips = max(1, math.ceil(music_duration / CLIP_DURATION))
        print(f"\n   📊 Music is {music_duration:.1f}s — need {num_clips} clips")

        clip_configs = build_scene_sequence(band, num_clips)
        clip_paths = self.generate_video_clips(clip_configs, ref_urls, video_model)

        if not clip_paths:
            print("\n❌ Video generation failed. Aborting.")
            return ""

        # Step 4: Merge clips + music
        merged_path = self.merge_final_video(clip_paths, music_path)
        if not merged_path:
            print("\n❌ Failed to merge video.")
            return ""

        # Step 5: Lip-sync (optional, requires SYNC_API_KEY)
        final_path = self.lip_sync(merged_path, music_path)

        print("\n" + "=" * 60)
        print(f"  ✅ Done! Final music video: {final_path}")
        print("=" * 60 + "\n")

        return final_path


def parse_assignments(assign_list: list[str]) -> dict[str, str]:
    """Parse 'role=character' strings into a dict."""
    assignments = {}
    if not assign_list:
        return assignments
    for item in assign_list:
        if "=" not in item:
            print(f"⚠️ Invalid format: {item} (expected role=character)")
            continue
        role_id, char_id = item.split("=", 1)
        if role_id not in BAND_ROLES:
            print(f"⚠️ Unknown role: {role_id}. Available: {', '.join(BAND_ROLES.keys())}")
            continue
        if char_id not in ANIMAL_CHARACTERS:
            print(f"⚠️ Unknown character: {char_id}. Use --list-characters to see options.")
            continue
        assignments[role_id] = char_id
    return assignments


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Music Video Generator — Cartoon Animal Band (MiniMax)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 4-piece band with female vocalist
  python src/main.py --prompt "A happy pop song" --band-size 4 --vocal-gender female

  # 5-piece band with custom assignments
  python src/main.py --prompt "A rock anthem" --band-size 5 \\
    --assign vocalist=thunder_wolf guitarist=spike_hedgehog

  # Browse characters and roles
  python src/main.py --list-characters
  python src/main.py --list-roles
        """
    )
    parser.add_argument("--prompt", type=str, help="Music prompt")
    parser.add_argument("--band-size", type=int, default=4, choices=range(3, 9),
                        help="Number of band members (3-8, default: 4)")
    parser.add_argument("--vocal-gender", type=str, default="male",
                        choices=["male", "female"],
                        help="Gender of the vocalist (default: male)")
    parser.add_argument("--assign", nargs="*", metavar="ROLE=CHARACTER",
                        help="Assign animals to roles (e.g. vocalist=luna_cat)")
    parser.add_argument("--video-model", type=str, default="MiniMax-Hailuo-2.3",
                        choices=["MiniMax-Hailuo-2.3", "MiniMax-Hailuo-02"],
                        help="Fallback video model for wide shots")
    parser.add_argument("--list-characters", action="store_true",
                        help="List all available animal characters")
    parser.add_argument("--list-roles", action="store_true",
                        help="List all available band roles")
    args = parser.parse_args()

    if args.list_characters:
        print("\n🐾 Available Animal Characters (each has male + female variant):\n")
        print(list_characters())
        print(f"\n   Total: {len(ANIMAL_CHARACTERS)} characters × 2 genders = "
              f"{len(ANIMAL_CHARACTERS) * 2} variants\n")
        exit(0)

    if args.list_roles:
        print("\n🎸 Available Band Roles:\n")
        print(list_roles())
        print(f"\n   Total: {len(BAND_ROLES)} roles\n")
        print("   Default roles by band size:")
        for size, roles in BAND_PRESETS.items():
            print(f"     {size} members: {', '.join(roles)}")
        print()
        exit(0)

    if not args.prompt:
        parser.error("--prompt is required (unless using --list-characters or --list-roles)")

    # Build the band
    assignments = parse_assignments(args.assign)
    band = build_band(args.band_size, assignments, args.vocal_gender)

    generator = MusicVideoGenerator()
    generator.run(args.prompt, band, args.video_model)
