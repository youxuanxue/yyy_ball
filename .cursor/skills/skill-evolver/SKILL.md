---
name: skill-evolver
description: 收集 lesson 运行反馈，生成 adapter/core 改进候选，并给出升级建议。
---

# Skill Evolver

本 Skill 不直接生成 lesson，而是把历史运行经验沉淀成可审查的改进候选。

## 目标

- 让 skill 体系从“写死 SOP”变成“可吸收反馈的工作流”
- 避免单个 lesson 的偶发问题直接污染 core
- 让 adapter 与 core 有清晰的晋升关系

## 输入

每条 observation 至少包含：

- `series`
- `lesson`
- `stage`：如 `planning` / `animation` / `render` / `publish`
- `status`：`passed` / `failed`
- `failure_type`
- `affects`：`adapter` / `core` / `unknown`
- `summary`

可选补充：

- `files`
- `commands`
- `notes`
- `skill_version`

## 决策规则

- 单系列问题：建议改对应 adapter
- 多系列同类失败：建议晋升为 core 候选
- 证据不足：保留为 observation，不升级

## 推荐命令

```bash
# 记录一次反馈
uv run python .cursor/skills/skill-evolver/scripts/evolve.py record \
  --series zsxq \
  --lesson 002 \
  --stage render \
  --status failed \
  --failure-type icon-missing \
  --affects adapter \
  --summary "icon name not found in finance icon list"

# 汇总历史反馈，生成升级建议
uv run python .cursor/skills/skill-evolver/scripts/evolve.py summarize
```

## 输出

- observation JSON 文件
- 汇总后的 Markdown 建议书
- 对 core / adapter / orchestrator 的候选改动建议

## 执行原则

- evolver 先提案，人工审阅后再真正改 skill
- 如果某条经验没有通过回归验证，不要晋升到 core
