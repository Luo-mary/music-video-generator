#!/usr/bin/env python3
"""
Music Video Generator Workflow
-------------------------------
1. Generate music from prompt (MiniMax Music API - music-2.5+)
2. Generate multiple video clips (MiniMax Video API - Hailuo)
3. Concatenate clips and merge with music (ffmpeg)

Usage:
    python src/main.py --prompt "A happy upbeat pop song with drums, bass, guitar"
"""

import os
import math
import argparse
import requests
import json
import time
import subprocess
import shutil
from pathlib import Path
from dotenv import load_dotenv

# Config
OUTPUT_DIR = Path(__file__).parent.parent / "output"
SCRIPT_DIR = Path(__file__).parent.parent
CLIP_DURATION = 6  # seconds per Hailuo clip

# Load env vars
load_dotenv(SCRIPT_DIR / ".env")

# Varied scene prompts for different clips to keep the video interesting
SCENE_VARIATIONS = [
    "wide shot of {base}, bright stage lights flashing",
    "close-up of {base}, camera focused on the singer rabbit",
    "medium shot of {base}, camera panning across the band",
    "close-up of the bear playing drums energetically, {base}",
    "close-up of the cat grooving on bass guitar, {base}",
    "close-up of the dog shredding electric guitar, {base}",
    "wide shot of {base}, confetti falling from above",
    "low angle shot of {base}, crowd of cartoon animals cheering",
    "side view of {base}, colorful spotlights sweeping the stage",
    "close-up of the rabbit singing passionately into the microphone, {base}",
    "overhead shot of {base}, balloons floating around",
    "dynamic shot of {base}, all animals jumping together",
]


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
        print(f"\n🎵 Step 1: Generating music...")
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

    def _poll_video_task(self, task_id: str) -> str:
        """Poll until task completes, return file_id."""
        for attempt in range(60):
            time.sleep(10)
            resp = requests.get(
                f"{self.base_url}/query/video_generation",
                headers=self.headers,
                params={"task_id": task_id},
                timeout=30
            )
            data = resp.json()
            status = data.get("status", "")
            if status == "Success":
                return data.get("file_id", "")
            elif status == "Fail":
                print(f"      ❌ Task {task_id} failed: {data.get('error_message', '')}")
                return ""
        return ""

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

    def generate_video_clips(self, base_prompt: str, num_clips: int, model: str) -> list[str]:
        """Generate multiple video clips with scene variations.

        Submits all tasks in parallel, then polls them all.
        """
        print(f"\n🎬 Step 2: Generating {num_clips} video clips...")

        # Build varied prompts
        prompts = []
        for i in range(num_clips):
            variation = SCENE_VARIATIONS[i % len(SCENE_VARIATIONS)]
            prompts.append(variation.format(base=base_prompt))

        # Submit all tasks in batches to respect rate limits
        BATCH_SIZE = 5
        tasks = []  # (index, task_id)
        for i, prompt in enumerate(prompts):
            # Pause between batches to avoid rate limiting
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
        pending = dict(tasks)  # index -> task_id
        completed = {}  # index -> file_id
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
                # Re-encode for consistent format
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
        print(f"\n🎞️ Step 3: Building final music video...")

        if not clip_paths:
            print("   ⚠️ No clips to merge")
            return ""

        # Create ffmpeg concat file
        concat_file = self.output_dir / "concat.txt"
        with open(concat_file, "w") as f:
            for path in clip_paths:
                f.write(f"file '{path}'\n")

        # Concatenate all clips into one video (no audio)
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

        # Merge music onto video — use shortest stream to determine duration
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

        # Get final duration
        probe = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(final_path)],
            capture_output=True, text=True
        )
        duration = float(probe.stdout.strip()) if probe.stdout.strip() else 0

        print(f"   ✅ Final video: {final_path} ({duration:.1f}s)")

        # Cleanup temp files
        concat_file.unlink(missing_ok=True)
        concat_video.unlink(missing_ok=True)

        return str(final_path)

    def run(self, prompt: str, video_prompt: str = None, video_model: str = "MiniMax-Hailuo-2.3"):
        """Run the full workflow."""
        print("\n" + "=" * 60)
        print("  🎸 Music Video Generator (MiniMax Edition)")
        print("=" * 60)

        # Step 1: Generate music
        music_path, music_duration = self.generate_music(prompt)
        if not music_path:
            print("\n❌ Music generation failed. Aborting.")
            return ""

        # Step 2: Generate video clips to cover music duration
        num_clips = max(1, math.ceil(music_duration / CLIP_DURATION))
        print(f"\n   📊 Music is {music_duration:.1f}s — need {num_clips} clips ({CLIP_DURATION}s each)")

        base_video_prompt = video_prompt or "a cartoon band of cute animals - a bear on drums, a cat on bass guitar, a dog on electric guitar, and a rabbit singing - performing on a colorful festival stage with balloons and confetti, cartoon animated style, vibrant colors"
        clip_paths = self.generate_video_clips(base_video_prompt, num_clips, video_model)

        if not clip_paths:
            print("\n❌ Video generation failed. Aborting.")
            return ""

        # Step 3: Merge clips + music into final video
        final_path = self.merge_final_video(clip_paths, music_path)

        if final_path:
            print("\n" + "=" * 60)
            print(f"  ✅ Done! Final music video: {final_path}")
            print("=" * 60 + "\n")
        else:
            print("\n❌ Failed to create final video.")

        return final_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Music Video Generator (MiniMax)")
    parser.add_argument("--prompt", type=str, required=True, help="Music prompt")
    parser.add_argument("--video-prompt", type=str, default=None, help="Video prompt (optional)")
    parser.add_argument("--video-model", type=str, default="MiniMax-Hailuo-2.3",
                        choices=["MiniMax-Hailuo-2.3", "MiniMax-Hailuo-02"],
                        help="Video model to use")
    args = parser.parse_args()

    generator = MusicVideoGenerator()
    generator.run(args.prompt, args.video_prompt, args.video_model)
