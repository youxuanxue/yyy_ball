# Series Adapter Reference: Sunzi

## Series-owned assets

| Asset type | Path | Used by |
|---|---|---|
| Script prompt | `series/prompts/sunzi_script.prompt` | `lesson-content-planning` |
| Animation prompt | `series/prompts/sunzi_annimate.prompt` | `lesson-animation-authoring` |
| Cover template | `series/template/sunzi/cover_template.html` | `src/utils/cover_generator.py` and any cover-generation flow |
| Cover generator runtime | `src/utils/cover_generator.py` | Render-time cover generation |
| Lesson source | `series/book_sunzibingfa/lessonXX/origin.md` | `lesson-content-planning` |

## Template closure

`series/template/sunzi/cover_template.html` is the only tracked asset under `series/template/` today. It is loaded by `src/utils/cover_generator.py` via Jinja2 and rendered with Playwright.

The animation prompt refers to `animate_template.py`, but the actual template contract is embedded in `series/prompts/sunzi_annimate.prompt`; there is no tracked standalone `animate_template.py` under `series/template/sunzi/`.

## Content contract

- Pre-render outputs: `script.json`, `wechat.md`
- Post-publish outputs: none
- Icon family: education icons

## Fallback rules

- If the education icon manifest is unavailable locally, reuse icon names already validated in existing `series/book_sunzibingfa/lesson*/script.json`
- Keep `origin.md` as the required lesson-local source of truth before content generation
