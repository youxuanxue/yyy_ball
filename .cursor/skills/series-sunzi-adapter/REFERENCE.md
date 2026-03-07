# Series Adapter Reference: Sunzi

## Series-owned assets

| Asset type | Path | Used by |
|---|---|---|
| Script prompt | `.cursor/skills/series-sunzi-adapter/prompts/sunzi_script.prompt` | `lesson-content-planning` |
| Animation prompt | `.cursor/skills/series-sunzi-adapter/prompts/sunzi_annimate.prompt` | `lesson-animation-authoring` |
| Icon list | `.cursor/skills/series-sunzi-adapter/icons_education.txt` | `lesson_vertical.py` icon lookup; fallback to `assets/icons8/` |
| Cover template | `.cursor/skills/series-sunzi-adapter/templates/cover_template.html` | `src/utils/cover_generator.py` via Jinja2 + Playwright |
| Lesson source | `series/book_sunzibingfa/lessonXX/origin.md` | `lesson-content-planning` |

## Template closure

`cover_template.html` is loaded by `src/utils/cover_generator.py` via Jinja2 `FileSystemLoader` and rendered to PNG with Playwright. The base class `SunziLessonVertical` resolves this template via its `cover_template_dir` class attribute.

The animation prompt contains the full animate.py code template as an embedded code block; there is no separate standalone `animate_template.py`.

## Content contract

- Pre-render outputs: `script.json`, `wechat.md`
- Post-publish outputs: none
- Icon family: education icons

## Fallback rules

- If the education icon manifest is unavailable locally, reuse icon names already validated in existing `series/book_sunzibingfa/lesson*/script.json`
- Keep `origin.md` as the required lesson-local source of truth before content generation
