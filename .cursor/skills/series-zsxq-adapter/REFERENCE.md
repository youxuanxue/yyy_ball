# Series Adapter Reference: ZSXQ

## Series-owned assets

| Asset type | Path | Used by |
|---|---|---|
| Script prompt | `series/prompts/zsxq_100ke_script.prompt` | `lesson-content-planning` |
| Animation prompt | `series/prompts/zsxq_100ke_annimate.prompt` | `lesson-animation-authoring` |
| Source content | `assets/zsxq/jingpin_100ke_posts.json` | `lesson-content-planning` |
| Source refresh script | `.cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py` | Maintainers refreshing `assets/zsxq/jingpin_100ke_posts.json` |

## Content contract

- Pre-render outputs: `script.json`, `wechat.md`
- Post-publish outputs: none
- Icon family: finance icons

## Source refresh closure

- The ZSXQ dataset refresh entrypoint lives with this adapter at `.cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py`
- The script writes to `assets/zsxq/jingpin_100ke_posts.json` and `assets/zsxq/jingpin_100ke_posts_raw.json`
- It requires `ZSXQ_ACCESS_TOKEN` in the environment and should be treated as adapter-owned maintenance logic, not shared runtime

## Fallback rules

- If the finance icon manifest is unavailable locally, reuse icon names already validated in existing `series/book_zsxq_100ke/lesson*/script.json`
- Do not invent icon file names or prompt-local schema variants
