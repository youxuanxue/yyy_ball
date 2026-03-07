# Chinese Series Orchestrator Reference

## Full-chain asset routing

| Step | Skill | Repo assets touched |
|---|---|---|
| 1 | `series-zsxq-adapter` / `series-sunzi-adapter` | Series prompt paths, lesson numbering, source location |
| 2 | `lesson-content-planning` | `series/prompts/*_script.prompt`, lesson source data, `wechat.md` generation |
| 3 | `lesson-animation-authoring` | `series/prompts/*_annimate.prompt`, `src/animate/__init__.py`, `src/animate/lesson_vertical.py`, `src/utils/anim_helper.py` |
| 4 | `lesson-render-publish` | `.cursor/skills/video-core-protocol/scripts/workflow.py`, `src/animate/lesson_vertical.py`, `src/utils/anim_helper.py`, `src/utils/voice_edgetts.py`, `src/utils/cover_generator.py`, `src/utils/icon_helper.py` |
| 5 | `skill-evolver` | Observation JSON and reports |

## Series-specific note

- `sunzi` additionally owns `series/template/sunzi/cover_template.html`
- Both Chinese series produce `wechat.md` in the planning layer before render
