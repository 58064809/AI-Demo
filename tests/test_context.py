from __future__ import annotations

from src.enterprise_ai_test_agents.context import (
    get_architecture_snapshot,
    is_architecture_ready,
)


def test_get_architecture_snapshot_returns_dict() -> None:
    snapshot = get_architecture_snapshot()

    assert isinstance(snapshot, dict)
    assert snapshot["project_name"] == "AI-Demo"
    assert snapshot["default_role"] == "资深测试工程师"


def test_snapshot_contains_core_counts() -> None:
    snapshot = get_architecture_snapshot()

    assert snapshot["agent_count"] >= 9
    assert snapshot["standard_count"] >= 5
    assert snapshot["skill_count"] >= 2
    assert snapshot["template_count"] >= 2
    assert snapshot["doc_count"] >= 3


def test_snapshot_contains_core_flags() -> None:
    snapshot = get_architecture_snapshot()

    assert snapshot["routing_enabled"] is True
    assert snapshot["architecture_layering_enabled"] is True
    assert snapshot["engineering_support_enabled"] is True


def test_snapshot_contains_primary_layers() -> None:
    snapshot = get_architecture_snapshot()

    assert "identity" in snapshot["primary_layers"]
    assert "role" in snapshot["primary_layers"]
    assert "standard" in snapshot["primary_layers"]
    assert "routing" in snapshot["primary_layers"]
    assert "execution_support" in snapshot["primary_layers"]


def test_snapshot_contains_primary_agents() -> None:
    snapshot = get_architecture_snapshot()

    assert "资深测试工程师代理" in snapshot["primary_agents"]
    assert "需求分析代理" in snapshot["primary_agents"]
    assert "测试设计代理" in snapshot["primary_agents"]
    assert "接口测试代理" in snapshot["primary_agents"]


def test_architecture_ready() -> None:
    assert is_architecture_ready() is True