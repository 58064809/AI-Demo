# 企业级 AI 测试 Agent 架构

这是一个偏企业级的 AI 测试 Agent 仓库骨架，目标不是直接产出某个单一工具，而是先搭好一套可长期扩展的测试协作体系。

核心结构分为五层：

- `agents/`：测试子 Agent，解决“当前由哪种测试思维处理”
- `skills/`：能力定义，解决“具体如何处理”
- `standards/`：共享规范，解决“按什么标准处理”
- `templates/`：输出模板，解决“以什么格式交付”
- `references/`：参考资料，解决“需要查什么背景信息”

同时补充了 `docs/task-routing-matrix.md`，用于定义任务如何路由到合适的 Agent、Standard 和 Skill。

## 目录结构

```text
AGENTS.md
agents/
standards/
skills/
templates/
references/
docs/
scripts/
src/
tests/
```

## 当前定位

- 以测试领域为主轴
- 保留向爬虫、API Mock、小工具、质量平台等方向扩展的空间
- 默认协作者身份是资深测试工程师
- 多个 Agent 是同一名测试工程师在不同任务场景下的专业分身
- 默认全部内容以中文为主，必要时保留英文技术术语

## 快速校验

```bash
python scripts/smoke_check.py
pytest
```

## 后续扩展建议

1. 继续补充 `agents/`，完善测试任务分工和协作流转
2. 继续补充 `skills/`，把常见能力沉淀成可复用技能
3. 在 `standards/` 中加入团队自己的规范和质量红线
4. 在 `templates/` 中加入实际会反复使用的交付模板
5. 在 `references/` 中加入业务背景、系统说明和环境资料
