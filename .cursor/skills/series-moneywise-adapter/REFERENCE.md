# Series Adapter Reference: MoneyWise

## Series-owned assets

| Asset type | Path | Used by |
|---|---|---|
| Script prompt | `.cursor/skills/series-moneywise-adapter/prompts/moneywise_script.prompt` | `lesson-content-planning` |
| Animation prompt | `.cursor/skills/series-moneywise-adapter/prompts/moneywise_annimate.prompt` | `lesson-animation-authoring` |
| Icon list | `.cursor/skills/series-moneywise-adapter/icons_finance.txt` | `lesson_vertical.py` icon lookup; fallback to `assets/icons8/` |
| Source content | `assets/zsxq/jingpin_100ke_posts.json` | `lesson-content-planning` |

## Content contract

- Pre-render outputs: `script.json`
- Post-publish outputs: website MDX
- Runtime env for site integration: `MONEYWISE_SITE_DIR`

## Taxonomy closure

Primary source of truth when available:

- `$MONEYWISE_SITE_DIR/src/config/taxonomy.ts`

Repo-local fallback when the site repo is unavailable:

- Keep `blog.category` and `blog.tags` within the families already validated in `series/moneywise_global/lesson*/script.json`
- Observed local categories:
  - `Debt Management`
  - `Economic Fundamentals`
  - `Investing`
  - `Personal Finance`

Selected observed local tags include:

- `banking`
- `credit score`
- `debt payoff`
- `fiat currency`
- `financial planning`
- `gold`
- `inflation`
- `interest rates`
- `investing basics`
- `investing strategy`
- `market crash`
- `monetary policy`
- `money management`
- `passive income`
- `real estate`
- `scams`
- `stocks`

## Fallback rules

- If the finance icon manifest is unavailable locally, reuse icon names already validated in existing `series/moneywise_global/lesson*/script.json`
- If `MONEYWISE_SITE_DIR` is unavailable, do not invent category/tag families outside the local validated set above
