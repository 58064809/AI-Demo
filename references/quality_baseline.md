# 📏 Quality Baseline

---

## 🎯 Purpose

本文件用于定义本仓库默认采用的基础质量判断基线，帮助不同 Agent、不同 Standard、不同 Skill 和不同 Template 在输出质量结论、风险结论、测试结论和发布建议时，具备相对一致的底层参照。

它解决的问题包括：

- 什么样的状态可以被视为“基本可接受”
- 什么情况下不应轻易给出“可通过”或“可上线”结论
- 什么类型问题应被视为高敏感度问题
- 什么样的测试覆盖才算具备基本可信度
- 如何避免不同 Agent 在质量判断口径上出现明显偏差

本文件属于 `references/`，用于补充统一背景，不直接替代 `standards/` 的规则文件。

---

## 🧠 Baseline Principles

### 1. Quality Is Not “No Known Bug”

质量不是“当前没看到问题”或“当前没报错”，而是：

- 核心功能可用
- 关键规则正确
- 高风险场景有覆盖
- 高影响问题已识别
- 剩余风险已知且可接受

---

### 2. Core Flow First

默认情况下，核心业务链路必须优先满足质量要求。  
如果核心链路不稳定，其它边缘能力再完整，也不能视为整体质量达标。

---

### 3. Risk Awareness Matters More Than Surface Pass

一次执行通过，不等于质量稳定。  
如果：

- 测试覆盖明显不足
- 高风险区域未验证
- 规则缺失仍未澄清
- 环境或数据不可信

则不能因为“当前表面通过”就给出乐观结论。

---

### 4. Data / Permission / State Problems Are High Sensitivity Issues

默认情况下，以下类型问题属于高敏感度问题：

- 数据错误
- 数据不一致
- 权限异常
- 状态流转错误
- 关键链路失败
- 安全 / 合规相关异常

这些问题通常不能被轻易视为低风险。

---

### 5. Explicit Assumptions Are Better Than Implicit Optimism

如果结论依赖前提，应明确写出前提。  
本仓库默认不鼓励“看起来问题不大”“大概率可以上线”这种隐性乐观判断。

---

## ✅ Minimum Acceptable Quality Conditions

在默认情况下，一个版本、需求或功能要达到“基本可接受”状态，通常至少应满足以下条件：

### 1. Core Functional Availability

核心功能和核心业务链路必须可执行、可验证、结果正确。

例如：

- 登录
- 提交
- 查询
- 下单
- 支付
- 审批
- 发布
- 配置保存
- 核心状态流转

如果核心链路不可用，默认不满足质量基线。

---

### 2. Rule Correctness

关键业务规则必须明确且已按规则验证。  
至少不应出现：

- 主规则缺失
- 关键规则冲突
- 关键状态未定义
- 权限边界不清
- 成功 / 失败条件不明确

如果规则本身都不清，默认不应给出高置信度通过结论。

---

### 3. Basic Exception Coverage

不能只验证正常流程。  
至少应对以下内容具备基本覆盖：

- 关键异常路径
- 常见非法输入
- 关键边界条件
- 关键失败反馈
- 状态异常触发场景

如果异常路径完全未覆盖，质量判断默认应保守。

---

### 4. Data Consistency

页面、接口、数据库、缓存和下游结果之间，关键业务数据应保持一致。  
默认情况下，以下问题不应被视为可接受：

- 返回成功但数据未落库
- 页面展示与后台状态不一致
- 状态已更新但关联数据未同步
- 重复写入 / 漏写 / 脏数据无控制

---

### 5. Permission Correctness

不同角色的可见范围和可操作范围必须正确。  
默认情况下，以下问题不应被视为低风险：

- 越权访问
- 漏权导致功能不可用
- 错权导致角色能力错配
- 敏感数据误展示

---

### 6. Basic Recoverability and Observability

系统至少应具备基础可恢复性和可观测性：

- 问题出现后能发现
- 关键日志可定位
- 状态可观察
- 失败结果可识别
- 必要时可回退 / 重试 / 补偿

如果问题发生后既难发现又难定位，质量结论应更保守。

---

## ⚠️ High-Sensitivity Risk Types

默认情况下，以下问题类型应被优先视为高敏感度风险：

### 1. Core Flow Breakage

核心链路不可用、错误流转或结果错误。

### 2. Data Integrity Issues

涉及订单、库存、资金、资产、配置、报表、状态等关键数据错误。

### 3. Permission / Security Issues

涉及越权、错权、漏权、敏感功能暴露、敏感数据误展示。

### 4. State Machine Errors

涉及状态错乱、非法流转、重复触发、逆向触发、状态恢复异常。

### 5. Release-Critical Unknowns

临近发布时，关键规则仍未澄清、关键区域未验证、高风险问题未关闭。

### 6. Dependency and Stability Risks

依赖不稳定、重试放大、超时链路失控、长时间运行退化、日志与监控不足。

---

## 🧪 Baseline for Testing Completion

默认情况下，测试达到“基本完成”状态，不是指“所有内容都测了”，而通常至少意味着：

### 1. Core Coverage Exists

核心功能和核心链路已覆盖。

### 2. High-Risk Areas Are Addressed

高风险区域已验证，或已明确剩余风险并接受。

### 3. Critical Defects Are Resolved or Explicitly Accepted

P0 / P1 问题已关闭，或已有明确风险接受前提。

### 4. Regression Scope Is Reasonable

本次改动影响范围内的关键区域已完成回归验证。

### 5. Remaining Gaps Are Known

明确知道哪些没测、为什么没测、会带来什么风险。

---

## 📊 Baseline for Release Readiness

默认情况下，若要给出“可通过”或“可上线”结论，至少应满足以下思路：

### 可通过 / 可上线（默认前提）

通常应满足：

- 核心链路通过
- 高风险问题已关闭或明确接受
- 回归范围合理
- 剩余风险已知
- 测试结论具备依据

---

### 有条件通过

通常意味着：

- 整体可推进
- 但依赖特定前提成立
- 或存在少量已知风险需配套控制措施

例如：

- 限定灰度范围
- 增加监控
- 发布后重点观察
- 补回归
- 补日志 / 补告警

---

### 不建议通过

通常意味着：

- 核心链路存在明显问题
- 高风险问题未关闭
- 测试覆盖明显不足
- 关键规则仍未确认
- 剩余风险不可接受
- 发布后事故概率高且缺少兜底

---

## ❌ What Should Not Be Considered “Acceptable”

默认情况下，以下情况不应被直接视为“可接受质量状态”：

- 只测了主流程
- 只验证页面展示，不验证数据结果
- 只返回 200，不验证业务结果
- 有多个高风险未确认项，但仍直接建议上线
- 缺少测试范围边界说明
- 缺少风险说明
- 缺少核心问题结论
- 用“基本正常”“大概率没问题”替代正式结论

---

## 🧩 Relationship with Other Files

本文件通常作为背景基线，与以下文件共同作用：

- `standards/output_standard.md`
- `standards/bug_standard.md`
- `standards/risk_standard.md`
- `standards/review_standard.md`
- `templates/test_report_template.md`
- `templates/risk_assessment_template.md`

它不直接规定输出格式，但为这些文件提供一致的底层质量判断背景。

---

## 🚫 Non-Goals

本文件不负责：

- 定义某个具体业务线的详细验收标准
- 替代项目级发布规范
- 替代具体缺陷定级标准
- 给出某个版本的测试结论

如果未来需要面向特定领域（如电商、金融）定义更细质量基线，应在 `references/` 层补充领域化 baseline 文件。

---

## 🏁 Final Requirement

本文件的最终目标不是“制定一个绝对严格的质量教条”，而是：

> 为本仓库中的 Agent、Standard、Skill、Template 和后续工程化能力提供统一的默认质量判断基线，使整套测试 Agent 体系在输出测试结论、风险结论和发布建议时具备一致、稳健、可解释的底层参照。