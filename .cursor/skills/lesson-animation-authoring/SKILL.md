---
name: lesson-animation-authoring
description: 根据 script.json 和系列 prompt 生成 animate.py，渲染视频并验证产物完整性。
---

# Lesson Animation Authoring

本 Skill 负责把 `script.json` 转成可渲染的 `animate.py`，随后渲染并验证产物。

具体 animate prompt 资产、runtime 源码依赖和验证流程见 `REFERENCE.md`。

## 何时使用

- `script.json` 已存在，需要生成或修复 `animate.py`
- 需要渲染视频并验证产物完整性
- 某个 lesson 渲染失败，需要回调动画实现

## 必要输入

1. `video-core-protocol`
2. 对应 `series-*-adapter`
3. lesson 目录下的 `script.json`
4. adapter 指定的 animate prompt

## 执行步骤

### A. 生成 animate.py

1. 读取 `script.json`，确保场景顺序、图标名和口播结构清晰。
2. 读取 adapter 指定的 animate prompt。
3. 生成 `animate.py`，使用约定类名 `LessonNNNVerticalScenes`。
4. 检查是否满足共享约束：
   - 输出为 9:16 竖屏场景
   - 不引入与单 lesson 强绑定的硬编码绝对路径
   - 避免已知高风险动画模式

### B. 渲染与验证

5. 使用 workflow CLI 检查状态、渲染视频：
   - 检查状态：`uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series <series> status <lesson>`
   - 渲染视频：`uv run python .cursor/skills/video-core-protocol/scripts/workflow.py --series <series> render <lesson>`
6. 验证渲染产物：
   - lesson 目录存在
   - `script.json` 存在
   - `animate.py` 存在
   - 渲染成功并产出 MP4

## 已知约束

- 渲染入口统一走 `.cursor/skills/video-core-protocol/scripts/workflow.py`
- 若只在一个系列触发的动画例外，优先写入 adapter 而不是 core
- 本 Skill 不负责发布；发布由 orchestrator 直接调用 `workflow.py publish`
- 本 Skill 不负责生成 `wechat.md` / website MDX

## 失败归因

- 脚本缺字段：回 `lesson-content-planning`
- `animate.py` 语法或动画问题：在本 Skill 内修复
- 路径、类名、状态检查规则问题：回 `video-core-protocol`
- 内容派生产物不符合预期：回 `lesson-content-planning`
- 系列定制规则不符合预期：回对应 adapter

## 反馈回流

- 场景节奏与结构问题：回到 `lesson-content-planning`
- Manim 通用失败模式：升级到 `video-core-protocol`
- 系列独有布局问题：回到对应 adapter
