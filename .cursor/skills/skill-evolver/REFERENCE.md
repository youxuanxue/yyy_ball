# Skill Evolver Reference

## Owned assets

| Asset | Path | Role |
|---|---|---|
| Evolver CLI | `.cursor/skills/skill-evolver/scripts/evolve.py` | Records lesson observations and summarizes cross-series recommendations |
| Observation storage root | `.cursor/skills/skill-evolver/data/observations/` | JSON observation snapshots created by `record` |
| Report output root | `.cursor/skills/skill-evolver/reports/` | Markdown recommendation output created by `summarize` |

## Contract

- Input unit: one lesson observation with `series`, `lesson`, `stage`, `status`, `failure_type`, `affects`, and `summary`
- Output unit: grouped recommendation report with adapter/core targeting guidance
- Promotion rule: single-series issues stay in adapters first; repeated cross-series failures escalate toward core

## Relationship to other skills

- Consumes evidence from real lesson runs orchestrated by `chinese-series-orchestrator` and `moneywise-series-orchestrator`
- Feeds back into `video-core-protocol`, adapters, and content/animation layers as reviewable recommendations
