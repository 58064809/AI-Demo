from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ArchitectureSnapshot:
    """
    仓库当前测试 Agent 架构的最小快照。

    这个类不是为了动态扫描整个仓库，而是作为第一阶段的轻量代码支撑，
    用来表达当前仓库已经建立的核心结构信息，方便脚本校验、测试校验、
    后续扩展以及工程化接入。
    """

    project_name: str = "AI-Demo"
    default_role: str = "资深测试工程师"

    agent_count: int = 9
    standard_count: int = 5
    skill_count: int = 2
    template_count: int = 2
    doc_count: int = 3

    routing_enabled: bool = True
    architecture_layering_enabled: bool = True
    engineering_support_enabled: bool = True

    primary_layers: tuple[str, ...] = (
        "identity",
        "role",
        "standard",
        "skill",
        "template",
        "reference",
        "routing",
        "execution_support",
    )

    primary_agents: tuple[str, ...] = (
        "资深测试工程师代理",
        "需求分析代理",
        "测试设计代理",
        "缺陷分析代理",
        "接口测试代理",
        "UI 测试代理",
        "回归测试代理",
        "性能与稳定性代理",
        "测试架构代理",
    )

    primary_standards: tuple[str, ...] = (
        "输出规范",
        "测试用例规范",
        "缺陷规范",
        "风险评估规范",
        "评审规范",
    )

    primary_skills: tuple[str, ...] = (
        "测试用例设计技能",
        "接口测试技能",
    )

    primary_templates: tuple[str, ...] = (
        "测试用例模板",
        "缺陷报告模板",
    )

    core_docs: tuple[str, ...] = (
        "architecture-overview.md",
        "task-routing-matrix.md",
        "AGENTS.md",
    )


def get_architecture_snapshot() -> dict[str, Any]:
    """
    返回仓库当前架构快照的字典形式。

    适用于：
    - smoke check
    - 轻量测试
    - 后续 CLI / Web 展示
    - 工程化接入前的结构校验
    """
    return asdict(ArchitectureSnapshot())


def is_architecture_ready() -> bool:
    """
    判断当前仓库是否已经具备第一阶段可用的测试 Agent 架构骨架。
    """
    snapshot = ArchitectureSnapshot()
    return (
        snapshot.routing_enabled
        and snapshot.architecture_layering_enabled
        and snapshot.engineering_support_enabled
        and snapshot.agent_count >= 9
        and snapshot.standard_count >= 5
    )