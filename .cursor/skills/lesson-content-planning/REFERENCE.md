# Lesson Content Planning Reference

## Prompt asset map

| Series | Prompt asset (in adapter skill dir) | Primary source | Content outputs | Local fallback when external assets are absent |
|---|---|---|---|---|
| `zsxq` | `.cursor/skills/series-zsxq-adapter/prompts/zsxq_100ke_script.prompt` | `assets/zsxq/jingpin_100ke_posts.json` | `script.json`, `wechat.md` | Reuse icon names and field patterns from nearby `series/book_zsxq_100ke/lesson*/script.json` |
| `sunzi` | `.cursor/skills/series-sunzi-adapter/prompts/sunzi_script.prompt` | `series/book_sunzibingfa/lessonXX/origin.md` | `script.json`, `wechat.md` | Reuse icon names and field patterns from nearby `series/book_sunzibingfa/lesson*/script.json` |
| `moneywise` | `.cursor/skills/series-moneywise-adapter/prompts/moneywise_script.prompt` | `assets/zsxq/jingpin_100ke_posts.json` | `script.json` | Reuse valid `blog.category`, `blog.tags`, and icon naming families from existing `series/moneywise_global/lesson*/script.json` |

## Post-publish content pass

`lesson-content-planning` runs a second pass for MoneyWise after publish:

- Inputs: `script.json`, `videoId`, published duration, and `MONEYWISE_SITE_DIR` when available
- Output: website MDX

There is currently no separate post-publish prompt file; the series adapter and this reference define the contract.

## Audit entrypoint

Use `.cursor/skills/lesson-content-planning/scripts/audit_content.py` to inspect generated lesson outputs for:

- missing required files or top-level schema blocks
- stale MoneyWise year references
- risky hype/AI-ish phrasing signals
- icon-count and icon-format drift
- Sunzi title emoji and interactive-scene contract issues

## Schema anchors from prompt assets

| Series | Required content blocks |
|---|---|
| `zsxq` | `meta`, `wechat`, `youtube`, `icons`, `scenes` |
| `sunzi` | `meta`, `wechat`, `youtube`, `icons`, `scenes`, interactive question in Scene 6 |
| `moneywise` | `meta`, `seo`, `social`, `youtube`, `blog`, `icons`, `scenes` |

## External asset note

Each adapter skill directory contains the icon list file for its series (e.g. `.cursor/skills/series-sunzi-adapter/icons_education.txt`). These icon manifests may not be present in every workspace — when unavailable, use same-series validated `script.json` examples as the local fallback source of truth and must not invent icon names.
