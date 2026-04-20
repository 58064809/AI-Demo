from src.enterprise_ai_test_agents.context import get_architecture_snapshot


def test_architecture_snapshot() -> None:
    snapshot = get_architecture_snapshot()

    assert snapshot["default_role"] == "senior-qa-agent"
    assert snapshot["agent_count"] == 9
    assert snapshot["skill_count"] == 8
    assert snapshot["standard_count"] == 5
