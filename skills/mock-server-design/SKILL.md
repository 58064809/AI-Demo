---
name: mock-server-design
description: API Mock 设计技能。用于需要快速构建模拟接口、隔离外部依赖、定义桩数据或设计最小可用 Mock 服务时。
---

# mock-server-design

设计 Mock 服务时，优先明确：

1. Mock 的目标是什么
2. 要隔离哪个外部依赖
3. 需要哪些典型响应
4. 需要哪些异常响应
5. 如何让 Mock 结果可重复、可维护

默认输出应包含：

- Mock 范围
- 路由定义
- 请求示例
- 响应示例
- 使用方式

