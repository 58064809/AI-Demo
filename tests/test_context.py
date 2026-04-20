from src.enterprise_ai_test_agents.context import get_architecture_snapshot


def test_architecture_snapshot() -> None:
    snapshot = get_architecture_snapshot()

    assert snapshot["default_role"] == "senior-test-engineer"
    assert snapshot["agent_count"] == 8
    assert snapshot["skill_count"] == 8
    assert snapshot["standard_count"] == 5
    assert snapshot["routing_enabled"] is True
