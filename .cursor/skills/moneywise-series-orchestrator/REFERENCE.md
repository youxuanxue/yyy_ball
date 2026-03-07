# MoneyWise Series Orchestrator Reference

## Full-chain asset routing

| Step | Skill | Repo assets touched |
|---|---|---|
| 1 | `series-moneywise-adapter` | `series/prompts/moneywise_*.prompt`, taxonomy fallback rules |
| 2 | `lesson-content-planning` (pre-render pass) | `series/prompts/moneywise_script.prompt`, lesson source data |
| 3 | `lesson-animation-authoring` | `series/prompts/moneywise_annimate.prompt`, `src/animate/lesson_vertical.py`, `src/utils/anim_helper.py` |
| 4 | `lesson-render-publish` | `.cursor/skills/video-core-protocol/scripts/workflow.py`, `src/animate/lesson_vertical.py`, `src/utils/anim_helper.py`, `src/utils/voice_edgetts.py`, `src/utils/cover_generator.py`, `src/utils/icon_helper.py` |
| 5 | `lesson-content-planning` (post-publish pass) | publish metadata + MoneyWise site taxonomy contract |
| 6 | `skill-evolver` | Observation JSON and reports |

## Post-publish closure

MoneyWise website MDX is intentionally generated in a second planning pass so that all content artifacts remain owned by `lesson-content-planning`, while `lesson-render-publish` stays execution-only.
