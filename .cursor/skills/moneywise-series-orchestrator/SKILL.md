---
name: moneywise-series-orchestrator
description: MoneyWise Global 总编排器，负责串起英文 lesson 的完整生产流程。
---

# MoneyWise Series Orchestrator

本 Skill 是 MoneyWise 的顶层总编排器。

它不承载共享实现，只负责按顺序调用分层 skill。

完整资产路由表见 `REFERENCE.md`。

## 调用顺序

1. 读取 `video-core-protocol`
2. 读取 `series-moneywise-adapter`
3. 第一次调用 `lesson-content-planning`
   - 生成 `script.json`
4. 调用 `lesson-animation-authoring`
   - 生成 `animate.py`
   - 渲染视频并验证产物
5. 发布视频（直接调用 workflow CLI）：
   - `uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series moneywise publish <lesson>`
6. 第二次调用 `lesson-content-planning`
   - 在拿到 `videoId`、时长等发布元数据后生成 website MDX
7. 如有失败或反复返工，调用 `skill-evolver`

## 共享脚本入口

```bash
# 创建 lesson 目录
uv run python .cursor/skills/video-core-protocol/scripts/create_lesson.py --series moneywise 021

# 检查状态
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series moneywise status 021

# 渲染
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series moneywise render 021 --quality qh

# 发布
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py \
  --series moneywise \
  --media-publisher-dir "$MEDIA_PUBLISHER_DIR" \
  publish 021 \
  --platform youtube \
  --privacy private
```

## 约束

- website MDX 也是内容产物，归 `lesson-content-planning`
- 共享规则改动写入 `video-core-protocol`
- MoneyWise 的系列差异只写入 `series-moneywise-adapter`
