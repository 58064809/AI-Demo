from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True, slots=True)
class ArchitectureSnapshot:
    """
    仓库当前测试 Agent 架构的动态快照。

    这版快照会根据当前仓库目录自动统计核心文件数量，
    用于支撑脚本校验、测试校验、后续工程化扩展和仓库状态感知。
    """

    project_name: str
    default_role: str

    agent_count: int
    standard_count: int
    skill_count: int
    template_count: int
    doc_count: int

    routing_enabled: bool
    architecture_layering_enabled: bool
    engineering_support_enabled: bool

    primary_layers: tuple[str, ...]
    primary_agents: tuple[str, ...]
    primary_standards: tuple[str, ...]
    primary_skills: tuple[str, ...]
    primary_templates: tuple[str, ...]
    core_docs: tuple[str, ...]


def _count_markdown_files(directory: Path) -> int:
    if not directory.exists() or not directory.is_dir():
        return 0
    return sum(1 for path in directory.rglob("*.md") if path.is_file())


def _count_skill_files(directory: Path) -> int:
    if not directory.exists() or not directory.is_dir():
        return 0
    return sum(1 for path in directory.rglob("SKILL.md") if path.is_file())


def _build_snapshot() -> ArchitectureSnapshot:
    agents_dir = ROOT / "agents"
    standards_dir = ROOT / "standards"
    skills_dir = ROOT / "skills"
    templates_dir = ROOT / "templates"
    docs_dir = ROOT / "docs"

    primary_agents = (
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

    primary_standards = (
        "输出规范",
        "测试用例规范",
        "缺陷规范",
        "风险评估规范",
        "评审规范",
    )

    primary_skills = (
        "测试用例设计技能",
        "接口测试技能",
        "需求评审技能",
    )

    primary_templates = (
        "测试用例模板",
        "缺陷报告模板",
        "风险评估模板",
    )

    core_docs = (
        "architecture-overview.md",
        "task-routing-matrix.md",
        "AGENTS.md",
    )

    return ArchitectureSnapshot(
        project_name="AI-Demo",
        default_role="资深测试工程师",
        agent_count=_count_markdown_files(agents_dir),
        standard_count=_count_markdown_files(standards_dir),
        skill_count=_count_skill_files(skills_dir),
        template_count=_count_markdown_files(templates_dir),
        doc_count=_count_markdown_files(docs_dir),
        routing_enabled=(docs_dir / "task-routing-matrix.md").exists(),
        architecture_layering_enabled=all(
            (ROOT / name).exists()
            for name in ("agents", "standards", "skills", "templates", "docs")
        ),
        engineering_support_enabled=all(
            (ROOT / name).exists()
            for name in ("src", "scripts", "tests")
        ),
        primary_layers=(
            "identity",
            "role",
            "standard",
            "skill",
            "template",
            "reference",
            "routing",
            "execution_support",
        ),
        primary_agents=primary_agents,
        primary_standards=primary_standards,
        primary_skills=primary_skills,
        primary_templates=primary_templates,
        core_docs=core_docs,
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
    return asdict(_build_snapshot())


def is_architecture_ready() -> bool:
    """
    判断当前仓库是否已经具备第一阶段可用的测试 Agent 架构骨架。
    """
    snapshot = _build_snapshot()
    return (
        snapshot.routing_enabled
        and snapshot.architecture_layering_enabled
        and snapshot.engineering_support_enabled
        and snapshot.agent_count >= 9
        and snapshot.standard_count >= 5
        and snapshot.skill_count >= 3
        and snapshot.template_count >= 3
        and snapshot.doc_count >= 2
    )