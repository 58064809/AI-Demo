from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.enterprise_ai_test_agents.context import get_architecture_snapshot, is_architecture_ready


def _print_section(title: str) -> None:
    print()
    print(f"=== {title} ===")


def main() -> None:
    snapshot = get_architecture_snapshot()

    _print_section("Repository Audit Summary")
    print(f"project_name: {snapshot['project_name']}")
    print(f"default_role: {snapshot['default_role']}")
    print(f"architecture_ready: {is_architecture_ready()}")

    _print_section("Counts")
    print(f"agents: {snapshot['agent_count']}")
    print(f"standards: {snapshot['standard_count']}")
    print(f"skills: {snapshot['skill_count']}")
    print(f"templates: {snapshot['template_count']}")
    print(f"docs: {snapshot['doc_count']}")

    _print_section("Core Flags")
    print(f"routing_enabled: {snapshot['routing_enabled']}")
    print(f"architecture_layering_enabled: {snapshot['architecture_layering_enabled']}")
    print(f"engineering_support_enabled: {snapshot['engineering_support_enabled']}")

    _print_section("Primary Layers")
    for item in snapshot["primary_layers"]:
        print(f"- {item}")

    _print_section("Primary Agents")
    for item in snapshot["primary_agents"]:
        print(f"- {item}")

    _print_section("Primary Standards")
    for item in snapshot["primary_standards"]:
        print(f"- {item}")

    _print_section("Primary Skills")
    for item in snapshot["primary_skills"]:
        print(f"- {item}")

    _print_section("Primary Templates")
    for item in snapshot["primary_templates"]:
        print(f"- {item}")

    _print_section("Core Docs")
    for item in snapshot["core_docs"]:
        print(f"- {item}")

    _print_section("Baseline Checks")
    warnings: list[str] = []

    if snapshot["agent_count"] < 9:
        warnings.append("Agent 数量低于预期最小值（9）")
    if snapshot["standard_count"] < 5:
        warnings.append("Standard 数量低于预期最小值（5）")
    if snapshot["skill_count"] < 4:
        warnings.append("Skill 数量低于当前推荐最小值（4）")
    if snapshot["template_count"] < 4:
        warnings.append("Template 数量低于当前推荐最小值（4）")
    if snapshot["doc_count"] < 3:
        warnings.append("Docs 数量低于当前推荐最小值（3）")

    if warnings:
        print("status: NEEDS_ATTENTION")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("status: HEALTHY")


if __name__ == "__main__":
    main()