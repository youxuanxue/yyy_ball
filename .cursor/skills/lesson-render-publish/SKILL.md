---
name: lesson-render-publish
description: 负责渲染、状态检查与发布，是视频生产链路的执行与校验层。
---

# Lesson Render Publish

本 Skill 聚焦“让产物真正跑起来”，只负责状态检查、渲染和发布。

具体 runtime 源码依赖与资源链见 `REFERENCE.md`。

## 何时使用

- lesson 已具备 `script.json` 和 `animate.py`
- 需要渲染视频、检查状态、发布到平台

## 统一脚本入口

- 创建 lesson：`uv run python .cursor/skills/video-core-protocol/scripts/create_lesson.py --series <series> <lesson>`
- 检查状态：`uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series <series> status <lesson>`
- 渲染视频：`uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series <series> render <lesson>`
- 发布视频：`uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series <series> publish <lesson>`

## 验证顺序

1. lesson 目录存在
2. `script.json` 存在
3. `animate.py` 存在
4. 渲染成功并产出 MP4
5. 再做发布或内容派生

## 失败归因

- 脚本缺字段：回 `lesson-content-planning`
- `animate.py` 语法或动画问题：回 `lesson-animation-authoring`
- 路径、类名、状态检查规则问题：回 `video-core-protocol`
- 内容派生产物不符合预期：回 `lesson-content-planning`
- 系列定制规则不符合预期：回对应 adapter

## 演进原则

本 Skill 不应该复制系列细节，也不负责生成 `wechat.md` / website MDX。
