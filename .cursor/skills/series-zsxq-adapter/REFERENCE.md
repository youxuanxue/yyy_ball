# Series Adapter Reference: ZSXQ

## Series-owned assets

| Asset type | Path | Used by |
|---|---|---|
| Script prompt | `series/prompts/zsxq_100ke_script.prompt` | `lesson-content-planning` |
| Animation prompt | `series/prompts/zsxq_100ke_annimate.prompt` | `lesson-animation-authoring` |
| Source content | `assets/zsxq/jingpin_100ke_posts.json` | `lesson-content-planning` |

## Content contract

- Pre-render outputs: `script.json`, `wechat.md`
- Post-publish outputs: none
- Icon family: finance icons

## Fallback rules

- If the finance icon manifest is unavailable locally, reuse icon names already validated in existing `series/book_zsxq_100ke/lesson*/script.json`
- Do not invent icon file names or prompt-local schema variants
