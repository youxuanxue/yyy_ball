# Chinese Series Orchestrator Reference

## Full-chain asset routing

| Step | Skill | Repo assets touched |
|---|---|---|
| 1 | `series-zsxq-adapter` / `series-sunzi-adapter` | Adapter-local prompts, lesson numbering, source location |
| 2 | `lesson-content-planning` | Adapter's `*_script.prompt`, lesson source data, `wechat.md` generation |
| 3 | `lesson-animation-authoring` | Adapter's `*_annimate.prompt`, `src/animate/*`, `src/utils/*`, `.cursor/skills/video-core-protocol/scripts/workflow.py` |
| 4 | `skill-evolver` | Observation JSON and reports |

## Publishing

Publishing is executed directly via the shared workflow CLI rather than through a separate skill layer:

```bash
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series <series> --media-publisher-dir "$MEDIA_PUBLISHER_DIR" publish <lesson>
```

## Series-specific note

- `sunzi` additionally owns `cover_template.html` in its adapter skill directory
- Both Chinese series produce `wechat.md` in the planning layer before render
