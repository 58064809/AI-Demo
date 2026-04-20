# 任务路由矩阵

本文件定义“用户问题如何路由到合适的测试子 Agent”，以及每个 Agent 默认应加载哪些标准和可选技能。

目标不是让每次对话读取全部文件，而是建立一套稳定、低成本、可维护的按需加载机制。

## 路由原则

1. 先识别用户当前最核心的问题是什么
2. 一个任务优先只选一个主 Agent
3. 只有在主 Agent 无法独立完成时，才补充次级 Agent 视角
4. 默认只加载 `output_standard.md` 和主 Agent 必需的标准
5. 只有命中具体能力时，才补充 Skill
6. 模板和参考资料始终按需加载

## 主 Agent 选择规则

### 1. `requirement_analysis_agent.md`

优先命中关键词或场景：

- 需求评审
- 需求澄清
- PRD 分析
- 测试点拆解前置分析
- 范围不清
- 规则冲突

默认加载 Standards：

- `standards/output_standard.md`
- `standards/review_standard.md`
- `standards/risk_standard.md`

可选加载 Skills：

- `skills/requirement-review/SKILL.md`
- `skills/bug-triage/SKILL.md`

常用模板：

- `templates/review_checklist_template.md`
- `templates/risk_assessment_template.md`

### 2. `test_design_agent.md`

优先命中关键词或场景：

- 设计测试点
- 写测试用例
- 补漏测试
- 用例评审
- 覆盖设计

默认加载 Standards：

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/review_standard.md`

可选加载 Skills：

- `skills/test-case-design/SKILL.md`
- `skills/api-testing/SKILL.md`

常用模板：

- `templates/test_case_template.md`
- `templates/review_checklist_template.md`

### 3. `api_test_agent.md`

优先命中关键词或场景：

- 接口测试
- API 测试
- Swagger / OpenAPI 分析
- 入参出参校验
- 鉴权 / 幂等 / 状态码分析
- 接口自动化设计

默认加载 Standards：

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/risk_standard.md`

可选加载 Skills：

- `skills/api-testing/SKILL.md`
- `skills/mock-server-design/SKILL.md`

常用模板：

- `templates/test_case_template.md`
- `templates/api_mock_spec_template.md`
- `templates/risk_assessment_template.md`

### 4. `ui_test_agent.md`

优先命中关键词或场景：

- 页面测试
- 交互测试
- 前端回归
- 按钮状态
- 文案提示
- 页面流程验证

默认加载 Standards：

- `standards/output_standard.md`
- `standards/test_case_standard.md`
- `standards/review_standard.md`

可选加载 Skills：

- `skills/test-case-design/SKILL.md`

常用模板：

- `templates/test_case_template.md`
- `templates/review_checklist_template.md`

### 5. `bug_analysis_agent.md`

优先命中关键词或场景：

- Bug 分析
- 缺陷评估
- 线上问题
- 是否阻塞上线
- 根因分析
- 影响范围判断

默认加载 Standards：

- `standards/output_standard.md`
- `standards/bug_standard.md`
- `standards/risk_standard.md`

可选加载 Skills：

- `skills/bug-triage/SKILL.md`

常用模板：

- `templates/bug_report_template.md`
- `templates/risk_assessment_template.md`

### 6. `regression_agent.md`

优先命中关键词或场景：

- 回归测试
- 发版回归
- 改动影响分析
- 最小回归集
- 灰度前检查

默认加载 Standards：

- `standards/output_standard.md`
- `standards/risk_standard.md`
- `standards/review_standard.md`

可选加载 Skills：

- `skills/test-case-design/SKILL.md`
- `skills/api-testing/SKILL.md`

常用模板：

- `templates/test_report_template.md`
- `templates/risk_assessment_template.md`

### 7. `performance_stability_agent.md`

优先命中关键词或场景：

- 性能测试
- 压测方案
- 稳定性测试
- 容量评估
- 慢接口
- 并发风险

默认加载 Standards：

- `standards/output_standard.md`
- `standards/risk_standard.md`

可选加载 Skills：

- `skills/api-testing/SKILL.md`
- `skills/log-analysis/SKILL.md`

常用模板：

- `templates/test_report_template.md`
- `templates/risk_assessment_template.md`

### 8. `qa_architect_agent.md`

优先命中关键词或场景：

- 测试体系建设
- 自动化架构设计
- 质量平台规划
- 测试流程治理
- 环境 / 数据 / Mock / CI 规划
- 企业级 Agent 架构设计

默认加载 Standards：

- `standards/output_standard.md`
- `standards/review_standard.md`
- `standards/risk_standard.md`

可选加载 Skills：

- `skills/mock-server-design/SKILL.md`
- `skills/automation-scripting/SKILL.md`
- `skills/test-data-building/SKILL.md`

常用模板：

- `templates/test_plan_template.md`
- `templates/review_checklist_template.md`
- `templates/risk_assessment_template.md`

## 次级 Agent 补充规则

仅在以下情况下引入次级 Agent：

- 主 Agent 的输出需要另一个专业视角才能闭环
- 用户明确要求从多个测试维度同时分析
- 风险判断已经跨越单一任务场景

典型组合：

- 需求评审 + 测试点设计：`requirement_analysis_agent` + `test_design_agent`
- 接口设计 + Mock 方案：`api_test_agent` + `qa_architect_agent`
- 缺陷评估 + 是否阻塞上线：`bug_analysis_agent` + `regression_agent`
- 回归范围评估 + 性能风险：`regression_agent` + `performance_stability_agent`

## 不建议的做法

- 不要默认同时加载多个 Agent
- 不要为了“完整”而强行读取全部 Standards
- 不要在没有明确场景时提前加载 Skills
- 不要把模板当成规则全文重复展开

