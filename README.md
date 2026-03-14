# Music Video Generator

Generate full-length music videos with cartoon animal bands from text prompts. Powered by MiniMax APIs (minimax.io).

## Workflow

```
[Your Prompt]
    → 🎵 MiniMax Music API (music-2.5+) — generates a full song with lyrics
    → 🎬 MiniMax Video API (MiniMax-Hailuo-2.3) — generates multiple 6s video clips
    → 🎞️ ffmpeg — concatenates clips + merges music into final music video
```

The tool automatically calculates how many video clips are needed to match the music duration, generates them with varied camera angles/scenes, handles API rate limits, and stitches everything together into one music video with audio.

## Demo

Prompt: *"A joyful upbeat song for a happy animal festival, with playful drums, bouncy bass, cheerful guitar, and fun lyrics about cartoon animals dancing and celebrating together"*

[Download demo video (final_video.mp4)](https://github.com/Luo-mary/music-video-generator/releases/download/v1.0/final_video.mp4)

## Quick Start

### 1. Install dependencies

```bash
cd music-video-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

ffmpeg is also required:
```bash
# macOS
brew install ffmpeg
```

### 2. Configure API Key

```bash
cp .env.example .env
# Edit .env and add your MiniMax API key
```

Get your API key at: https://platform.minimax.io/

Only **one API key** is needed — it covers both music and video generation.

### 3. Run

```bash
python src/main.py --prompt "A joyful upbeat song for a happy animal festival"
```

## Usage

```bash
# Basic — uses default video prompt (cartoon animal band) and model
python src/main.py --prompt "A happy pop song about summer"

# Custom video prompt
python src/main.py \
  --prompt "A rock ballad about friendship" \
  --video-prompt "A cartoon band of animals performing in a stadium with fireworks"

# Use a different video model
python src/main.py --prompt "An energetic dance track" --video-model MiniMax-Hailuo-02
```

### Options

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--prompt` | Yes | — | Music description (style, mood, instruments, theme) |
| `--video-prompt` | No | Cartoon animal band on festival stage | Base video scene description |
| `--video-model` | No | `MiniMax-Hailuo-2.3` | Video model (`MiniMax-Hailuo-2.3` or `MiniMax-Hailuo-02`) |

## MiniMax API

| Service | Model | Description |
|---------|-------|-------------|
| Music | `music-2.5+` | Text-to-music with auto-generated lyrics |
| Video | `MiniMax-Hailuo-2.3` | Hailuo 2.3 — high quality text-to-video |
| Video | `MiniMax-Hailuo-02` | Hailuo 02 — 1080P, up to 10s clips |

API platform: https://platform.minimax.io/
Pricing: https://platform.minimax.io/pricing

## Output

All generated files are saved to the `output/` directory:

| File | Description |
|------|-------------|
| `music.mp3` | Generated song |
| `clips/clip_XXX_enc.mp4` | Individual re-encoded video clips |
| `final_video.mp4` | Final music video (all clips + music merged) |

## Controlling Duration

### Music Length

The Music API has no direct `duration` parameter. Song length is determined by lyrics content:

| Want | How |
|------|-----|
| Shorter song (~1 min) | Write short lyrics — one verse + one chorus |
| Longer song (~3 min) | Write full lyrics with multiple sections |

Use the `--prompt` to describe the song, and structure your lyrics with tags like `[Verse]`, `[Chorus]`, `[Bridge]`, `[Outro]` to control the song structure. Enable `lyrics_optimizer` (on by default) to auto-generate lyrics from your prompt.

### Video Length

Each video clip has a fixed max duration depending on the model:

| Model | Clip Duration |
|-------|---------------|
| `MiniMax-Hailuo-2.3` | ~6 seconds |
| `MiniMax-Hailuo-02` | up to 10 seconds |

The tool automatically generates enough clips to cover the full music duration. Using `MiniMax-Hailuo-02` means fewer clips needed (and fewer API calls).

### Final Video

The final video length is determined by whichever is shorter — the concatenated video or the music track. They are merged with `ffmpeg -shortest`.

## How It Works

1. **Music generation** — Sends the prompt to MiniMax Music API (`music-2.5+`), receives hex-encoded MP3 audio
2. **Clip calculation** — Determines how many ~6s video clips are needed to cover the full song duration
3. **Video generation** — Submits all clip tasks to MiniMax Hailuo API with varied scene descriptions (close-ups, wide shots, different instruments), handles rate limits with automatic batching and retries
4. **Polling** — Monitors all tasks concurrently until all clips are ready
5. **Download & encode** — Downloads each clip and re-encodes with ffmpeg for consistent format
6. **Final merge** — Concatenates all clips and overlays the music track using ffmpeg

## Requirements

- Python 3.10+
- ffmpeg
- MiniMax API key (minimax.io)
