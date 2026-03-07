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
- script prompt：`prompts/zsxq_100ke_script.prompt`（本 skill 目录下）
- animate prompt：`prompts/zsxq_100ke_annimate.prompt`（本 skill 目录下）
- 数据源：`assets/zsxq/jingpin_100ke_posts.json`

## 特异规则

- 需要从帖子数据中筛出 `第XXX课`
- `lesson-content-planning` 会额外生成 `wechat.md`
- 图标使用财经类素材列表

## 与其他 skill 的关系

- 内容规划交给 `lesson-content-planning`
- 动画生成与渲染交给 `lesson-animation-authoring`
- 发布由 orchestrator 直接调用 `workflow.py publish`
- 本 Skill 只承载系列差异，不复制通用流程
