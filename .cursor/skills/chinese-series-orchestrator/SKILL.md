---
name: chinese-series-orchestrator
description: 中文系列总编排器，负责串起 zsxq 与 sunzi 的完整生产流程。
---

# Chinese Series Orchestrator

本 Skill 是中文系列的顶层总编排器，覆盖：

- 日日生金（`zsxq`）
- 孙子兵法（`sunzi`）

它不承载共享实现，只负责按顺序调用分层 skill。

完整资产路由表见 `REFERENCE.md`。

## 调用顺序

1. 读取 `video-core-protocol`
2. 选择系列 adapter：
   - 日日生金：`series-zsxq-adapter`
   - 孙子兵法：`series-sunzi-adapter`
3. 调用 `lesson-content-planning`
   - 生成 `script.json`
   - 生成 `wechat.md`
4. 调用 `lesson-animation-authoring`
   - 生成 `animate.py`
5. 调用 `lesson-render-publish`
   - 使用 core workflow 做 `status` / `render` / `publish`
6. 如有失败或反复返工，调用 `skill-evolver`

## 共享脚本入口

```bash
# 创建 lesson 目录
uv run python .cursor/skills/video-core-protocol/scripts/create_lesson.py --series zsxq 002
uv run python .cursor/skills/video-core-protocol/scripts/create_lesson.py --series sunzi 07

# 检查状态
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series zsxq status 002
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series sunzi status 06

# 渲染
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series zsxq render 002
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series sunzi render 06 --quality ql

# 发布
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series zsxq --media-publisher-dir "$MEDIA_PUBLISHER_DIR" publish 002
uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series sunzi --media-publisher-dir "$MEDIA_PUBLISHER_DIR" publish 06
```

## 约束

- 共享规则改动写入 `video-core-protocol`
- 系列差异只写入 adapter
- `wechat.md` 等内容产物统一由 `lesson-content-planning` 生成
