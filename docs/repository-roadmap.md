# 🗺️ Repository Roadmap

---

## 🎯 Purpose

本文件用于说明本仓库当前的建设进度、阶段目标、优先级顺序和后续演进方向。

它解决的问题包括：

- 当前仓库已经完成了什么
- 当前仓库还缺什么
- 哪些目录和文件是已落地能力
- 哪些目录和文件仍属于预留扩展
- 下一阶段最值得优先补什么
- 如何避免仓库无序扩张

本文件不是 README 的重复描述，而是仓库级的建设路线图与阶段说明。

---

## 🧭 Roadmap Principles

本仓库的后续建设默认遵守以下原则：

### 1. Core First

优先补充核心能力，而不是铺量式补文件。

### 2. Honest Progress Tracking

明确区分“已完成”“进行中”“预留扩展”，不夸大当前完成度。

### 3. Layered Evolution

优先保证 Identity / Agent / Standard / Routing 等核心层稳定，再扩展 Skill、Template、Reference 和工程化能力。

### 4. Reuse over Quantity

优先补高复用、高价值内容，而不是追求文件数量。

### 5. Engineering Alignment

仓库演进应逐步走向工程化，而不是永远停留在纯文档层。

---

## ✅ Current Status Summary

截至当前阶段，本仓库已经完成了第一批核心骨架建设，已经具备企业级测试 Agent 仓库的基础形态。

当前已具备以下能力：

- 项目级总规则
- 核心测试 Agent 体系
- 核心 Standard 体系
- 基础 Routing 机制
- 部分高价值 Skill
- 部分高价值 Template
- 最小代码支撑
- 最小测试校验

这意味着本仓库当前已从“概念仓库”进入“可持续演进的测试 Agent 仓库雏形”。

---

## 🏗️ Phase Breakdown

### Phase 1：Core Framework Established

#### Goal

建立仓库的最小核心架构，确保身份、角色、标准、路由与工程入口具备基本闭环。

#### Completed Items

- `README.md`
- `AGENTS.md`
- 核心 `agents/`
- 核心 `standards/`
- `docs/architecture-overview.md`
- `docs/task-routing-matrix.md`
- `src/enterprise_ai_test_agents/context.py`
- `scripts/smoke_check.py`
- `tests/test_context.py`
- `conftest.py`

#### Phase Result

第一阶段已经完成。  
仓库已经具备清晰的结构分层和基本工程支撑。

---

### Phase 2：High-Value Skill and Template Accumulation

#### Goal

围绕最常用、最高价值的测试场景，补齐方法层和交付层，让仓库具备更强的实际使用价值。

#### Completed Items

##### Skills

- `skills/test-case-design/SKILL.md`
- `skills/api-testing/SKILL.md`
- `skills/requirement-review/SKILL.md`
- `skills/log-analysis/SKILL.md`

##### Templates

- `templates/test_case_template.md`
- `templates/bug_report_template.md`
- `templates/risk_assessment_template.md`
- `templates/test_report_template.md`

#### Phase Result

第二阶段已完成首批高价值沉淀。  
仓库已经具备较强的测试设计、需求评审、接口测试、日志分析和交付模板支撑能力。

---

### Phase 3：Planned Expansion

#### Goal

围绕测试治理、平台化和更复杂任务场景，继续补齐尚未落地的高价值模块。

#### Planned Items

##### Skills（候选）

- `skills/bug-triage/SKILL.md`
- `skills/mock-server-design/SKILL.md`
- `skills/automation-scripting/SKILL.md`
- `skills/test-data-building/SKILL.md`

##### Templates（候选）

- `templates/test_plan_template.md`
- `templates/review_checklist_template.md`
- `templates/api_mock_spec_template.md`

##### References（候选）

- `references/glossary.md`
- `references/system_context.md`
- `references/quality_baseline.md`

#### Phase Result Target

第三阶段完成后，仓库将从“高价值核心能力已落地”进一步升级为“更接近团队协作与平台化落地的完整测试 Agent 仓库”。

---

### Phase 4：Engineering and Platform Integration

#### Goal

将当前文档化能力逐步接入更真实的工程环境与测试平台能力。

#### Planned Items

- 增强 `context.py` 的动态感知能力
- 增加更多最小测试校验
- 为 CLI / Script / 内部工具接入预留能力
- 与自动化测试框架衔接
- 与日志、报告、测试平台联动
- 为未来接入 MCP / Workflow / 工具调用能力预留结构

#### Phase Result Target

第四阶段完成后，仓库将不再只是“结构完整的测试 Agent 仓库”，而会开始具备真实工程接入价值。

---

## 📌 Current Priority Order

当前阶段建议的优先级如下：

### Priority 1：保持核心层稳定

包括：

- `README.md`
- `AGENTS.md`
- `agents/`
- `standards/`
- `docs/architecture-overview.md`
- `docs/task-routing-matrix.md`

这部分应优先保持稳定，不频繁大改。

---

### Priority 2：继续补高价值 Skill / Template

优先补充那些能够显著增强仓库实用性的内容，而不是补边缘文件。

优先顺序建议：

1. `skills/bug-triage/SKILL.md`
2. `templates/test_plan_template.md`
3. `templates/review_checklist_template.md`
4. `skills/mock-server-design/SKILL.md`

---

### Priority 3：逐步补充 Reference

References 目前可保留为空或半空状态，但不建议优先投入过多精力。  
只有在仓库开始服务于更真实业务上下文时，再逐步补充更合适。

---

### Priority 4：增强代码支撑层

在当前文档结构趋于稳定后，逐步增强：

- `context.py`
- `smoke_check.py`
- `tests/`

但此阶段不宜过早做重度工程化。

---

## 🟡 Completed vs Planned Clarification

为避免误解，当前仓库中的内容应明确分为三类：

### 1. Completed

已经真实存在、已具备内容、已可直接使用的文件。

### 2. In Progress

已经有目录或初步文件，但内容尚不完整，仍在逐步补充。

### 3. Planned / Reserved

当前主要作为预留扩展位存在，尚未真正完成的文件和目录。

---

## 📂 Directory Maturity Notes

### agents/

成熟度：**高**

说明：  
核心 Agent 已基本齐全，当前重点应转向微调与协作优化，而不是继续大量新增 Agent。

---

### standards/

成熟度：**高**

说明：  
核心标准已具备，后续重点应保持稳定与小步修正。

---

### skills/

成熟度：**中**

说明：  
已有高价值核心技能，但仍有若干扩展技能未完成。  
后续应按真实使用价值逐个补充，不建议一次补全所有目录。

---

### templates/

成熟度：**中**

说明：  
高频模板已开始成型，但仍存在若干规划中模板。  
建议优先补与当前 Agent 使用频率高的模板。

---

### references/

成熟度：**低**

说明：  
当前更多是预留扩展，不应被误认为已完整落地。

---

### docs/

成熟度：**高**

说明：  
说明层和路由层已经具备较完整基础，后续可少量补充，不建议频繁重写。

---

### src / scripts / tests/

成熟度：**中**

说明：  
已有最小代码支撑，但距离“真实工程工具层”仍有明显空间。  
后续应逐步增强，而不是突然复杂化。

---

## ⚠️ Current Constraints

当前仓库继续演进时，应注意以下约束：

- 不要为了填满目录而补低价值文件
- 不要让 README 过度承担 Roadmap 职责
- 不要让 Routing 文档长期领先于实际落地太多
- 不要频繁改动核心 Standard 和核心 Agent，避免结构不稳定
- 不要过早引入复杂代码层，导致维护成本失控
- 不要让仓库退化成“很多文件但没有优先级”的状态

---

## ✅ Next Recommended Actions

当前阶段完成后，建议下一步优先考虑以下动作：

1. 校准 `README.md`，区分“当前已落地”与“预留扩展”
2. 校准 `docs/task-routing-matrix.md`，为未落地文件增加“可选 / 后续补充”语义
3. 视实际需要补充以下高价值内容之一：
   - `skills/bug-triage/SKILL.md`
   - `templates/test_plan_template.md`
   - `templates/review_checklist_template.md`
4. 逐步增强 `context.py` 和测试覆盖，而不是继续快速铺文档

---

## 🏁 Final Requirement

本路线图的最终目标不是把仓库“填满”，而是：

> 让仓库始终沿着清晰、可控、可复用、可工程化的方向演进，逐步沉淀为一套真正具备企业级价值的测试 Agent 协作体系。