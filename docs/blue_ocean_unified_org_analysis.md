# 统一组织治理模型下的架构重审

> 前文（`blue_ocean_migration_analysis.md`）结论为"不建议合并"。本文从一个新的视角重新审视：**如果 yyy_ball 的视频生产也采用「1 CEO + N Agent + 飞书」的组织治理模型**，共享基础设施的面积是否足以逆转之前的结论？

---

## 一、问题重构

之前的分析将 blue_ocean 定位为"市场情报系统"，将 yyy_ball 定位为"视频生产流水线"，认为两者领域正交。

但如果换一个视角：blue_ocean 不只是一个市场情报工具，它更是一个**组织治理运行时**——一套让 AI Agent 在人类 CEO 监督下自主决策和执行的通用框架。而"市场情报 → 公众号文章"只是跑在这个框架上的**第一个场景**。

关键问题变成了：**视频生产能否成为跑在同一框架上的第二个场景？**

---

## 二、Blue Ocean org/ 的架构解剖

### 2.1 分层拆解

对 blue_ocean 的 org/ 模块逐文件审计后，可以清晰地分出三层：

```
┌─────────────────────────────────────────────────────────────┐
│  场景层 (Domain-specific)                                    │
│  scenario_article.py    — 公众号文章生产场景                    │
│  article_prompt_builder.py — 文章 prompt 构建器                │
│  tone_guard.py          — AI味检测/改写（文本内容专用）          │
│  *.md                   — 场景相关设计文档                     │
├─────────────────────────────────────────────────────────────┤
│  治理层 (Domain-agnostic — 可复用)                            │
│  governance.py          — Policy/Risk 裁决引擎                │
│  schema_guard.py        — 动作包 Schema 校验                  │
│  runtime_store.py       — 动作快照 + 状态迁移 JSONL 存储        │
│  feishu_app.py          — 飞书卡片构建 + 回调签名               │
│  feishu_client.py       — 飞书 API 客户端（token/发消息）       │
│  feishu_dispatch.py     — 推送调度                            │
│  feishu_callback_server.py — HTTP 回调网关                    │
│  feishu_longconn.py     — 飞书长连接客户端                     │
├─────────────────────────────────────────────────────────────┤
│  通用层 (Infrastructure)                                     │
│  common/llm.py          — OpenAI 兼容 LLM 调用               │
│  common/store.py        — JSONL 事件存储                     │
│  common/notify.py       — Webhook 通知                      │
│  common/fetcher.py      — HTTP 抓取（市场情报专用）             │
│  common/dashboard.py    — 决策看板（市场情报专用）               │
│  config.py              — 配置中心                           │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 可复用部分的代码量统计

| 层 | 文件数 | 约行数 | 领域耦合度 |
|----|--------|--------|-----------|
| 治理层 | 8 个 .py | ~900 行 | **低** — governance/schema_guard 有少量硬编码规则（如 `skill_content_strategy`），但容易参数化 |
| 通用层（可复用部分） | llm.py + store.py + notify.py | ~250 行 | **零** — 纯基础设施 |
| 场景层 | 2 个 .py + tone_guard.py | ~600 行 | **高** — 完全绑定公众号文章场景 |
| 通用层（领域专用） | fetcher.py + dashboard.py | ~350 行 | **高** — 绑定市场情报采集 |

**结论：约 1150 行代码（治理层 + 通用可复用层）是领域无关的，可以服务于任何「CEO + Agent + 飞书」场景。**

### 2.3 治理层中需要参数化的硬编码

| 文件 | 硬编码 | 改造方式 |
|------|--------|----------|
| `governance.py` | `evaluate_policy` 中检查 `"scam"/"fraud"` 关键词 | 改为可配置的 policy_rules 列表 |
| `governance.py` | `budget > 20_000` 阈值 | 改为配置项 |
| `schema_guard.py` | `owner_agent == "skill_content_strategy"` 时要求 AI tone 证据 | 改为按场景注册的验证规则 |
| `feishu_app.py` | `build_action_card` 中的按钮标签（"批准/驳回/升级/重试"） | 保持不变，这是通用的 |
| `feishu_dispatch.py` | `push_article_for_review` 推送文章终稿 | 这是场景层，不在可复用范围内 |

**改造量很小**，主要是把 3-5 处硬编码改为配置注入。

---

## 三、视频生产的治理场景设计

### 3.1 视频生产的动作包（Action Package）

```json
{
  "schema_version": "v1.1",
  "action_id": "vid_20260307_c3d4",
  "source_signals": ["content_trending", "series_gap", "audience_request"],
  "priority": "P2",
  "authority_level": "L1",
  "title": "制作第41课：理财中的沉没成本谬误",
  "objective": {
    "north_star": "完成一个高质量60-180秒竖屏教育视频",
    "metrics": [
      {"name": "render_success", "target_delta": 1.0},
      {"name": "voice_clarity", "target_delta": 0.85}
    ]
  },
  "constraints": {
    "budget_cap": 500,
    "risk_limit": "low",
    "deadline": "2026-03-14T00:00:00Z"
  },
  "execution": {
    "owner_agent": "skill_lesson_content_planning",
    "collaborators": [
      "skill_lesson_animation_authoring",
      "skill_voice_synthesis",
      "skill_cover_generation"
    ],
    "sla_hours": 24
  },
  "approval": {"required": false, "approver_role": "auto"},
  "validation": {
    "acceptance_criteria": [
      "视频时长 60-180 秒",
      "渲染输出 1080x1920 MP4 无报错",
      "语音文件完整覆盖所有场景"
    ],
    "kill_criteria": [
      "script.json 内容涉及政治/宗教敏感话题",
      "渲染失败超过 3 次",
      "系列课程编号冲突"
    ]
  },
  "status": "proposed"
}
```

这个 action package 与 blue_ocean 的公众号文章 action package **使用完全相同的 schema**。governance 裁决、CEO 审批、状态迁移、证据追溯——全部可以复用。

### 3.2 视频生产的场景流程

```
┌──────────────────────────────────────────────────────────────┐
│  scenario_video.py（新建，类比 scenario_article.py）           │
│                                                              │
│  Node1: 信号聚合                                              │
│    ├─ 读取 content-creator 的选题建议                          │
│    ├─ 检查系列课程缺口（哪些课还没做）                           │
│    └─ 构建 action package                                    │
│                                                              │
│  Node2: 治理裁决  ← governance.py (复用)                      │
│    ├─ Policy: 内容敏感度检查                                   │
│    ├─ Risk: 课程编号冲突/系列完整性                              │
│    └─ 如果 P1 → CEO 审批 via 飞书 (复用)                       │
│                                                              │
│  Node3: 执行                                                 │
│    ├─ 生成 script.json (lesson-content-planning skill)        │
│    ├─ 生成 animate.py (lesson-animation-authoring skill)      │
│    ├─ 渲染视频 (Manim)                                        │
│    └─ 记录证据                                                │
│                                                              │
│  Node4: 质量门禁                                              │
│    ├─ 渲染产物完整性检查                                       │
│    ├─ 语音覆盖率检查                                           │
│    └─ （可选）脚本 AI 味检测                                   │
│                                                              │
│  Node5: 回写                                                 │
│    ├─ 更新 action status                                     │
│    ├─ 飞书通知 CEO 结果                                       │
│    └─ （可选）自动发布到 YouTube/微信                           │
└──────────────────────────────────────────────────────────────┘
```

### 3.3 视频场景复用了什么、新建了什么

| 组件 | 复用/新建 | 说明 |
|------|-----------|------|
| governance.py | **复用** | Policy/Risk 裁决，规则参数化 |
| schema_guard.py | **复用** | action package 校验 |
| runtime_store.py | **复用** | 动作快照 + 状态迁移 |
| feishu_client.py | **复用** | 飞书 API |
| feishu_app.py | **复用** | 卡片构建 + 回调 |
| feishu_dispatch.py | **部分复用** | push_action_to_feishu 可复用，push_article_for_review 是文章专用 |
| feishu_callback_server.py | **复用** | 回调网关 |
| common/llm.py | **复用** | LLM 调用 |
| common/store.py | **复用** | 事件存储 |
| common/notify.py | **复用** | 通知 |
| scenario_video.py | **新建** | 视频场景运行时 |
| video_quality_gate.py | **新建** | 视频渲染质量门禁 |
| scenario_article.py | 不变 | 公众号文章场景继续独立运行 |
| tone_guard.py | 不变 | 文章专用，视频场景不需要 |
| monitors/ | 不变 | 市场情报采集，与视频场景无直接关联 |

---

## 四、架构方案

### 4.1 方案 E：提取 org-runtime 为共享包（推荐）

```
youxuanxue/
├── yyy-org-runtime/           # 新仓库：组织治理运行时框架
│   ├── org_runtime/
│   │   ├── governance.py      # Policy/Risk 裁决（参数化）
│   │   ├── schema_guard.py    # Action Package 校验（可扩展验证规则）
│   │   ├── runtime_store.py   # 动作快照 + 状态迁移
│   │   ├── feishu/
│   │   │   ├── client.py      # 飞书 API
│   │   │   ├── app.py         # 卡片构建 + 回调
│   │   │   ├── dispatch.py    # 推送调度
│   │   │   ├── callback_server.py
│   │   │   └── longconn.py
│   │   ├── llm.py             # LLM 调用
│   │   ├── store.py           # JSONL 事件存储
│   │   └── notify.py          # Webhook 通知
│   └── pyproject.toml
│
├── yyy-oversea/
│   └── blue_ocean/
│       ├── monitors/          # 市场情报采集（不变）
│       ├── scenarios/
│       │   └── article.py     # 公众号文章场景（调用 org_runtime）
│       ├── common/
│       │   ├── fetcher.py     # HTTP 抓取（市场情报专用）
│       │   └── dashboard.py   # 决策看板（市场情报专用）
│       └── ...
│
├── yyy_ball/
│   ├── src/animate/           # 视频引擎（不变）
│   ├── src/utils/             # 语音/封面（不变）
│   ├── series/                # 内容层（不变）
│   ├── scenarios/
│   │   └── video.py           # 视频生产场景（新建，调用 org_runtime）
│   └── ...
```

**优点**：
- 各仓库保持领域内聚
- 共享基础设施通过包依赖引入，无代码重复
- org-runtime 可以独立演进（新增场景类型不影响消费方）
- 版本管理清晰：org-runtime 发版，两个消费方各自升级

**缺点**：
- 新增一个仓库要维护
- 早期开发三个仓库联调可能麻烦（可用 uv workspace 的 path dependency 缓解）

### 4.2 方案 F：合并到 yyy_ball，org 作为独立包

```
yyy_ball/
├── src/animate/               # 视频引擎（不变）
├── src/utils/                 # 语音/封面（不变）
├── series/                    # 内容层（不变）
├── org_runtime/               # 治理框架（从 blue_ocean 提取）
│   ├── governance.py
│   ├── schema_guard.py
│   ├── runtime_store.py
│   ├── feishu/
│   ├── llm.py
│   ├── store.py
│   └── notify.py
├── scenarios/
│   ├── video.py               # 视频生产场景
│   └── article.py             # 公众号文章场景（从 blue_ocean 迁入）
├── monitors/                  # 市场情报采集（从 blue_ocean 迁入）
│   ├── skill_highlights.py
│   ├── new_term.py
│   └── ...
├── pyproject.toml             # 合并依赖
```

**优点**：
- 单仓库，开发者体验简单
- 两个场景共享同一个 org_runtime，无版本同步问题
- 如果团队规模小（1-3 人），维护成本低

**缺点**：
- yyy_ball 变成"大杂烩"，定位从"视频工具"变成"CEO 运营平台"
- 依赖膨胀问题仍然存在（curl_cffi/feedparser 等被所有人安装）
- 仓库名 yyy_ball 不再准确，需要重命名

### 4.3 方案 G：合并但用 uv workspace 隔离

```
yyy_ball/  (或改名 yyy_platform)
├── pyproject.toml             # workspace 根 — 仅声明 members
├── video/                     # 视频生产包
│   ├── src/animate/
│   ├── src/utils/
│   ├── series/
│   ├── scenarios/video.py
│   └── pyproject.toml         # 视频专有依赖（Manim, torch, etc.）
├── org_runtime/               # 治理框架包
│   ├── governance.py
│   ├── feishu/
│   └── pyproject.toml         # 治理依赖（lark-oapi, openai）
├── blue_ocean/                # 市场情报包
│   ├── monitors/
│   ├── scenarios/article.py
│   └── pyproject.toml         # 情报依赖（curl_cffi, feedparser）
```

**优点**：
- uv workspace 提供依赖隔离
- 单仓库，但逻辑边界清晰
- `uv run --package video ...` 不会安装 blue_ocean 的依赖

**缺点**：
- 需要重构现有目录结构（大量路径修改）
- yyy_ball 的 `.cursor/skills/` 路径引用需要全部更新
- 初始改造工作量大

---

## 五、治理层需要的改造清单

无论选择哪个方案，将 org/ 从"文章专用"升级为"通用框架"需要以下改造：

### 5.1 governance.py — 规则参数化

```python
# 当前：硬编码
if "scam" in title or "fraud" in title:
    return PolicyVerdict(decision="block", notes=["title contains high-risk claims"])

# 改造后：可注入规则
def evaluate_policy(action: dict, rules: PolicyRules | None = None) -> PolicyVerdict:
    rules = rules or DEFAULT_POLICY_RULES
    for rule in rules.block_keywords:
        if rule in title:
            return PolicyVerdict(decision="block", notes=[f"title matches block keyword: {rule}"])
```

### 5.2 schema_guard.py — 场景验证规则注册

```python
# 当前：硬编码 skill_content_strategy
if owner == "skill_content_strategy":
    if not any("ai_tone_report" in r for r in refs):
        issues.append("content action requires ai_tone_report evidence")

# 改造后：注册制
_SCENE_VALIDATORS: dict[str, Callable] = {}

def register_scene_validator(owner_agent: str, fn: Callable):
    _SCENE_VALIDATORS[owner_agent] = fn

# 文章场景注册
register_scene_validator("skill_content_strategy", validate_article_evidence)
# 视频场景注册
register_scene_validator("skill_lesson_content_planning", validate_video_evidence)
```

### 5.3 config.py — 多场景配置

```python
# 当前：blue_ocean 专用配置
REPORTS_DIR = ROOT / "reports"

# 改造后：按场景隔离
SCENARIO_CONFIGS = {
    "article": {"reports_dir": ROOT / "reports", ...},
    "video": {"reports_dir": PROJECT_ROOT / "reports" / "video_org", ...},
}
```

### 5.4 改造工作量估算

| 改造项 | 文件 | 估计工时 |
|--------|------|----------|
| governance 参数化 | governance.py | 2h |
| schema_guard 注册制 | schema_guard.py | 2h |
| config 多场景 | config.py + runtime_store.py | 1h |
| feishu_dispatch 场景适配 | feishu_dispatch.py | 2h |
| scenario_video.py 编写 | 新文件 | 4-6h |
| video_quality_gate.py 编写 | 新文件 | 2-3h |
| 集成测试 | 端到端测试 | 3-4h |
| **总计** | | **16-20h** |

---

## 六、深度反思

### 反思 1：这个视角是否成立？

**挑战**：blue_ocean 的 org/ 真的是"通用框架"吗？还是它只是一个被过度泛化解读的"文章生产工具"？

**回应**：
- 审查代码后，org/ 的核心抽象（Action Package、Policy/Risk 裁决、状态机、飞书推送）确实是领域无关的。action_package_schema.json 中没有任何字段绑定"文章"概念——`title`、`objective`、`constraints`、`execution`、`validation` 都是通用的。
- `scenario_article.py` 是唯一绑定"文章"领域的文件。如果将它视为"第一个场景实现"而非"核心框架的一部分"，org/ 的通用性就成立了。
- Agent Charter（`agent_charter_v1.md`）的设计也是领域无关的——它定义的是组织角色和决策流程，不是具体业务逻辑。

**结论**：这个视角成立。org/ 确实可以被提取为通用框架。

### 反思 2：视频生产真的需要治理吗？

**挑战**：当前 yyy_ball 的工作流是"Agent 生成 animate.py → 渲染 → 完成"。这已经够了。为什么需要 Policy/Risk 裁决和 CEO 审批？

**回应**：
- 当视频生产是手动的、低频的（每周几个），直接渲染即可。
- 但如果目标是**规模化自动生产**（每天多个系列、多节课同时推进），就需要：
  - **调度**：哪些课优先做？资源冲突怎么办？
  - **质量控制**：渲染失败自动重试还是升级人工？内容敏感怎么拦截？
  - **CEO 审批**：新系列上线、重大课程调整需要人工确认。
  - **可追溯性**：每个视频的生产全链路有审计日志。
  - **异常处理**：渲染失败后的自动降级/重试/告警。
- 这些都是 org/ 治理框架已经解决的问题。

**但这是一个"何时需要"的问题**，不是"是否需要"的问题。当前阶段如果视频产量还不需要自动化治理，过早引入框架会是过度工程化。

### 反思 3：合并 vs 分离 — 重新校准

之前的分析认为合并没有好处。现在的发现是：**如果两者共享治理框架，合并在架构上有合理性**。但这并不意味着一定要物理合并到同一仓库。

| 共享模式 | 适用场景 | 推荐度 |
|----------|----------|--------|
| 方案 E（独立包） | 团队 ≥3 人，两个产品独立演进 | ⭐⭐⭐⭐⭐ |
| 方案 G（uv workspace） | 团队 1-2 人，希望单仓库简单管理 | ⭐⭐⭐⭐ |
| 方案 F（简单合并） | 团队 1 人，不在意仓库纯洁性 | ⭐⭐⭐ |
| 不合并不共享 | 两者发展路径不同，治理需求不紧迫 | ⭐⭐ |

### 反思 4：monitors/ 和 video 的关系

**挑战**：如果 monitors/ 的市场情报可以直接驱动视频选题呢？

**回应**：
- 这是一个有吸引力的想法：`gap_analyzer` 发现"AI隐私"是热门话题 → 自动创建一个视频 action package "制作AI隐私主题理财课"。
- 但这需要一个**信号翻译层**，将市场情报的 gap 映射到视频系列的具体课题。这比简单的代码复用更复杂，涉及领域知识的转换。
- 如果这条路走通了，monitors/ 就变成了两个场景的共享上游信号源，进一步加强了统一框架的论据。

### 反思 5：时机判断

**关键问题**：现在就做这个统一，还是等到视频产量需要治理时再做？

**务实建议**：
1. **现在做**：将 org/ 的治理层 + 通用层提取为独立包（方案 E），但**暂不编写** `scenario_video.py`。只做"可复用的基础"。
2. **当视频产量需要治理时**：编写 `scenario_video.py`，接入 org-runtime。
3. **当两个场景都稳定时**：评估是否需要 monitors/ 驱动视频选题。

这样既保留了扩展能力，又不过度工程化。

### 反思 6：前文结论需要修正吗？

前文说"领域正交、不应合并"。现在的修正：

> 两者的**业务领域**确实正交（视频 vs 文章），但它们的**运营模型**可以是同构的（都是「CEO + Agent + 飞书」）。这个同构性产生了约 1150 行可复用的治理基础设施。是否合并取决于团队对"统一运营模型"的战略判断——如果决定走这条路，就值得提取共享框架；如果不需要，保持分离依然正确。

---

## 七、分阶段执行计划

### 阶段 0：决策（Day 0）

回答一个核心问题：**yyy_ball 的视频生产是否需要组织治理？**

- 如果"是"或"未来需要" → 进入阶段 1
- 如果"不需要" → 保持现状，前文结论不变

### 阶段 1：提取 org-runtime（1-2 天）

1. 创建 `yyy-org-runtime` 仓库（或 yyy_ball 下的 `org_runtime/` 目录）。
2. 将以下文件从 blue_ocean 复制并去耦合：
   - `governance.py` → 参数化 policy rules
   - `schema_guard.py` → 注册制验证
   - `runtime_store.py` → 可配置存储路径
   - `feishu/` 下所有文件 → 不变
   - `common/llm.py`、`common/store.py`、`common/notify.py` → 不变
3. 验证 blue_ocean 改为依赖 org-runtime 后功能不变。

### 阶段 2：视频场景接入（2-3 天）

4. 在 yyy_ball 中编写 `scenario_video.py`。
5. 编写 `video_quality_gate.py`（渲染完整性检查）。
6. 在 yyy_ball 的 `.cursor/skills/` 中新增一个 `video-org-orchestrator` skill，定义飞书驱动的视频生产流程。
7. 端到端测试：用一节已有课程走完 "提案 → 治理 → 渲染 → 门禁 → 飞书通知" 全流程。

### 阶段 3：信号驱动（可选，1-2 周）

8. 编写信号翻译层：market gap → video topic proposal。
9. blue_ocean 的 monitors 输出可以自动触发 yyy_ball 的 scenario_video。
10. 两个场景共享同一个飞书群，CEO 在一个地方审批所有动作。

---

## 八、最终建议

| # | 建议 | 条件 |
|---|------|------|
| 1 | **提取 org-runtime 为独立共享包** | 如果决定走「统一治理模型」路线 |
| 2 | **不急于合并仓库** | org-runtime 可以先作为 path dependency 开发 |
| 3 | **视频场景按需接入** | 等到视频产量需要自动化调度时再编写 scenario_video |
| 4 | **前文结论依然有效** | 即使提取共享框架，blue_ocean 的 monitors/ 和场景层仍应留在 yyy-oversea |

**一句话总结**：blue_ocean 和 yyy_ball 的业务领域不应合并，但它们的**运营治理基础设施**值得统一。正确的做法是"共享框架，分离场景"——提取治理层为独立包，两个仓库各自实现自己的场景逻辑。
