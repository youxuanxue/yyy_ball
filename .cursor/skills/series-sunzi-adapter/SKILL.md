---
name: series-sunzi-adapter
description: 孙子兵法系列适配层，提供目录、编号、prompt、origin.md 规则和系列特异约束。
---

# Series Adapter: Sunzi

配套 prompt / template 资产和 cover 模板闭环见 `REFERENCE.md`。

## 系列配置

- `series`: `sunzi`
- 目录：`series/book_sunzibingfa`
- lesson 编号：2 位数，如 `06`
- script prompt：`series/prompts/sunzi_script.prompt`
- animate prompt：`series/prompts/sunzi_annimate.prompt`
- 数据源：lesson 目录下的 `origin.md`

## 特异规则

- lesson 在生成 `script.json` 前必须先有 `origin.md`
- `lesson-content-planning` 会额外生成 `wechat.md`
- 图标使用教育类素材列表

## 与其他 skill 的关系

- 先由本 Skill 提供 `origin.md` / prompt / lesson 位数等约束
- 再由 `lesson-content-planning`、`lesson-animation-authoring`、`lesson-render-publish` 执行通用链路
