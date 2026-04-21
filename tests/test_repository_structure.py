from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_core_root_files_exist() -> None:
    assert (ROOT / "README.md").exists()
    assert (ROOT / "AGENTS.md").exists()
    assert (ROOT / "conftest.py").exists()


def test_core_directories_exist() -> None:
    expected_dirs = (
        "agents",
        "standards",
        "skills",
        "templates",
        "references",
        "docs",
        "scripts",
        "src",
        "tests",
    )

    for directory in expected_dirs:
        assert (ROOT / directory).exists(), f"Missing directory: {directory}"


def test_core_agent_files_exist() -> None:
    agents_dir = ROOT / "agents"
    expected_files = (
        "senior_qa_agent.md",
        "requirement_analysis_agent.md",
        "test_design_agent.md",
        "api_test_agent.md",
        "ui_test_agent.md",
        "bug_analysis_agent.md",
        "regression_agent.md",
        "performance_stability_agent.md",
        "qa_architect_agent.md",
    )

    for filename in expected_files:
        assert (agents_dir / filename).exists(), f"Missing agent file: {filename}"


def test_core_standard_files_exist() -> None:
    standards_dir = ROOT / "standards"
    expected_files = (
        "output_standard.md",
        "test_case_standard.md",
        "bug_standard.md",
        "risk_standard.md",
        "review_standard.md",
    )

    for filename in expected_files:
        assert (standards_dir / filename).exists(), f"Missing standard file: {filename}"


def test_core_docs_exist() -> None:
    docs_dir = ROOT / "docs"
    expected_files = (
        "architecture-overview.md",
        "task-routing-matrix.md",
        "repository-roadmap.md",
    )

    for filename in expected_files:
        assert (docs_dir / filename).exists(), f"Missing docs file: {filename}"


def test_core_code_support_files_exist() -> None:
    assert (ROOT / "scripts" / "smoke_check.py").exists()
    assert (ROOT / "src" / "enterprise_ai_test_agents" / "__init__.py").exists()
    assert (ROOT / "src" / "enterprise_ai_test_agents" / "context.py").exists()
    assert (ROOT / "tests" / "test_context.py").exists()


def test_minimum_skill_files_exist() -> None:
    expected_skill_files = (
        ROOT / "skills" / "requirement-review" / "SKILL.md",
        ROOT / "skills" / "test-case-design" / "SKILL.md",
        ROOT / "skills" / "api-testing" / "SKILL.md",
        ROOT / "skills" / "log-analysis" / "SKILL.md",
    )

    for path in expected_skill_files:
        assert path.exists(), f"Missing skill file: {path}"


def test_minimum_template_files_exist() -> None:
    expected_template_files = (
        ROOT / "templates" / "test_case_template.md",
        ROOT / "templates" / "bug_report_template.md",
        ROOT / "templates" / "risk_assessment_template.md",
        ROOT / "templates" / "test_report_template.md",
    )

    for path in expected_template_files:
        assert path.exists(), f"Missing template file: {path}"


def test_minimum_reference_files_exist() -> None:
    expected_reference_files = (
        ROOT / "references" / "glossary.md",
        ROOT / "references" / "system_context.md",
        ROOT / "references" / "quality_baseline.md",
    )

    for path in expected_reference_files:
        assert path.exists(), f"Missing reference file: {path}"