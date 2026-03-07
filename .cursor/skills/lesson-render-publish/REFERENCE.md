# Lesson Render Publish Reference

## Core execution entrypoints

| Command surface | Path | Role |
|---|---|---|
| Shared workflow CLI | `.cursor/skills/video-core-protocol/scripts/workflow.py` | `status`, `render`, `render-all`, `publish` |
| Lesson bootstrap CLI | `.cursor/skills/video-core-protocol/scripts/create_lesson.py` | Creates lesson folder and prints layered execution order |

## Runtime source dependencies

| Src asset | Why this skill depends on it |
|---|---|
| `src/animate/lesson_vertical.py` | Manim scene base classes, resource preparation, cover injection, and series-specific runtime behavior |
| `src/utils/anim_helper.py` | Audio duration timing, combined voice+BGM generation, PNG icon loading |
| `src/utils/voice_edgetts.py` | Voice clip generation during lesson resource preparation |
| `src/utils/cover_generator.py` | Cover image generation during resource preparation |
| `src/utils/icon_helper.py` | Final icon fallback path when PNG icon lookup fails |

## Runtime asset chain

- `src/animate/lesson_vertical.py` calls `gen_voice_clips_from_json()` from `src/utils/voice_edgetts.py`
- `src/animate/lesson_vertical.py` calls `generate_cover()` from `src/utils/cover_generator.py`
- `src/animate/lesson_vertical.py` calls `get_audio_duration()`, `combine_audio_clips()`, and `load_png_icon()` from `src/utils/anim_helper.py`
- `src/utils/anim_helper.py` falls back to `src/utils/icon_helper.py` when PNG icon lookup cannot resolve an asset

## Non-git asset caveats

- `assets/icons8/` metadata and image directories may be absent; icon loading degrades to fallbacks
- `series/cover/<series_name>/` may be absent; cover generation then warns and skips
- `series/bgm/<series_name>/bgm.wav` may be absent; BGM is skipped without blocking render
- Edge TTS needs network access for fresh voice generation
