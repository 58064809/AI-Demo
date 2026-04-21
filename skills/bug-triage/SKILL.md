# 🛠️ Skill Name

缺陷分级与归因技能

---

## 🎯 Purpose

本技能用于定义缺陷分级、缺陷归因、缺陷处置判断和缺陷流转分析的具体处理方法，帮助 Agent 在面对测试发现的问题、线上故障、联调异常和回归失败时，能够以结构化、系统化、可复用的方式完成高质量 Bug Triage。

它解决的问题不是“给 Bug 随手定个级”，而是：

- 如何判断问题严重程度
- 如何区分问题归属和影响范围
- 如何识别是否阻塞上线
- 如何把问题从“一个现象”转成“一个可处理的质量项”
- 如何让缺陷流转、回归和质量决策更一致

---

## 🧠 Core Principles

### 1. Impact Before Emotion

缺陷分级要看业务影响、用户影响、数据影响和恢复成本，而不是看主观感受。

### 2. Fact Before Blame

先确认问题事实、复现条件和影响范围，再讨论归因，不做情绪化归责。

### 3. Severity vs Priority Separation

严重程度描述问题本身的影响级别，优先级描述处理顺序。  
两者相关，但不能完全混同。

### 4. Scope Awareness

Bug Triage 不只是给一个问题打标签，而是要判断它影响到哪些用户、角色、功能、链路和后续测试范围。

### 5. Decision Support

缺陷分级和归因的最终目标是支持修复决策、上线判断、回归策略和质量治理。

---

## 📦 Applicable Scenarios

本技能适用于但不限于以下场景：

- 测试发现 Bug 后的分级判断
- 线上问题的初步归因
- 发布前缺陷评估
- 回归失败问题判断
- 联调阶段问题归因
- 版本评审中的问题梳理
- 缺陷复盘与质量分析

---

## 🔍 Input Requirements

开始 Bug Triage 前，尽量先明确以下输入：

- 问题现象是什么
- 如何复现
- 出现频率如何
- 影响哪些用户 / 角色 / 场景
- 是否影响核心业务链路
- 是否影响资金、订单、库存、权限、安全、数据正确性
- 是否有临时绕过方案
- 是否已有日志、截图、链路信息、数据库证据
- 当前是否临近发布或已经线上

如果上述信息不完整，应先明确“已知事实”和“待确认项”。

---

## 🧩 Standard Triage Process

### Step 1：Clarify the Problem

先明确问题本身：

- 是功能错误
- 是展示错误
- 是权限问题
- 是状态错乱
- 是数据不一致
- 是性能问题
- 是稳定性问题
- 是环境或依赖问题

不要在问题类型都不清时直接定级。

---

### Step 2：Assess User and Business Impact

判断：

- 影响多少用户
- 影响哪些角色
- 是否影响核心功能
- 是否影响关键业务链路
- 是否造成直接业务损失
- 是否影响数据正确性或安全性

---

### Step 3：Assess Recoverability and Workaround

判断：

- 用户是否可绕过
- 绕过后是否有副作用
- 是否需要人工补偿 / 修数 / 手工干预
- 是否会持续扩大影响

---

### Step 4：Determine Severity

默认建议按以下等级判断：

- P0：系统不可用 / 核心业务中断 / 严重数据或安全问题
- P1：核心功能严重异常 / 高影响问题
- P2：一般功能异常 / 局部高影响或可控问题
- P3：低影响问题 / 展示或体验问题

必须说明定级依据，不可只给结论。

---

### Step 5：Determine Likely Ownership and Cause Direction

区分：

- 前端表现问题
- 后端逻辑问题
- 接口契约问题
- 数据问题
- 配置问题
- 环境问题
- 外部依赖问题
- 可观测性不足问题

这里强调“方向判断”，不是要求一次性完全坐实根因。

---

### Step 6：Decide Release Impact

判断：

- 是否阻塞上线
- 是否可带风险上线
- 是否需要灰度
- 是否必须补测 / 补回归 / 补监控
- 是否需要升级风险等级

---

## 📌 Default Triage Checklist

### 1. Problem Type

- 问题属于哪一类
- 是稳定复现还是偶发
- 是单点还是系统性问题

### 2. Impact Scope

- 影响用户范围
- 影响角色范围
- 影响功能范围
- 影响业务范围
- 是否影响核心链路

### 3. Data / Security / Permission Sensitivity

- 是否影响关键数据
- 是否有越权风险
- 是否影响安全或合规
- 是否可能导致资金 / 库存 / 订单错误

### 4. Workaround

- 是否可绕过
- 绕过成本是否高
- 绕过后是否仍有副作用

### 5. Release Risk

- 是否临近发布
- 是否影响发布目标
- 是否已知有同类历史问题
- 是否需要升级为风险项

### 6. Test Follow-up

- 是否需要补测
- 是否需要补自动化
- 是否需要扩大回归范围
- 是否需要增加日志 / 监控 / 告警

---

## 🧪 Triage Strategies by Scenario

### 1. For Functional Bugs

重点关注：

- 是否影响主流程
- 是否影响规则正确性
- 是否可稳定复现
- 是否会扩展到同类功能

### 2. For UI / Display Bugs

重点关注：

- 是否只是展示问题
- 是否误导用户操作
- 是否影响可用性
- 是否与权限 / 数据错误有关

### 3. For Data Bugs

重点关注：

- 是否产生错误数据
- 是否可恢复
- 是否需要修数
- 是否影响历史数据和后续流程

### 4. For Permission / Security Bugs

重点关注：

- 是否有越权 / 漏权 / 错权
- 是否影响敏感功能
- 是否需要快速升级等级和风险提示

### 5. For Release-Critical Bugs

重点关注：

- 是否阻塞上线
- 是否有合理风险接受条件
- 是否必须补回归 / 补监控 / 补灰度方案

---

## 📝 Output Guidance

最终输出时，应遵守：

- `standards/output_standard.md`
- `standards/bug_standard.md`
- `standards/risk_standard.md`

建议输出结构包括：

- 问题概述
- 已知事实
- 严重程度建议
- 定级依据
- 影响范围
- 初步归因方向
- 是否阻塞上线
- 建议动作

---

## 🚫 Common Mistakes

缺陷分级与归因时，必须避免以下问题：

- 只看表面现象，不看影响范围
- 根据情绪而不是依据定级
- 把严重程度和处理优先级混为一谈
- 问题未确认就直接甩锅
- 忽略数据和权限类问题的高敏感性
- 只说问题严重，不说为什么严重
- 不说明上线影响和后续动作

---

## ✅ Good Output Characteristics

高质量 Bug Triage 通常具备以下特征：

- 问题类型清晰
- 影响范围清晰
- 定级依据清晰
- 已知与推断边界清晰
- 上线影响清晰
- 后续建议明确
- 能直接支撑修复、回归和质量决策

---

## 🤝 Relationship with Other Files

本技能通常与以下文件配合使用：

- 角色定义 → `agents/bug_analysis_agent.md`
- 通用输出要求 → `standards/output_standard.md`
- 缺陷规范 → `standards/bug_standard.md`
- 风险评估规范 → `standards/risk_standard.md`
- 缺陷报告模板 → `templates/bug_report_template.md`

在以下场景中也常与其它文件联动：

- 补测设计 → `agents/test_design_agent.md`
- 接口问题归因 → `agents/api_test_agent.md`
- 上线判断与回归评估 → `agents/regression_agent.md`

---

## 🏁 Final Requirement

本技能的最终目标不是“给 Bug 打个标签”，而是：

> 让缺陷分级与归因具备统一口径、明确依据和可执行结论，帮助团队更准确地处理问题、更合理地安排优先级，并更有效地支持上线决策和质量治理。