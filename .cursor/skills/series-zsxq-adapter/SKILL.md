---
name: series-zsxq-adapter
description: 日日生金系列适配层，提供目录、编号、prompt、数据源和系列特异规则。
---

# Series Adapter: ZSXQ

配套 prompt 资产和 fallback 规则见 `REFERENCE.md`。

## 系列配置

- `series`: `zsxq`
- 目录：`series/book_zsxq_100ke`
- lesson 编号：3 位数，如 `002`
- script prompt：`series/prompts/zsxq_100ke_script.prompt`
- animate prompt：`series/prompts/zsxq_100ke_annimate.prompt`
- 数据源：`assets/zsxq/jingpin_100ke_posts.json`
- 数据刷新脚本：`.cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py`

## 特异规则

- 需要从帖子数据中筛出 `第XXX课`
- `lesson-content-planning` 会额外生成 `wechat.md`
- 图标使用财经类素材列表
- 如需刷新帖子源数据，优先通过 adapter 自带脚本执行，而不是回到 `src/crawlers/` 寻找旧入口

## 与其他 skill 的关系

- 内容规划交给 `lesson-content-planning`
- 动画生成交给 `lesson-animation-authoring`
- 渲染/发布交给 `lesson-render-publish`
- 本 Skill 只承载系列差异，不复制通用流程

## 系列自带脚本

- 刷新 `assets/zsxq/jingpin_100ke_posts.json`：
  `uv run python .cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py`
- 去重已有数据：
  `uv run python .cursor/skills/series-zsxq-adapter/scripts/crawler_zsxq_100.py --dedupe`
