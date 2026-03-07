---
name: video-core-protocol
description: 视频生产共享内核契约。定义 lesson 输入输出、分层边界、验证门禁与升级规则。
---

# Video Core Protocol

本 Skill 不直接生成视频，而是定义所有视频类 skill 的共享契约，避免每个系列重复发明流程。

配套资产清单与验证边界见 `REFERENCE.md`。

## 分层结构

1. `lesson-content-planning`：生成 `script.json`
2. `lesson-animation-authoring`：生成 `animate.py`
3. `lesson-render-publish`：渲染、状态检查、发布、内容派生
4. `series-*-adapter`：提供系列特异配置
5. `skill-evolver`：读取运行反馈，提出规则升级候选

## 共享输入

- `series`: `zsxq` / `sunzi` / `moneywise`
- `lesson`: lesson 编号，进入执行前必须先归一化
- `adapter`: 一个系列适配 skill，负责暴露目录、prompt、数据源、附加产物

## 共享中间产物

- `script.json`: 内容规划的稳定交接物
- `animate.py`: 动画编排的稳定交接物

## 共享输出

- lesson 目录
- `media/videos/animate/1920p60/LessonXXXVerticalScenes.mp4`
- 发布结果 / Video ID
- 供 `lesson-content-planning` 消费的发布元数据

## 职责边界

### Core 负责

- lesson 编号规范化
- 目录与类名约定
- 状态检查项
- render / publish 脚本入口
- 跨系列共性失败经验

### Adapter 负责

- 系列目录
- lesson 编号位数
- script / animate prompt
- 数据源
- 特殊产物和例外规则

## 变更升级规则

- 只影响单系列：先改 adapter
- 跨 2 个及以上系列重复出现：再晋升到 core
- 没有复现样本：不写入 core

## 最小验证门禁

每次修改共享规则时，至少完成：

1. `python3 .cursor/skills/video-core-protocol/scripts/check_protocol.py`
2. 相关单测
3. 一个 lesson 的 smoke render，或等价的脚本级验证

## 当前共享脚本

- `.cursor/skills/video-core-protocol/scripts/create_lesson.py`
- `.cursor/skills/video-core-protocol/scripts/workflow.py`
- `.cursor/skills/video-core-protocol/scripts/lesson_num.py`

所有顶层 orchestrator 都应调用这些共享脚本，而不是在各自 skill 内复制实现。
