# 架构概览

本仓库采用“测试子 Agent + 可复用 Skill + 共享 Standard + 模板 + 参考资料”的分层结构。

## 分层说明

- Agent 层：定义测试任务场景下的专业分身
- Skill 层：定义可复用能力
- Standard 层：定义共享规范
- Template 层：定义交付模板
- Reference 层：定义背景资料

## 推荐协作流

1. 先判断当前任务最适合由哪个测试子 Agent 处理
2. 参考 `task-routing-matrix.md` 补充对应的 Standard
3. 如果涉及具体能力，再加载相关 Skill
4. 如果需要固定输出结构，再读取 Template
5. 如果需要背景资料，再读取 Reference
