---
name: lesson-content-planning
description: 负责 script.json 与系列内容派生物的生成，是视频链路的内容规划层。
---

# Lesson Content Planning

本 Skill 专门负责所有内容类产物，既包括前置的 `script.json`，也包括系列内容派生物。

具体 prompt 资产、fallback 规则和 post-publish 内容闭环见 `REFERENCE.md`。

## 何时使用

- 创建新 lesson
- 补生成缺失的 `script.json`
- 生成 `wechat.md`
- 生成 MoneyWise website MDX
- 需要基于运行反馈回改脚本结构或文案节奏

## 必要输入

1. `video-core-protocol`
2. 对应 `series-*-adapter`
3. 该 lesson 的原始数据源
4. adapter 指定的 script prompt
5. 若生成 post-publish 内容，还需要发布元数据（如 `videoId`、时长）

## 执行步骤

1. 读取 adapter，确认 lesson 目录、编号位数、数据源和 prompt。
2. 读取原始内容：
   - `zsxq` / `moneywise`：`assets/zsxq/jingpin_100ke_posts.json`
   - `sunzi`：`series/book_sunzibingfa/lessonXX/origin.md`
3. 生成前置内容产物：
   - 所有系列：`script.json`
   - 中文系列：`wechat.md`
4. 如果已经有发布元数据，再生成后置内容产物：
   - MoneyWise：website MDX
5. 检查字段是否完整、命名是否稳定、场景顺序是否可被下游 `animate.py` 消费。

## 运行模式

- **Pre-render pass**：生成 `script.json` 和系列前置内容产物
- **Post-publish pass**：在视频发布后补生成依赖发布元数据的内容产物

## 输出要求

- `script.json` 必须保存到对应 lesson 目录。
- 中文系列的 `wechat.md` 也由本 Skill 生成。
- MoneyWise 的 website MDX 也由本 Skill 生成，但需要发布后的 `videoId`、时长等元数据。
- 字段名应稳定；不要为单个 lesson 临时改 schema。
- 若某条规则只适合一个系列，写入 adapter，而不是 core。

## 反馈回流

当渲染失败或人工验收发现问题时：

- 文案/结构问题：优先回改本 Skill 或对应 adapter
- 动画实现问题：交给 `lesson-animation-authoring`
- 共性 schema 问题：升级到 `video-core-protocol`

## 自检入口

可使用 `.cursor/skills/lesson-content-planning/scripts/audit_content.py` 对真实 lesson 输出做结构与内容审计。
