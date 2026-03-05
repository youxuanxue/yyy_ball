# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

This is a Chinese educational video production pipeline that uses **Manim** (animation engine), **Edge TTS** (voice synthesis), and **Playwright** (cover generation & publishing) to produce animated short-form vertical videos (1080x1920, 9:16). See `README.md` for full details.

### Key commands

- **Render a lesson** (from the lesson directory): `uv run manim -ql --disable_caching animate.py ClassName`
  - Use `-ql` for low quality (fast), `-qh` for high quality (production)
  - The class name is typically `LessonXXVerticalScenes` (check each `animate.py`)
- **Generate voice only**: `uv run python series/<book>/<lessonXX>/gen_voice.py`
- **Generate cover only**: `uv run python series/<book>/<lessonXX>/gen_cover.py`

### Prerequisites (already in VM snapshot)

- Python 3.13+ (installed via `deadsnakes` PPA)
- `uv` package manager (`~/.local/bin/uv`)
- System packages: `ffmpeg`, `libpango1.0-dev`, `libcairo2-dev`, `pkg-config`
- Playwright Chromium browser (`uv run playwright install chromium`)

### Non-obvious caveats

- `pyproject.toml` requires Python >= 3.13. The default system Python 3.12 will not work with `uv sync`.
- `uv` is installed to `~/.local/bin/` — ensure `PATH` includes it. The update script handles this.
- The `pydub` library emits `SyntaxWarning` on Python 3.13 about invalid escape sequences — this is harmless and comes from an upstream dependency.
- Cover generation requires source images in `series/cover/<series_name>/`. If missing, cover is skipped with a warning but rendering still succeeds.
- Voice generation uses Edge TTS (Microsoft cloud, free, no API key needed) and requires network access.
- CosyVoice and SadTalker are optional git submodules and not required for the core pipeline.
- No formal lint or test framework is configured in this project.
- Generated `media/`, `voice/`, and `images/` directories appear in lesson folders during rendering — these are gitignored build artifacts.
