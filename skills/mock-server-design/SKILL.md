# 🛠️ Skill Name

Mock 服务设计技能

---

## 🎯 Purpose

本技能用于定义 Mock 服务设计、依赖隔离、联调替身构建和测试桩设计的具体处理方法，帮助 Agent 在面对外部依赖不稳定、接口未完成、测试数据难准备、联调受阻或异常场景难以制造时，能够以结构化、系统化、可复用的方式完成高质量 Mock 设计。

它解决的问题不是“随便返回一段假数据”，而是：

- 如何为测试提供稳定、可控、可重复的依赖替身
- 如何隔离外部系统不稳定带来的干扰
- 如何模拟成功、失败、超时、空返回、脏数据等复杂场景
- 如何让 Mock 服务既便于联调，也服务于测试设计和自动化
- 如何避免 Mock 与真实接口契约长期偏离

---

## 🧠 Core Principles

### 1. Contract Alignment First

Mock 设计必须首先与真实接口契约保持一致。  
如果 Mock 脱离真实契约，只会制造伪通过和错误联调结论。

### 2. Test Purpose Driven

Mock 不是为了“看起来能跑”，而是为了支持明确的测试目标，例如：

- 联调推进
- 依赖隔离
- 异常场景制造
- 自动化稳定性提升
- 测试数据可控化

### 3. Deterministic over Randomness

默认优先设计可重复、可预测、可配置的 Mock 行为，而不是随机返回结果。

### 4. Scenario-Based Simulation

Mock 不能只支持 happy path，还应支持失败、超时、限流、空值、错误码、状态冲突等测试场景。

### 5. Maintainable and Traceable

Mock 行为必须可理解、可配置、可维护，并尽量标明与真实接口的对应关系和偏差边界。

---

## 📦 Applicable Scenarios

本技能适用于但不限于以下场景：

- 外部依赖未完成时的联调替代
- 第三方服务不稳定时的测试隔离
- 难以制造的异常场景模拟
- 自动化测试中的依赖替身
- 复杂测试数据准备中的接口返回控制
- 上下游联调节奏不一致时的并行推进
- 接口回归测试中的可控假服务设计

---

## 🔍 Input Requirements

开始设计 Mock 服务前，尽量先明确以下输入：

- 真实接口路径是什么
- 请求方法是什么
- 输入输出契约是什么
- 成功场景返回是什么
- 失败场景返回是什么
- 是否存在状态机或前后依赖
- 是否存在分页、筛选、排序、幂等、鉴权等规则
- Mock 的使用目标是什么
- Mock 是给谁用（测试、开发、联调、自动化）
- 是否允许与真实环境混用

如果上述信息不完整，应先明确待确认项。

---

## 🧩 Standard Design Process

### Step 1：Clarify Mock Objective

先明确本次 Mock 的主要目标：

- 联调占位
- 测试隔离
- 异常模拟
- 自动化支持
- 压测 / 稳定性测试前置准备
- 数据构造辅助

不同目标决定 Mock 的复杂度和设计重点。

---

### Step 2：Identify Real Contract

梳理真实接口契约，包括：

- 路径
- 方法
- 请求参数
- 响应结构
- 字段语义
- 状态码 / 错误码
- 鉴权要求
- 状态依赖
- 调用顺序依赖

如果真实接口契约本身不清晰，应优先记录偏差风险。

---

### Step 3：Define Supported Scenarios

明确 Mock 至少要支持哪些场景，例如：

- 正常返回
- 参数校验失败
- 鉴权失败
- 业务规则失败
- 空结果
- 超时
- 下游错误
- 状态冲突
- 分页结果
- 特定条件下的特殊返回

不能只做单一成功返回。

---

### Step 4：Design Configuration Strategy

尽量明确 Mock 行为如何切换，例如：

- 固定场景切换参数
- Header 控制
- Query 参数控制
- 路径控制
- 环境变量控制
- 配置文件控制

目标是让场景切换可控，而不是靠手工改代码。

---

### Step 5：Define Data and State Handling

明确 Mock 是否需要支持：

- 固定静态返回
- 条件返回
- 简单内存态状态流转
- 基于输入参数决定结果
- 多次调用返回不同结果
- 失败后恢复
- 列表 / 详情联动

如果任务需要验证状态流转，静态返回往往不够。

---

### Step 6：Document Deviations and Limits

任何 Mock 都可能与真实系统存在差异。  
必须明确：

- 哪些部分是严格对齐真实契约的
- 哪些部分是简化实现
- 哪些部分当前未模拟
- 使用该 Mock 时有哪些风险和限制

---

## 📌 Default Design Checklist

设计 Mock 服务时，默认优先检查以下内容：

### 1. Contract Consistency

- 路径是否一致
- 方法是否一致
- 参数位置是否一致
- 字段名是否一致
- 返回结构是否一致
- 状态码 / 错误码是否一致

### 2. Scenario Coverage

- 是否支持成功场景
- 是否支持失败场景
- 是否支持异常场景
- 是否支持边界场景
- 是否支持关键业务规则场景

### 3. Configurability

- 是否便于切换场景
- 是否便于不同测试人员使用
- 是否便于自动化接入
- 是否避免每次改代码才能切换结果

### 4. State Awareness

- 是否需要模拟状态流转
- 是否需要模拟重复调用差异
- 是否需要模拟前后调用依赖
- 是否需要模拟异步完成前后的结果差异

### 5. Error Simulation

- 是否支持错误码模拟
- 是否支持超时
- 是否支持空返回
- 是否支持格式异常
- 是否支持第三方失败
- 是否支持慢响应

### 6. Usage Boundaries

- 适合哪些测试场景
- 不适合哪些验证
- 是否可能掩盖真实问题
- 是否会让联调结果过度乐观

---

## 🧪 Design Strategies by Scenario

### 1. For API Early Integration

重点关注：

- 基本契约一致
- 常用成功 / 失败场景可切换
- 足够支撑前后端并行联调

### 2. For Automated Testing

重点关注：

- 返回可预测
- 场景可配置
- 稳定性高
- 易于脚本调用
- 易于重置状态

### 3. For Exception Simulation

重点关注：

- 错误码模拟
- 超时模拟
- 空数据模拟
- 数据脏值模拟
- 状态冲突模拟

### 4. For Workflow Testing

重点关注：

- 多接口联动
- 状态推进
- 前后依赖
- 多次调用结果差异
- 回退 / 重试后的结果

### 5. For Third-Party Dependency Isolation

重点关注：

- 契约对齐
- 可用性高
- 不受外部环境影响
- 可快速切换真实 / mock 依赖

---

## 📝 Output Guidance

最终输出时，应尽量包含以下内容：

- Mock 目标
- 对应真实接口
- 支持场景
- 配置方式
- 返回规则
- 状态处理方式
- 已知限制
- 使用建议

如需输出更规范交付内容，可配合：

- `templates/api_mock_spec_template.md`（后续若补充）
- `standards/output_standard.md`

---

## 🚫 Common Mistakes

设计 Mock 服务时，必须避免以下问题：

- 只返回固定成功数据，不支持异常场景
- Mock 契约与真实接口明显不一致
- 不说明简化点和限制
- 场景切换只能靠手改代码
- 只适合一次联调，不适合重复使用
- Mock 掩盖了真实依赖风险，却没有任何提示
- 不考虑自动化使用场景
- 不考虑状态流转和多次调用差异

---

## ✅ Good Output Characteristics

高质量 Mock 设计通常具备以下特征：

- 契约一致性清晰
- 目标场景清晰
- 场景切换方式清晰
- 已知限制清晰
- 便于联调
- 便于自动化
- 便于异常模拟
- 便于后续维护和扩展

---

## 🤝 Relationship with Other Files

本技能通常与以下文件配合使用：

- 角色定义 → `agents/api_test_agent.md`
- 测试架构规划 → `agents/qa_architect_agent.md`
- 通用输出要求 → `standards/output_standard.md`
- 测试用例规范 → `standards/test_case_standard.md`

在以下场景中也常与其它文件联动：

- 接口测试设计 → `skills/api-testing/SKILL.md`
- 测试数据准备 → `skills/test-data-building/SKILL.md`（后续补充）
- 测试计划和联调说明 → `templates/test_plan_template.md`

---

## 🏁 Final Requirement

本技能的最终目标不是“造一个假的接口”，而是：

> 让 Mock 服务设计具备契约意识、场景意识、配置意识和边界意识，能够真实支撑联调、测试、自动化和依赖隔离，并成为可长期复用的测试资产。