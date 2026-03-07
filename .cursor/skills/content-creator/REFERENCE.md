# Content Creator Reference

## Provenance

本 Skill 的脚本从 [yyy_monkey/creator](https://github.com/youxuanxue/yyy_monkey/tree/main/creator) 迁移。
原始上游代码保留在 `upstream/` 目录供参考。

## Script assets

| Script | Path | Role |
|---|---|---|
| CLI 入口 | `.cursor/skills/content-creator/scripts/cli.py` | 统一命令行界面，支持 `scrape` / `analyze` / `plan` / `run` |
| 抓取器 | `.cursor/skills/content-creator/scripts/scraper.py` | Playwright-based WeChat GZH 文章抓取，支持深度/列表两种模式 |
| 分析器 | `.cursor/skills/content-creator/scripts/analyzer.py` | 纯 Python 离线内容分析：主题分类、风格画像、互动统计 |
| 规划器 | `.cursor/skills/content-creator/scripts/planner.py` | LLM 辅助日更规划生成，输出 Markdown + JSON |

## Config format

`config/target.json` 结构：

```json
{
  "target": {
    "name": "账号名称",
    "positioning": "账号定位描述",
    "style_notes": "写作风格要求",
    "family": {}
  },
  "references": [
    {"name": "参考账号1"},
    {"name": "参考账号2"}
  ],
  "plan_config": {
    "duration_days": 30,
    "articles_per_day": 1,
    "spare_topics": 5,
    "start_date": "auto"
  },
  "columns": [
    {"weekday": 1, "name": "栏目名", "focus": "内容方向"}
  ]
}
```

## Output structure

```
output/
├── articles/           # 抓取的原始文章数据 (JSON)
│   ├── 目标账号.json
│   └── 参考账号.json
├── analysis_report.md  # 人类可读分析报告
├── analysis_report.json # 结构化分析数据
└── plans/
    ├── plan_YYYYMMDD_30d.md   # 选题规划 Markdown
    └── plan_YYYYMMDD_30d.json # 选题规划 JSON
```

## Authentication

微信公众号登录态持久化到 `~/.media-publisher/gzh_auth.json`，与 media-publisher 共享。

## LLM integration

规划器使用 OpenAI 兼容 API，支持 GPT-4o / DeepSeek / Qwen 等。
通过环境变量配置：`OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL`。

## Relationship to other skills

- 输出的选题规划可指导 `lesson-content-planning` 生成具体 `script.json`
- 分析报告可提供 `skill-evolver` 内容层面的反馈数据
- 抓取的竞品数据可辅助 `series-*-adapter` 优化系列定位
