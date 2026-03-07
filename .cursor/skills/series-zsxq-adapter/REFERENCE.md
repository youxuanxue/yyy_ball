# Series Adapter Reference: ZSXQ

## Series-owned assets

| Asset type | Path | Used by |
|---|---|---|
| Script prompt | `.cursor/skills/series-zsxq-adapter/prompts/zsxq_100ke_script.prompt` | `lesson-content-planning` |
| Animation prompt | `.cursor/skills/series-zsxq-adapter/prompts/zsxq_100ke_annimate.prompt` | `lesson-animation-authoring` |
| Icon list | `.cursor/skills/series-zsxq-adapter/icons_finance.txt` | `lesson_vertical.py` icon lookup; fallback to `assets/icons8/` |
| Source content | `assets/zsxq/jingpin_100ke_posts.json` | `lesson-content-planning` |

## Content contract

- Pre-render outputs: `script.json`, `wechat.md`
- Post-publish outputs: none
- Icon family: finance icons

## Fallback rules

- If the finance icon manifest is unavailable locally, reuse icon names already validated in existing `series/book_zsxq_100ke/lesson*/script.json`
- Do not invent icon file names or prompt-local schema variants
