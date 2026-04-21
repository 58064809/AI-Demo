# 🛠️ Skill Name

日志分析技能

---

## 🎯 Purpose

本技能用于定义日志分析、异常定位、故障排查和问题归因的具体处理方法，帮助 Agent 在面对应用日志、接口日志、链路日志、任务日志、错误堆栈和运行时异常信息时，能够以结构化、系统化、可复用的方式完成高质量分析。

它解决的问题不是“看几行报错”，而是：

- 如何从日志中快速提取有效线索
- 如何区分表象异常和真实根因
- 如何结合上下文缩小排查范围
- 如何把日志分析结果转化为缺陷判断、风险判断和补测建议
- 如何避免只盯单条报错而忽略整条调用链和上下游影响

---

## 🧠 Core Principles

### 1. Context Before Conclusion

先理解日志产生的上下文，再下结论。  
日志分析不能只看某一行报错，要结合时间、链路、输入、状态和前后事件一起判断。

### 2. Fact Before Inference

先提取已知事实，再做合理推断。  
不能把猜测直接当成根因结论。

### 3. Chain-Oriented Analysis

日志问题往往不在报错位置本身，而在整条链路中的上游输入、下游依赖、状态冲突或重试放大中。

### 4. Symptom vs Root Cause Separation

必须区分：

- 表面现象
- 触发点
- 传播路径
- 可能根因
- 已确认根因

### 5. Actionable Output

日志分析结果必须能支持后续动作，例如：

- 缺陷归因
- 补测建议
- 监控补强
- 日志补充
- 代码排查方向
- 风险升级判断

---

## 📦 Applicable Scenarios

本技能适用于但不限于以下场景：

- 接口报错排查
- 页面异常对应服务端问题定位
- 自动化测试失败排查
- 联调问题定位
- 上线后异常日志分析
- 性能与稳定性问题日志排查
- 定时任务 / 异步任务异常定位
- 缺陷复盘中的日志归因分析

---

## 🔍 Input Requirements

开始日志分析前，尽量先明确以下输入：

- 问题现象是什么
- 问题发生时间范围是什么
- 涉及哪个环境
- 涉及哪个用户 / 角色 / 请求 / 任务
- 涉及哪个接口 / 页面 / 服务 / 链路
- 是否有 requestId / traceId / orderId / userId / taskId 等关键标识
- 是否有复现步骤
- 是否有相关上下游日志
- 是否有错误码、异常堆栈、监控告警、数据库结果等辅助信息

如果缺少关键上下文，必须先标记待确认项。

---

## 🧩 Standard Analysis Process

### Step 1：Clarify the Problem Statement

先明确当前要解决的问题：

- 是报错问题
- 是超时问题
- 是数据不一致问题
- 是状态错乱问题
- 是异步任务失败问题
- 是偶发异常还是稳定复现问题

不要在问题对象不清时直接开始扫日志。

---

### Step 2：Locate the Time Window and Trace Context

优先锁定：

- 问题发生时间窗口
- 关键 traceId / requestId / userId / orderId / taskId
- 所属服务 / 模块 / 接口 / 页面 / 任务名称

如果没有这些关键标识，必须先寻找可用的关联字段。

---

### Step 3：Extract Observable Facts

先提取已知事实，包括：

- 报错信息
- 异常类型
- 状态码 / 错误码
- 执行路径
- 入参片段
- 关键状态值
- 调用顺序
- 重试次数
- 超时点
- 成功 / 失败分支

这一阶段只提事实，不急着下结论。

---

### Step 4：Build the Event Chain

把日志按链路组织起来，重点关注：

- 请求进入点
- 关键处理节点
- 状态变化节点
- 异常抛出点
- 重试与回滚
- 下游依赖调用
- 最终结果

目标是还原“发生了什么”。

---

### Step 5：Separate Symptom, Trigger, and Cause

明确区分：

- 表面现象是什么
- 触发动作是什么
- 问题在哪个环节首次出现
- 问题是本系统产生还是外部依赖传入
- 当前是怀疑原因还是已验证原因

---

### Step 6：Assess Scope and Risk

结合日志判断：

- 是单点问题还是系统性问题
- 是局部请求异常还是整类链路异常
- 是否影响核心业务
- 是否有扩散风险
- 是否会重复发生
- 是否需要升级问题等级

---

### Step 7：Form Actionable Output

最终输出至少应支持以下其中一项：

- 缺陷分析
- 排查建议
- 补测建议
- 日志补强建议
- 监控补强建议
- 风险评估结论

---

## 📌 Default Analysis Checklist

分析日志时，默认优先检查以下内容：

### 1. Time and Context

- 问题发生时间是否明确
- 日志时间是否连续
- 是否存在跨时区 / 延迟写入问题
- 是否能关联到唯一请求或任务

### 2. Request and Input

- 请求参数是否异常
- 参数缺失 / 格式错误 / 空值是否可见
- 是否存在非法组合输入
- 是否存在前端入参与服务端处理不一致

### 3. Status and State

- 问题发生前系统状态是什么
- 状态是否按预期流转
- 是否存在非法状态进入
- 是否有重复触发 / 状态竞争

### 4. Exception and Stack Trace

- 异常类型是什么
- 报错位置在哪里
- 报错是首次根因还是二次包装异常
- 是否存在被吞掉的异常 / 泛化异常信息

### 5. Dependency Calls

- 是否调用了外部系统
- 外部依赖是否超时 / 空返回 / 错误返回
- 上下游是否有对应异常日志
- 是否存在依赖失败放大问题

### 6. Retry / Timeout / Concurrency

- 是否发生重试
- 重试是否改变了结果
- 是否发生超时
- 是否存在并发争抢、锁等待、重复请求

### 7. Data and Consistency

- 日志中是否能看出数据写入结果
- 是否存在“返回成功但数据未落库”
- 是否存在“状态已变但响应未同步”
- 是否存在缓存 / 数据库 / 下游结果不一致

### 8. Observability Gaps

- 是否缺关键字段
- 是否缺 traceId / requestId
- 是否缺状态日志
- 是否缺输入输出摘要
- 是否难以定位链路节点

---

## 🧪 Analysis Strategies by Scenario

### 1. For API Error Logs

重点关注：

- 请求参数
- 状态码 / 错误码
- 业务异常 vs 系统异常
- 下游依赖调用
- 返回结果与实际数据结果是否一致

### 2. For UI-Triggered Backend Issues

重点关注：

- 页面操作时间
- 接口触发链路
- 页面提示与接口结果是否一致
- 是否是前端参数问题还是后端处理问题

### 3. For Async Task Logs

重点关注：

- 任务触发源
- 入队 / 出队是否正常
- 消费是否成功
- 重试次数
- 失败后补偿 / 回滚 / 告警是否存在

### 4. For Stability / Performance Logs

重点关注：

- 慢日志
- 超时日志
- 线程池 / 连接池 / 队列状态
- 重试风暴
- 资源耗尽信号
- 依赖雪崩迹象

### 5. For Automated Test Failure Logs

重点关注：

- 用例输入
- 失败步骤
- 接口返回
- 页面状态
- 是否是环境问题 / 数据问题 / 代码问题 / 脚本问题
- 是否为偶发失败或真实缺陷

---

## 📝 Output Guidance

最终输出时，应遵守：

- `standards/output_standard.md`
- `standards/bug_standard.md`
- `standards/risk_standard.md`

推荐输出结构包括：

- 问题概述
- 已知事实
- 关键日志线索
- 事件链路
- 可能原因
- 已确认 / 待确认项
- 影响范围
- 建议动作

---

## 🚫 Common Mistakes

日志分析时，必须避免以下问题：

- 只看最后一条报错，不看前序链路
- 把包装异常当根因
- 把猜测直接写成结论
- 没有时间窗口和唯一标识就盲目搜索
- 只看本服务，不看上下游依赖
- 只说“日志报错了”，不说明报错含义
- 不区分真实缺陷、环境问题、数据问题和观察性不足问题
- 不输出下一步排查方向

---

## ✅ Good Output Characteristics

高质量日志分析通常具备以下特征：

- 时间窗口清晰
- 链路上下文清晰
- 已知事实和推断边界清晰
- 问题传播路径清晰
- 风险影响判断清晰
- 下一步动作明确
- 能直接支持缺陷分析、补测设计和监控补强

---

## 🤝 Relationship with Other Files

本技能通常与以下文件配合使用：

- 缺陷分析 → `agents/bug_analysis_agent.md`
- 性能与稳定性分析 → `agents/performance_stability_agent.md`
- 通用输出要求 → `standards/output_standard.md`
- 缺陷规范 → `standards/bug_standard.md`
- 风险评估规范 → `standards/risk_standard.md`

在以下场景中也常与其它文件联动：

- 接口问题分析 → `agents/api_test_agent.md`
- 缺陷补测 → `agents/test_design_agent.md`
- 回归风险评估 → `agents/regression_agent.md`

---

## 🏁 Final Requirement

本技能的最终目标不是“从日志里找一条报错”，而是：

> 让日志分析具备清晰方法、链路意识、事实边界和可执行输出，帮助团队更快定位问题、更准确识别风险，并为缺陷修复、测试补强和质量治理提供高价值输入。