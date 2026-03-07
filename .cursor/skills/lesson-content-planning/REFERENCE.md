# Lesson Content Planning Reference

## Prompt asset map

| Series | Prompt asset | Primary source | Content outputs | Local fallback when external assets are absent |
|---|---|---|---|---|
| `zsxq` | `series/prompts/zsxq_100ke_script.prompt` | `assets/zsxq/jingpin_100ke_posts.json` | `script.json`, `wechat.md` | Reuse icon names and field patterns from nearby `series/book_zsxq_100ke/lesson*/script.json` |
| `sunzi` | `series/prompts/sunzi_script.prompt` | `series/book_sunzibingfa/lessonXX/origin.md` | `script.json`, `wechat.md` | Reuse icon names and field patterns from nearby `series/book_sunzibingfa/lesson*/script.json` |
| `moneywise` | `series/prompts/moneywise_script.prompt` | `assets/zsxq/jingpin_100ke_posts.json` | `script.json` | Reuse valid `blog.category`, `blog.tags`, and icon naming families from existing `series/moneywise_global/lesson*/script.json` |

## Post-publish content pass

`lesson-content-planning` runs a second pass for MoneyWise after publish:

- Inputs: `script.json`, `videoId`, published duration, and `MONEYWISE_SITE_DIR` when available
- Output: website MDX

There is currently **no separate post-publish prompt file** in `series/prompts/`; the series adapter and this reference define the contract.

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

The prompt files mention `assets/icons8/*.txt`, but those icon manifests are not tracked in git. When they are unavailable in the workspace, this skill should use same-series validated `script.json` examples as the local fallback source of truth and must not invent icon names.
