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

## Skill-owned scripts covered by protocol checks

| Skill | Script path | Role |
|---|---|---|
| `lesson-content-planning` | `.cursor/skills/lesson-content-planning/scripts/audit_content.py` | Lesson output audit entrypoint |
| `series-zsxq-adapter` | `.cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py` | Adapter-owned source refresh entrypoint |
| `skill-evolver` | `.cursor/skills/skill-evolver/scripts/evolve.py` | Observation recording and summary entrypoint |

## Shared runtime source dependencies

| Src asset | Why it matters |
|---|---|
| `src/animate/__init__.py` | Unified re-export surface for lesson animation base classes |
| `src/animate/lesson_vertical.py` | Shared vertical lesson runtime, series base classes, resource preparation |
| `src/utils/anim_helper.py` | Audio timing, audio composition, and PNG icon loading |

## Prompt and template ownership model

| Concern | Owned by | Source assets |
|---|---|---|
| Script/content prompt assets | `lesson-content-planning` + series adapters | `series/prompts/*_script.prompt` |
| Animation prompt assets | `lesson-animation-authoring` + series adapters | `series/prompts/*_annimate.prompt` |
| Cover HTML template assets | series adapter + render stack | `series/template/sunzi/cover_template.html` |

## Validation boundary

`check_protocol.py` validates:

1. Every managed skill has `SKILL.md`
2. Required `REFERENCE.md` files exist for managed skills that own repo assets
3. Required skill-owned scripts exist
4. Required prompt/template assets exist
5. Required `src` runtime assets exist
6. Skill docs, skill-owned scripts, prompt/template files, and required runtime source files do not contain disallowed absolute paths

## Current managed entrypoints

- `chinese-series-orchestrator`
- `moneywise-series-orchestrator`

They orchestrate the flow, but they must call the core-owned scripts above instead of carrying private copies.
