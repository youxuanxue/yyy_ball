---
name: lesson-animation-authoring
description: 根据 script.json 和系列 prompt 生成 animate.py，并遵守共享动画约束。
---

# Lesson Animation Authoring

本 Skill 负责把 `script.json` 转成可渲染的 `animate.py`。

具体 animate prompt 资产和模板来源说明见 `REFERENCE.md`。

## 何时使用

- `script.json` 已存在，需要生成或修复 `animate.py`
- 某个 lesson 渲染失败，需要回调动画实现

## 必要输入

1. `video-core-protocol`
2. 对应 `series-*-adapter`
3. lesson 目录下的 `script.json`
4. adapter 指定的 animate prompt

## 执行步骤

1. 读取 `script.json`，确保场景顺序、图标名和口播结构清晰。
2. 读取 adapter 指定的 animate prompt。
3. 生成 `animate.py`，使用约定类名 `LessonNNNVerticalScenes`。
4. 检查是否满足共享约束：
   - 输出为 9:16 竖屏场景
   - 不引入与单 lesson 强绑定的硬编码绝对路径
   - 避免已知高风险动画模式

## 已知约束

- 渲染入口统一走 `.cursor/skills/video-core-protocol/scripts/workflow.py`
- 若只在一个系列触发的动画例外，优先写入 adapter 而不是 core

## 反馈回流

- 场景节奏与结构问题：回到 `lesson-content-planning`
- Manim 通用失败模式：升级到 `video-core-protocol`
- 系列独有布局问题：回到对应 adapter
