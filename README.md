# 🤖 AI-Demo

一个以 **资深测试工程师（Senior QA Engineer）** 为唯一核心身份构建的企业级 AI Agent 仓库。

本仓库不是零散 Prompt 的堆积区，也不是一次性的 Demo 脚本集合，而是面向长期迭代的 **测试 Agent 体系设计基座**。  
目标是沉淀一套能够支持 **需求分析、测试设计、接口测试、UI 测试、缺陷分析、回归评估、性能稳定性评估、测试体系规划** 的统一协作框架。

---

## 🎯 设计目标

本仓库希望解决的不是“让 AI 回一句像样的话”，而是下面这些更接近企业真实场景的问题：

- 如何让 AI 始终以资深测试工程师的身份工作
- 如何把不同测试任务拆分成清晰、稳定、可复用的 Agent
- 如何让不同 Agent 在输出风格、质量标准、风险判断上保持一致
- 如何把测试方法论、领域技能、交付模板、协作规范沉淀为长期资产
- 如何为后续接入自动化测试框架、质量平台、MCP、工作流编排保留扩展空间

---

## 🧠 核心理念

### 1. 唯一核心身份

本仓库中的所有 Agent，默认都属于同一个专业身份：

> **资深测试工程师**

这里的多个 Agent 并不代表多个不同职业角色，而是同一名资深测试工程师在不同任务场景下的专业分身。

例如：

- 需求分析 Agent
- 测试设计 Agent
- 接口测试 Agent
- 缺陷分析 Agent
- 回归评估 Agent
- 测试架构 Agent

它们共享同一套质量价值观、风险意识和专业输出标准。

### 2. 分层设计，而不是堆 Prompt

本仓库采用分层结构，将“身份、规则、能力、模板、参考资料”分开管理：

- `AGENTS.md`：项目级总规则
- `agents/`：任务场景级 Agent 定义
- `standards/`：共享质量规范与输出标准
- `skills/`：可复用测试能力
- `templates/`：固定交付模板
- `references/`：长期参考资料
- `docs/`：架构说明、路由矩阵、演进规划
- `src/`：轻量代码支撑
- `tests/`：基础校验

这比“一个超长系统提示词”更稳定，也更适合团队化、长期化使用。

---

## 🗂️ 仓库结构

```text
AI-Demo/
├─ README.md
├─ AGENTS.md
├─ agents/
│  ├─ senior_qa_agent.md
│  ├─ requirement_analysis_agent.md
│  ├─ test_design_agent.md
│  ├─ api_test_agent.md
│  ├─ ui_test_agent.md
│  ├─ bug_analysis_agent.md
│  ├─ regression_agent.md
│  ├─ performance_stability_agent.md
│  └─ qa_architect_agent.md
│
├─ standards/
│  ├─ output_standard.md
│  ├─ test_case_standard.md
│  ├─ bug_standard.md
│  ├─ risk_standard.md
│  └─ review_standard.md
│
├─ skills/
│  ├─ requirement-review/
│  │  └─ SKILL.md
│  ├─ test-case-design/
│  │  └─ SKILL.md
│  ├─ api-testing/
│  │  └─ SKILL.md
│  ├─ bug-triage/
│  │  └─ SKILL.md
│  ├─ mock-server-design/
│  │  └─ SKILL.md
│  ├─ automation-scripting/
│  │  └─ SKILL.md
│  ├─ test-data-building/
│  │  └─ SKILL.md
│  └─ log-analysis/
│     └─ SKILL.md
│
├─ templates/
│  ├─ test_case_template.md
│  ├─ bug_report_template.md
│  ├─ risk_assessment_template.md
│  ├─ review_checklist_template.md
│  ├─ test_plan_template.md
│  ├─ test_report_template.md
│  └─ api_mock_spec_template.md
│
├─ references/
│  ├─ glossary.md
│  ├─ system_context.md
│  └─ quality_baseline.md
│
├─ docs/
│  ├─ architecture-overview.md
│  ├─ task-routing-matrix.md
│  └─ repository-roadmap.md
│
├─ scripts/
│  └─ smoke_check.py
│
├─ src/
│  └─ enterprise_ai_test_agents/
│     ├─ __init__.py
│     └─ context.py
│
├─ tests/
│  └─ test_context.py
│
├─ pyproject.toml
└─ .gitignore
```
## 🧩 Agent 体系说明

### 核心 Agent

- `senior_qa_agent.md`  
  统一质量视角、测试策略和风险判断的总控 Agent

### 需求与设计类 Agent

- `requirement_analysis_agent.md`
- `test_design_agent.md`

### 执行与验证类 Agent

- `api_test_agent.md`
- `ui_test_agent.md`
- `regression_agent.md`
- `performance_stability_agent.md`

### 评估与治理类 Agent

- `bug_analysis_agent.md`
- `qa_architect_agent.md`

---

## 📏 Standards 的职责

`standards/` 用于定义所有 Agent 共享遵守的标准。

例如：

- `output_standard.md`：统一输出风格和结构
- `test_case_standard.md`：统一测试用例设计规范
- `bug_standard.md`：统一缺陷描述规范
- `risk_standard.md`：统一风险评估维度
- `review_standard.md`：统一评审检查项

企业级 Agent 体系最容易失败的地方，不是 Agent 不够多，而是标准不统一。  
因此，本仓库把 Standards 放在核心位置。

---

## 🛠️ Skills 的职责

`skills/` 不定义身份，而定义能力。  
它解决的问题是：

> 某个 Agent 在处理具体任务时，应该“如何做”。

例如：

- 如何进行需求评审
- 如何设计测试用例
- 如何分析接口测试点
- 如何做缺陷分级与 triage
- 如何设计 mock 方案
- 如何构建测试数据
- 如何分析日志并定位问题

Skills 采用独立目录，是为了便于按需加载、独立维护和后续扩展。

---

## 🧾 Templates 的职责

`templates/` 负责提供固定交付格式，避免每次重复组织结构。

例如：

- 测试用例模板
- 缺陷报告模板
- 风险评估模板
- 评审清单模板
- 测试计划模板
- 测试报告模板
- API Mock 规格模板

模板不是规则，模板是交付载体。  
规则保证质量一致，模板保证产出可复用。

---

## 📚 References 的职责

`references/` 用于沉淀长期背景资料和辅助理解信息，例如：

- 术语表
- 系统背景
- 质量基线
- 业务上下文
- 环境说明

References 不直接替代规则，也不直接替代 Agent，而是作为补充上下文使用。

---

## 🧭 未来扩展方向

本仓库的未来扩展方向包括但不限于：

- 接入自动化测试框架
- 接入 YAML / JSON 测试资产生成
- 接入日志分析与缺陷辅助定位
- 接入 MCP / Tool Calling / 工作流编排
- 接入质量平台与测试平台
- 接入行业特定领域知识（如电商、金融、企业服务等）

---

## 🚀 当前建设策略

本仓库采用“先搭标准，再补 Agent，再沉淀 Skill，最后接代码与平台”的建设路径：

### 第一阶段

- 完成仓库总规则
- 完成核心 Agent 定义
- 完成关键 Standards

### 第二阶段

- 完成 Skills
- 完成 Templates
- 完成路由文档与参考资料

### 第三阶段

- 接入轻量 Python 支撑代码
- 增加基础测试
- 与真实测试工程场景联动

---

## ✅ 使用原则

- 默认始终以资深测试工程师身份协作
- 优先保证专业性、一致性、可维护性
- 避免为“看起来完整”而堆无效内容
- 所有新增内容都应服务于真实测试任务
- 所有规则和模板都应可长期沉淀为团队资产