# Music Video Generator

Generate full-length music videos with customizable cartoon animal bands from text prompts. Powered by MiniMax APIs (minimax.io).

## Workflow

```
[Your Prompt] + [Band Setup]
    → 🎤 Choose band size (3-8 members) and assign roles
    → 🐾 Pick animal characters for each role from the character library
    → 🎵 MiniMax Music API (music-2.5+) — generates a full song with lyrics
    → 🎬 MiniMax Video API (Hailuo) — generates multiple clips with consistent characters
    → 🎞️ ffmpeg — concatenates clips + merges music into final music video
```

## Demo

Prompt: *"A joyful upbeat song for a happy animal festival"*

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
# Default 4-piece band
python src/main.py --prompt "A joyful upbeat song for a happy animal festival"

# Custom 5-piece band with specific characters
python src/main.py --prompt "A rock anthem" --band-size 5 \
  --assign vocalist=thunder_wolf guitarist=spike_hedgehog bassist=duke_crocodile
```

## Character System

### Band Roles (8 available)

| Role ID | Role | Instrument | Stage Position |
|---------|------|------------|----------------|
| `vocalist` | Lead Vocalist | Microphone | Center stage, front |
| `guitarist` | Lead Guitarist | Electric guitar | Stage right, front |
| `bassist` | Bass Guitarist | Bass guitar | Stage left, front |
| `drummer` | Drummer | Drum kit | Center stage, back |
| `keyboardist` | Keyboardist | Keyboard synthesizer | Stage left, back |
| `saxophonist` | Saxophonist | Saxophone | Stage right, back |
| `violinist` | Violinist | Violin | Stage right, middle |
| `dj` | DJ / Turntablist | DJ turntables & mixer | Stage left, elevated |

### Band Size Presets

| Size | Roles |
|------|-------|
| 3 | vocalist, guitarist, drummer |
| 4 | vocalist, guitarist, bassist, drummer |
| 5 | vocalist, guitarist, bassist, drummer, keyboardist |
| 6 | vocalist, guitarist, bassist, drummer, keyboardist, saxophonist |
| 7 | + violinist |
| 8 | + dj |

### Animal Characters (20 available)

Each character has a **detailed visual description** including species, clothing, accessories, and personality — ensuring consistent appearance across all video clips.

| Character ID | Name | Species | Personality |
|-------------|------|---------|-------------|
| `rocky_bear` | Rocky the Bear | Brown Bear | The confident powerhouse — big, loud, and full of heart |
| `luna_cat` | Luna the Cat | Siamese Cat | Cool, mysterious diva with effortless grace |
| `max_dog` | Max the Dog | Golden Retriever | The eternally happy, enthusiastic good boy |
| `jazz_rabbit` | Jazz the Rabbit | Dutch Rabbit | The intellectual artist — sophisticated and witty |
| `spike_hedgehog` | Spike the Hedgehog | Hedgehog | The punk rebel — small but fierce |
| `coco_panda` | Coco the Panda | Giant Panda | The sweet, lovable one who melts hearts |
| `blaze_fox` | Blaze the Fox | Red Fox | The suave showman — charming and stylish |
| `ella_elephant` | Ella the Elephant | African Elephant | The gentle giant — soulful and wise |
| `ricky_raccoon` | Ricky the Raccoon | Raccoon | The street-smart trickster |
| `melody_owl` | Melody the Owl | Barn Owl | The nocturnal maestro — wise and mysterious |
| `bubbles_frog` | Bubbles the Frog | Tree Frog | The groovy free spirit — chill and funky |
| `thunder_wolf` | Thunder the Wolf | Gray Wolf | The intense lone wolf — powerful and magnetic |
| `poppy_penguin` | Poppy the Penguin | Emperor Penguin | The showstopper — tiny and theatrical |
| `samba_parrot` | Samba the Parrot | Scarlet Macaw | The flamboyant showbird — loud and colorful |
| `indie_deer` | Indie the Deer | White-tailed Deer | The indie dreamer — gentle and artistic |
| `duke_crocodile` | Duke the Crocodile | Crocodile | The smooth operator — cool as ice, blues soul |
| `pixel_chameleon` | Pixel the Chameleon | Panther Chameleon | The tech-savvy wildcard — innovative |
| `rosie_flamingo` | Rosie the Flamingo | Flamingo | The glamorous diva — elegant and dramatic |
| `banjo_monkey` | Banjo the Monkey | Capuchin Monkey | The hyperactive multi-instrumentalist |
| `aurora_snake` | Aurora the Snake | King Cobra | The mesmerizing enchantress — hypnotic |

### Default Role Assignments

If you don't specify `--assign`, each role gets a default character:

| Role | Default Character |
|------|------------------|
| Vocalist | Thunder the Wolf |
| Guitarist | Blaze the Fox |
| Bassist | Duke the Crocodile |
| Drummer | Rocky the Bear |
| Keyboardist | Coco the Panda |
| Saxophonist | Jazz the Rabbit |
| Violinist | Indie the Deer |
| DJ | Ricky the Raccoon |

## Usage

```bash
# Default 4-piece band (vocalist, guitarist, bassist, drummer)
python src/main.py --prompt "A happy pop song about summer"

# 6-piece band
python src/main.py --prompt "A jazz fusion jam" --band-size 6

# Custom character assignments
python src/main.py --prompt "A punk rock song" --band-size 4 \
  --assign vocalist=spike_hedgehog guitarist=samba_parrot \
           bassist=aurora_snake drummer=banjo_monkey

# Use the higher quality video model
python src/main.py --prompt "A ballad" --band-size 3 --video-model MiniMax-Hailuo-02

# Browse available characters and roles
python src/main.py --list-characters
python src/main.py --list-roles
```

### Options

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--prompt` | Yes | — | Music description (style, mood, instruments, theme) |
| `--band-size` | No | `4` | Number of band members (3-8) |
| `--assign` | No | See defaults above | Map roles to characters (e.g. `vocalist=luna_cat`) |
| `--video-model` | No | `MiniMax-Hailuo-2.3` | Video model (`MiniMax-Hailuo-2.3` or `MiniMax-Hailuo-02`) |
| `--list-characters` | — | — | Show all 20 animal characters |
| `--list-roles` | — | — | Show all 8 band roles and presets |

## Character Consistency

To maintain visual consistency across clips, every video prompt includes the **full detailed character description** (appearance, clothing, accessories). The clip sequence alternates between:

1. **Wide/group shots** — all band members visible on stage together
2. **Close-up shots** — rotating through each individual member
3. **Dynamic shots** — action/energy moments (jumping, confetti, crowd)

This ensures each character looks the same throughout the entire music video.

## MiniMax API

| Service | Model | Description |
|---------|-------|-------------|
| Music | `music-2.5+` | Text-to-music with auto-generated lyrics |
| Video | `MiniMax-Hailuo-2.3` | Hailuo 2.3 — high quality text-to-video (~6s clips) |
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

Use `[Verse]`, `[Chorus]`, `[Bridge]`, `[Outro]` tags in your prompt to hint at structure.

### Video Length

| Model | Clip Duration |
|-------|---------------|
| `MiniMax-Hailuo-2.3` | ~6 seconds |
| `MiniMax-Hailuo-02` | up to 10 seconds |

The tool generates enough clips to cover the full music duration. Using `MiniMax-Hailuo-02` means fewer clips and fewer API calls.

### Final Video

The final video is trimmed to whichever is shorter — the concatenated video or the music track (`ffmpeg -shortest`).

## How It Works

1. **Band setup** — User selects band size and assigns animal characters to roles
2. **Music generation** — Sends prompt to MiniMax Music API, receives generated song
3. **Scene planning** — Builds a sequence of prompts alternating wide shots and close-ups, each containing full character descriptions for consistency
4. **Video generation** — Submits clip tasks in batches (rate limit aware), polls until complete
5. **Download & encode** — Downloads clips and re-encodes with ffmpeg for consistent format
6. **Final merge** — Concatenates all clips and overlays the music track

## Requirements

- Python 3.10+
- ffmpeg
- MiniMax API key (minimax.io)
