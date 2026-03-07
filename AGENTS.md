# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

This is a Chinese educational video production pipeline that uses **Manim** (animation engine), **Edge TTS** (voice synthesis), and **Playwright** (cover generation & publishing) to produce animated short-form vertical videos (1080x1920, 9:16). See `README.md` for full details.

Three active series exist:

| Series | Directory | Base class | Lessons w/ `animate.py` |
|---|---|---|---|
| 孙子兵法 (Sun Tzu for Kids) | `series/book_sunzibingfa/` | `SunziLessonVertical` | lesson06 |
| 精品100课理财 (Finance 100) | `series/book_zsxq_100ke/` | `Zsxq100keLessonVertical` | lesson021–040 |
| MoneyWise Global (English) | `series/moneywise_global/` | `MoneyWiseLessonVertical` | lesson001–020 |

Two content-only series (`book_lunyu/`, `book_yijing/`) have `origin.md` / `script.json` but no `animate.py` yet.

### Key commands

- **Render a lesson** (from the lesson directory): `uv run manim -ql --disable_caching animate.py ClassName`
  - Use `-ql` for low quality (fast, ~30s), `-qh` for high quality (production)
  - Class name convention: `Lesson<NNN>VerticalScenes` — `NNN` matches the lesson directory number (e.g. `Lesson021VerticalScenes` for `lesson021/`)
- **Quick smoke-test render** (known-good, ~30s):
  ```bash
  cd series/book_sunzibingfa/lesson06
  uv run manim -ql --disable_caching animate.py Lesson06VerticalScenes
  ```
- **Generate voice only**: `uv run python series/<book>/<lessonXX>/gen_voice.py`
- **Generate cover only**: `uv run python series/<book>/<lessonXX>/gen_cover.py`
- No lint or test framework is configured; validation is done by rendering.

### Workflow skills

The skill system is now layered:
- Core contract: `.cursor/skills/video-core-protocol/SKILL.md`
- Planning: `.cursor/skills/lesson-content-planning/SKILL.md`
- Animation: `.cursor/skills/lesson-animation-authoring/SKILL.md`
- Render/publish: `.cursor/skills/lesson-render-publish/SKILL.md`
- Series adapters: `.cursor/skills/series-zsxq-adapter/`, `.cursor/skills/series-sunzi-adapter/`, `.cursor/skills/series-moneywise-adapter/`
- Evolver: `.cursor/skills/skill-evolver/SKILL.md`
- Top-level orchestrators:
  - `.cursor/skills/chinese-series-orchestrator/SKILL.md`
  - `.cursor/skills/moneywise-series-orchestrator/SKILL.md`

Prompt/template/src runtime asset closure now lives in the corresponding `REFERENCE.md` files inside these skill directories.

### External skills (auto-synced)

The update script clones the repo specified by the `AGENT_SKILLS_REPO` env var (or its hardcoded default) into `~/.cache/agent-skills` and rsyncs two skill directories into `~/.cursor/skills/`:
- `inspur-ppt-gen` — PPT generation from templates
- `ppt-content-planning` — Slide content planning

If `AGENT_SKILLS_GIT_TOKEN` is set (as a Cursor secret), it is used for private repo access. Token is never printed to logs.

### Source architecture

```
src/animate/lesson_vertical.py   # LessonVertical (ABC) + 3 concrete base classes
src/utils/anim_helper.py         # Audio timeline, icon loading, ffmpeg helpers
src/utils/voice_edgetts.py       # Edge TTS voice synthesis
src/utils/cover_generator.py     # Playwright-based HTML→PNG cover generator
src/utils/icon_helper.py         # Icons8 PNG icon utilities
src/crawlers/                    # Data crawlers (ZSXQ, Lunyu, Yijing) — optional
```

### Prerequisites (already in VM snapshot)

- Python 3.13+ (installed via `deadsnakes` PPA)
- `uv` package manager (`~/.local/bin/uv`)
- System packages: `ffmpeg`, `libpango1.0-dev`, `libcairo2-dev`, `pkg-config`
- Playwright Chromium browser (`uv run playwright install chromium`)
- `.venv` (8.4 GB), `~/.cache/uv` (8.5 GB), `~/.cache/ms-playwright` (613 MB) are all pre-populated in the snapshot; `uv sync` takes <100 ms on warm start.
- `rsync` (installed for skills sync)

### Non-obvious caveats

- `pyproject.toml` requires Python >= 3.13. The default system Python 3.12 will not work with `uv sync`.
- `uv` is installed to `~/.local/bin/` — ensure `PATH` includes it. The update script handles this.
- The `pydub` library emits `SyntaxWarning` on Python 3.13 about invalid escape sequences — this is harmless and comes from an upstream dependency.
- `assets/icons8/` directory and `assets/bgm/` directory are **not** checked into git (large binary assets); icon loading falls back gracefully when missing. `series/cover/` is also empty in git. These missing assets cause warnings but do not block rendering.
- Cover generation requires source images in `series/cover/<series_name>/`. If missing, cover is skipped with a warning but rendering still succeeds.
- Voice generation uses Edge TTS (Microsoft cloud, free, no API key needed) and requires network access.
- CosyVoice and SadTalker are optional git submodules and not required for the core pipeline.
- No formal lint or test framework is configured in this project.
- Generated `media/`, `voice/`, and `images/` directories appear in lesson folders during rendering — these are gitignored build artifacts.
