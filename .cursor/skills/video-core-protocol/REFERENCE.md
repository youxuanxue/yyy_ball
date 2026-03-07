# Video Core Protocol Reference

## Purpose

This document closes the shared execution layer around concrete repo assets.

## Core-owned scripts

| Asset | Path | Role |
|---|---|---|
| Lesson number normalizer | `.cursor/skills/video-core-protocol/scripts/lesson_num.py` | Canonical lesson id parsing and zero-padding |
| Lesson directory bootstrapper | `.cursor/skills/video-core-protocol/scripts/create_lesson.py` | Creates lesson folders and prints layered execution order |
| Shared execution workflow | `.cursor/skills/video-core-protocol/scripts/workflow.py` | `status`, `render`, `render-all`, `publish` for all series |
| Protocol self-check | `.cursor/skills/video-core-protocol/scripts/check_protocol.py` | Verifies managed skills, reference docs, prompt/template assets, and path hygiene |

## Shared runtime (owned by this skill, consumed by all render flows)

These Python modules live in `src/` because they're imported at render time by every lesson `animate.py` via standard Python imports (`from src.animate import ...`). They cannot be moved into a skill directory without breaking all 41+ lesson import paths.

| Src asset | Role |
|---|---|
| `src/animate/__init__.py` | Re-export surface for `SunziLessonVertical`, `Zsxq100keLessonVertical`, `MoneyWiseLessonVertical` |
| `src/animate/lesson_vertical.py` | Base classes, resource preparation (voice/cover/BGM), scene orchestration |
| `src/utils/anim_helper.py` | Audio duration, audio composition, PNG icon loading |
| `src/utils/voice_edgetts.py` | Edge TTS voice clip generation |
| `src/utils/cover_generator.py` | Playwright-based HTML→PNG cover generation |
| `src/utils/icon_helper.py` | SVG/PNG icon fallback when PNG lookup fails |

### Call chain

```
lesson_vertical.py
  ├── voice_edgetts.gen_voice_clips_from_json()
  ├── cover_generator.generate_cover()
  ├── anim_helper.get_audio_duration()
  ├── anim_helper.combine_audio_clips()
  ├── anim_helper.load_png_icon()
  │     └── icon_helper.create_icon()  (fallback)
  └── series subclass overrides (build_scene_N)
```

## Prompt and template ownership model

| Concern | Owned by | Location |
|---|---|---|
| Script/content prompt assets | series adapters | `.cursor/skills/series-*-adapter/prompts/*_script.prompt` |
| Animation prompt assets | series adapters | `.cursor/skills/series-*-adapter/prompts/*_annimate.prompt` |
| Icon list files | series adapters | `.cursor/skills/series-*-adapter/icons_*.txt` |
| Cover HTML template | `series-sunzi-adapter` | `.cursor/skills/series-sunzi-adapter/templates/cover_template.html` |

## Validation boundary

`check_protocol.py` validates:

1. Every managed skill has `SKILL.md`
2. Required `REFERENCE.md` files exist for managed skills that own repo assets
3. Required prompt/template assets exist in their adapter skill directories
4. Required `src` runtime assets exist
5. Skill docs, prompts, templates, and runtime source files do not contain disallowed absolute paths

## Current managed entrypoints

- `chinese-series-orchestrator`
- `moneywise-series-orchestrator`

They orchestrate the flow, but they must call the core-owned scripts above instead of carrying private copies.
