# MoneyWise Series Orchestrator Reference

## Full-chain asset routing

| Step | Skill | Repo assets touched |
|---|---|---|
| 1 | `series-moneywise-adapter` | Adapter-local prompts (`moneywise_*.prompt`), taxonomy fallback rules |
| 2 | `lesson-content-planning` (pre-render pass) | Adapter's `moneywise_script.prompt`, lesson source data |
| 3 | `lesson-animation-authoring` | Adapter's `moneywise_annimate.prompt`, `src/animate/*`, `src/utils/*`, `.cursor/skills/video-core-protocol/scripts/workflow.py` |
| 4 | `lesson-content-planning` (post-publish pass) | publish metadata + MoneyWise site taxonomy contract |
| 5 | `skill-evolver` | Observation JSON and reports |

## Publishing

Publishing is executed directly via the shared workflow CLI rather than through a separate skill layer:

```bash
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py \
  --series moneywise \
  --media-publisher-dir "$MEDIA_PUBLISHER_DIR" \
  publish <lesson>
```

## Post-publish closure

MoneyWise website MDX is intentionally generated in a second planning pass so that all content artifacts remain owned by `lesson-content-planning`.
