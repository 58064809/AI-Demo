把需求、代码变更、接口文档、UI 页面、日志、测试报告等输入交给 AI Agent
让 Agent 自动分析风险、生成测试点、选择测试范围、执行测试、分析失败、维护用例
然后由人审核 Agent 的判断，并把它接入真实研发流程

质量策略设计
Agent 工作流设计
AI 输出评估
测试数据治理
风险判断
质量门禁
异常归因


Agentic QA 理想情况下应该能：
1. 读取需求或用户故事
2. 判断核心流程：登录、会员状态、商品、订单、支付、库存、权益
3. 生成测试计划
4. 自动生成接口/API/UI 测试
5. 准备测试数据
6. 执行测试
7. 读取失败日志和报告
8. 判断失败原因
9. 自动归类缺陷
10. 输出质量风险结论


3. Agentic QA Engineer 的核心职责
3.1 设计 AI 测试工作流
需求文档
→ Agent 分析测试范围
→ Agent 生成测试点
→ Agent 生成测试用例
→ Agent 选择自动化覆盖范围
→ Agent 生成/维护自动化脚本
→ CI 执行
→ Agent 分析失败
→ Agent 生成缺陷摘要
→ 人审核并确认风险
例如:

| Agent                      | 负责内容                                  |
| -------------------------- | ------------------------------------- |
| Requirement Analysis Agent | 分析需求、识别风险、提出疑问                        |
| Test Design Agent          | 生成测试点、测试用例、边界场景                       |
| API Test Agent             | 根据接口文档生成接口测试                          |
| UI Test Agent              | 根据页面或流程生成 UI 自动化                      |
| Test Data Agent            | 准备、清理、隔离测试数据                          |
| Execution Agent            | 调用 Pytest、Playwright、Postman、JMeter 等 |
| Failure Analysis Agent     | 分析日志、截图、报告、堆栈                         |
| Defect Triage Agent        | 归类缺陷、判断优先级、生成 Bug 描述                  |
| Regression Selection Agent | 根据代码变更选择回归范围                          |
| Report Agent               | 输出测试报告、风险结论、发布建议                      |

3.2 把 AI Agent 接入真实工具链

Agentic QA Engineer 不能只停留在聊天页面。

它要能接入：

| 类型          | 工具                                                           |
| ----------- | ------------------------------------------------------------ |
| 需求/文档       | Jira、Confluence、飞书文档、Notion、Markdown                         |
| 代码仓库        | GitHub、GitLab、Gitee                                          |
| 自动化框架       | Pytest、Playwright、JUnit、TestNG、Cypress                       |
| API 工具      | Postman、Apifox、OpenAPI/Swagger                               |
| CI/CD       | Jenkins、GitHub Actions、GitLab CI                             |
| 报告          | Allure、ReportPortal、JUnit XML                                |
| 日志          | ELK、Loki、CloudWatch、应用日志                                     |
| 监控          | Prometheus、Grafana、Datadog                                   |
| 缺陷系统        | Jira、禅道、TAPD、飞书项目                                            |
| AI/Agent 框架 | LangGraph、CrewAI、AutoGen、OpenAI Assistants/Responses API、MCP |


核心是：让 Agent 真正能读、能跑、能查、能判断，而不是只生成文本。

3.3 评估 AI 生成结果是否可信
AI 可能会：

漏掉关键测试场景
生成错误断言
编造接口字段
误判失败原因
忽略业务前置条件
生成不可执行脚本
把环境问题判断成代码问题

所以 Agentic QA Engineer 要建立评估标准：
| 评估维度 | 说明                   |
| ---- | -------------------- |
| 完整性  | 是否覆盖核心业务路径、异常路径、边界条件 |
| 正确性  | 用例、断言、数据是否符合真实业务规则   |
| 可执行性 | 脚本是否能运行，依赖是否清楚       |
| 可维护性 | 是否有清晰分层、复用、命名规范      |
| 可追溯性 | 用例能否追溯到需求、代码变更、缺陷    |
| 稳定性  | 是否容易 flaky，是否受环境影响   |
| 安全性  | 是否泄露敏感数据，是否错误操作生产环境  |
| 可解释性 | Agent 为什么这么判断，依据是什么  |

3.4 建立 Human-in-the-loop 机制

Agentic QA 不能一上来就完全无人化。

比较成熟的做法是：

低风险任务：允许 Agent 自动完成
中风险任务：Agent 生成，人审核后执行
高风险任务：Agent 只给建议，人必须确认

比如：
| 场景      | 自动化程度        |
| ------- | ------------ |
| 生成测试点   | 可自动生成，人审核    |
| 生成用例草稿  | 可自动生成，人抽检    |
| 执行只读测试  | 可自动执行        |
| 查询测试数据库 | 可自动执行，但限制权限  |
| 修改测试数据  | 需要审批或沙箱环境    |
| 线上环境操作  | 默认禁止或强审批     |
| 自动提 Bug | 可生成草稿，人确认后提交 |
| 自动发布拦截  | 需要质量门禁规则支持   |
Agentic QA Engineer 要设计权限边界，避免 Agent 乱操作。
4. 典型工作场景
场景 1：需求到测试用例自动生成

输入：

用户故事
PRD
验收标准
接口文档
历史缺陷

Agent 输出：

测试范围
测试点
正向用例
异常用例
边界用例
兼容性用例
接口用例
回归建议
风险问题清单

Agentic QA Engineer 要做的是：

设计 Prompt 模板
设计输出格式
接入需求系统
校验业务覆盖率
维护测试知识库
建立人工审核机制
场景 2：代码变更驱动精准回归

输入：

Git diff
PR 信息
影响文件
接口变更
数据库变更
历史缺陷
历史失败记录

Agent 判断：

这次改动影响哪些模块？
哪些接口需要测？
哪些 UI 流程需要回归？
哪些历史 Bug 可能复发？
哪些自动化用例需要执行？
是否需要人工探索测试？

输出：

精准回归测试清单
P0/P1/P2 风险级别
自动化执行计划
人工补充测试建议

这个方向非常有价值，因为企业最大痛点之一就是：每次发版不知道该回归多少。

场景 3：自动化失败智能分析

传统自动化失败后，人要自己看：

报错堆栈
请求响应
数据库数据
截图
Allure 报告
Jenkins 日志
应用日志

Agentic QA 可以让 Agent 自动归因：

失败类型	可能原因
脚本问题	选择器失效、断言写错、等待不足
数据问题	前置数据不存在、状态不符合、脏数据
环境问题	服务不可用、网络超时、依赖异常
业务 Bug	返回值错误、状态流转错误、金额计算错误
第三方问题	支付、短信、OCR、风控服务异常
非稳定失败	flaky、偶发超时、并发冲突

输出可以是：

失败摘要
根因判断
证据链
影响范围
是否需要提 Bug
建议修复方向
是否建议重跑
场景 4：自愈测试维护

传统 UI 自动化最大痛点是：

前端页面一改，选择器就挂

Agentic QA 可以做：

识别元素变化
尝试替代定位方式
分析页面结构
更新 locator
判断是否为真实 Bug
标记高风险变更

BrowserStack 也把 self-healing、test selection、test deduplication、visual review 等作为 AI Agents 在测试生命周期中的具体能力。

不过要注意：自愈不等于永远正确。

比如按钮文案从“提交订单”变成“确认支付”，Agent 自动修了定位，但业务含义可能已经变了。这种场景仍然需要人审核。

场景 5：Agentic API Testing

输入：

OpenAPI/Swagger
接口文档
请求示例
数据库表结构
历史接口用例

Agent 自动生成：

正常参数用例
必填缺失用例
边界值用例
枚举值用例
权限用例
幂等性用例
并发用例
契约测试
接口断言
数据库断言

进一步可以做：

自动识别接口字段变化
判断是否破坏兼容性
生成差异测试
自动更新测试数据
场景 6：质量报告自动总结

Agent 可以读取：

测试计划
用例执行结果
Allure 报告
Jenkins 构建结果
缺陷列表
失败日志
历史趋势

然后输出：

本次测试结论
阻塞问题
高风险模块
失败用例归因
是否建议发布
需要产品/开发确认的问题
下一轮回归建议

这类能力对 QA Lead、测试经理、发布负责人非常有用。
5.3 AI / Agent 能力

这是新增部分。

能力	说明
Prompt Engineering	能稳定控制 AI 输出结构
Function Calling / Tool Calling	让模型调用工具、脚本、接口
RAG	让 Agent 基于项目文档、历史用例、缺陷记录回答
Agent Workflow	拆任务、规划、执行、观察、重试
Multi-Agent	不同 Agent 负责需求、用例、执行、分析
MCP	给 Agent 接入文件、Git、数据库、测试工具等能力
Evaluation	评估 AI 输出正确性和稳定性
Guardrails	限制 Agent 权限，防止危险操作
Observability for AI	记录 Agent 每一步输入、输出、工具调用、决策依据

6. Agentic QA 的典型架构

一个比较标准的 Agentic QA 系统可以长这样：

用户目标 / 需求 / PR / 缺陷
        ↓
Orchestrator 编排器
        ↓
┌──────────────────────────────┐
│ Requirement Agent             │
│ Test Design Agent             │
│ API Test Agent                │
│ UI Test Agent                 │
│ Data Agent                    │
│ Execution Agent               │
│ Failure Analysis Agent        │
│ Report Agent                  │
└──────────────────────────────┘
        ↓
工具层：
Git / Docs / DB / API / Pytest / Playwright / Jenkins / Allure / Logs
        ↓
结果层：
测试计划 / 测试用例 / 自动化脚本 / 失败分析 / 质量报告
        ↓
Human Review / Quality Gate

关键点是：Agent 不是一个“大模型聊天框”，而是一个能连接工具、执行任务、保留上下文、形成闭环的系统。


| 产出物             | 说明                    |
| --------------- | --------------------- |
| Agentic QA 工作流  | 从需求到报告的自动化闭环          |
| AI 测试 Prompt 模板 | 稳定生成测试点、用例、报告         |
| 测试知识库           | 业务规则、历史缺陷、接口规范、测试策略   |
| 自动化测试资产         | API/UI/数据校验/性能/安全用例   |
| 测试执行编排          | 哪些用例何时执行、失败后如何处理      |
| 失败分析机制          | 自动归因、证据链、重跑策略         |
| 质量门禁规则          | 哪些失败阻塞发布，哪些可豁免        |
| AI 评估体系         | 评估 Agent 输出质量、准确率、召回率 |
| 审计与追踪           | Agent 每一步为什么这么做，有证据可查 |
高级：Agentic QA Engineer
能做到：

设计多 Agent 测试工作流
让 Agent 根据目标规划测试
让 Agent 调用工具执行测试
让 Agent 分析失败并输出证据链
建立 AI 输出评估体系
建立权限与审计机制

关键词：

Agent Workflow
LangGraph
MCP
RAG
Evaluation
Guardrails

架构级：Agentic Quality Architect

能做到：

建设公司级 Agentic QA 体系
定义质量门禁
定义 AI 测试规范
设计测试知识库
治理测试资产
打通研发全流程质量数据
度量 AI 对质量效率的提升

关键词：

Quality Engineering
TestOps
AI Governance
Observability
Continuous Testing
Enterprise QA