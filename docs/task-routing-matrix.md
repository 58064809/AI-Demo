# 🧭 Task Routing Matrix

---

## 🎯 Purpose

本文件用于定义：

- 不同类型的任务应优先路由到哪个 Agent
- 每个 Agent 默认应加载哪些 Standards
- 哪些 Skills 是按需补充的
- 哪些 Templates 在特定交付场景下需要启用
- 何时需要引入次级 Agent 视角

它的目标不是让每次任务都读取全部文件，而是建立一套 **稳定、低成本、可维护、可扩展** 的按需加载机制。

---

## 🧠 Routing Principles

### 1. One Primary Agent First

一个任务默认优先只选择 **一个主 Agent**。  
不要一开始同时加载多个 Agent，以避免职责混乱和输出失焦。

### 2. Standards Before Skills

默认先确定：

- 主 Agent
- 必需 Standards

只有命中具体处理能力时，才补充对应 Skills。

### 3. Templates On Demand

Template 只在需要固定交付格式时使用，不作为默认加载项。

### 4. References On Demand

References 仅用于补充背景信息，不替代 Agent、Standard 或 Skill。

### 5. Secondary Agent Only When Necessary

只有主 Agent 无法独立闭环，或者任务天然跨多个测试维度时，才引入次级 Agent。

---

## 📦 Default Loading Order

默认加载顺序如下：

1. `AGENTS.md`
2. `standards/output_standard.md`
3. 主 Agent
4. 主 Agent 对应的默认 Standards
5. 需要时补充相关 Skills
6. 需要固定交付格式时补充 Templates
7. 需要背景资料时补充 References

---

## 🧩 Primary Routing Matrix

### 1. Requirement Analysis Tasks

#### Typical Scenarios

- 需求评审
- PRD 分析
- 规则梳理
- 测试关注点提炼
- 可测试性分析
- 需求歧义 / 冲突 / 缺口识别

#### Primary Agent

- `agents/requirement_analysis_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/review_standard.md`
- `standards/risk_standard.md`

#### Optional Skills

- `skills/requirement-review/SKILL.md`

#### Optional Templates

- `templates/review_checklist_template.md`
- `templates/risk_assessment_template.md`

---

### 2. Test Design Tasks

#### Typical Scenarios

- 设计测试点
- 设计测试用例
- 补漏测试场景
- 测试覆盖评审
- 用例结构整理

#### Primary Agent

- `agents/test_design_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/review_standard.md`

#### Optional Skills

- `skills/test-case-design/SKILL.md`

#### Optional Templates

- `templates/test_case_template.md`
- `templates/review_checklist_template.md`

---

### 3. API Testing Tasks

#### Typical Scenarios

- 接口测试分析
- Swagger / OpenAPI 分析
- 参数校验测试
- 鉴权与幂等分析
- 接口自动化输入整理
- 接口风险识别

#### Primary Agent

- `agents/api_test_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/risk_standard.md`

#### Optional Skills

- `skills/api-testing/SKILL.md`
- `skills/mock-server-design/SKILL.md`

#### Optional Templates

- `templates/test_case_template.md`
- `templates/api_mock_spec_template.md`
- `templates/risk_assessment_template.md`

---

### 4. UI Testing Tasks

#### Typical Scenarios

- 页面测试分析
- 交互测试设计
- 前端回归测试
- 页面展示与反馈校验
- 表单与按钮状态校验
- 页面流程验证

#### Primary Agent

- `agents/ui_test_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/review_standard.md`

#### Optional Skills

- `skills/test-case-design/SKILL.md`

#### Optional Templates

- `templates/test_case_template.md`
- `templates/review_checklist_template.md`

---

### 5. Bug Analysis Tasks

#### Typical Scenarios

- 缺陷分析
- 问题归因
- 严重程度建议
- 是否阻塞上线判断
- 影响范围分析
- 缺陷复盘

#### Primary Agent

- `agents/bug_analysis_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/bug_standard.md`
- `standards/risk_standard.md`

#### Optional Skills

- `skills/bug-triage/SKILL.md`
- `skills/log-analysis/SKILL.md`

#### Optional Templates

- `templates/bug_report_template.md`
- `templates/risk_assessment_template.md`

---

### 6. Regression Tasks

#### Typical Scenarios

- 发版回归范围评估
- 改动影响分析
- 最小回归集设计
- 修复后补回归
- 上线前回归建议

#### Primary Agent

- `agents/regression_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/risk_standard.md`

#### Optional Skills

- `skills/test-case-design/SKILL.md`
- `skills/api-testing/SKILL.md`

#### Optional Templates

- `templates/test_plan_template.md`
- `templates/test_report_template.md`
- `templates/risk_assessment_template.md`

---

### 7. Performance and Stability Tasks

#### Typical Scenarios

- 性能风险分析
- 压测方案设计
- 稳定性测试设计
- 容量评估
- 高并发风险识别
- 长稳测试建议

#### Primary Agent

- `agents/performance_stability_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/risk_standard.md`

#### Optional Skills

- `skills/api-testing/SKILL.md`
- `skills/log-analysis/SKILL.md`

#### Optional Templates

- `templates/test_plan_template.md`
- `templates/test_report_template.md`
- `templates/risk_assessment_template.md`

---

### 8. QA Architecture and Governance Tasks

#### Typical Scenarios

- 测试体系建设
- 测试架构设计
- 自动化能力规划
- 测试平台规划
- 质量治理机制设计
- 流程与规范建设

#### Primary Agent

- `agents/qa_architect_agent.md`

#### Default Standards

- `standards/output_standard.md`
- `standards/review_standard.md`
- `standards/risk_standard.md`

#### Optional Skills

- `skills/automation-scripting/SKILL.md`
- `skills/test-data-building/SKILL.md`
- `skills/mock-server-design/SKILL.md`

#### Optional Templates

- `templates/test_plan_template.md`
- `templates/review_checklist_template.md`
- `templates/risk_assessment_template.md`

---

## 🔄 Secondary Agent Trigger Rules

仅在以下情况下引入次级 Agent：

### 1. Multi-Dimensional Analysis Required

用户明确要求从多个测试维度同时分析，例如：

- 需求分析 + 测试设计
- 缺陷分析 + 上线风险判断
- UI 问题 + 接口联动验证

### 2. Primary Agent Cannot Close the Task Alone

主 Agent 已完成本职分析，但任务需要额外专业视角才能闭环。

### 3. Risk or Impact Crosses Boundaries

风险或影响已经跨越多个测试域，例如：

- 前端现象问题，根因在接口状态机
- 接口修复，影响回归范围和上线判断
- 需求改动，同时影响 UI、接口和性能链路

---

## 🧪 Recommended Secondary Agent Combinations

### Requirement Analysis + Test Design

适用场景：

- 需求刚拿到，需要先拆规则再补用例

组合：

- 主 Agent：`requirement_analysis_agent.md`
- 次级 Agent：`test_design_agent.md`

---

### Test Design + API Testing

适用场景：

- 接口规则复杂，需要结合通用测试设计和接口细节

组合：

- 主 Agent：`test_design_agent.md`
- 次级 Agent：`api_test_agent.md`

---

### Test Design + UI Testing

适用场景：

- 页面流程与交互复杂，需要设计 UI 侧用例

组合：

- 主 Agent：`test_design_agent.md`
- 次级 Agent：`ui_test_agent.md`

---

### Bug Analysis + Regression

适用场景：

- 缺陷修复后需要评估补测和回归范围

组合：

- 主 Agent：`bug_analysis_agent.md`
- 次级 Agent：`regression_agent.md`

---

### Bug Analysis + API Testing

适用场景：

- 页面问题或业务问题实际落在接口层

组合：

- 主 Agent：`bug_analysis_agent.md`
- 次级 Agent：`api_test_agent.md`

---

### Regression + Performance and Stability

适用场景：

- 发布前既要回归，又担心并发或稳定性风险

组合：

- 主 Agent：`regression_agent.md`
- 次级 Agent：`performance_stability_agent.md`

---

### QA Architecture + Any Domain Agent

适用场景：

- 需要从具体测试场景反推体系建设方式

组合示例：

- `qa_architect_agent.md` + `api_test_agent.md`
- `qa_architect_agent.md` + `ui_test_agent.md`
- `qa_architect_agent.md` + `regression_agent.md`

---

## 🚫 Anti-Patterns

禁止以下使用方式：

### 1. Default Multi-Agent Loading

不要默认同时加载多个 Agent。

### 2. Full Repository Loading by Default

不要一上来读取所有 Standards、Skills、Templates、References。

### 3. Skills Before Problem Type

不要在任务类型尚未确定前提前加载 Skills。

### 4. Template as Rule Replacement

不要把 Template 当成规则全文使用。

### 5. Missing Risk Perspective

即使是设计和执行类任务，也不能缺失风险视角。

---

## ✅ Routing Outcome Requirements

完成路由后，至少应明确以下信息：

- 当前主 Agent 是谁
- 为什么选择它
- 默认应加载哪些 Standards
- 是否需要补充 Skills
- 是否需要固定输出模板
- 是否需要次级 Agent 参与
- 是否存在待确认项会影响后续路由

---

## 🏁 Final Requirement

本文件的最终目标不是“做一个分类表”，而是：

> 让仓库中的 Agent、Standards、Skills、Templates 和 References 形成一套清晰、稳定、可扩展的任务路由机制，使整个企业级测试 Agent 体系真正具备协作逻辑和长期演进能力。