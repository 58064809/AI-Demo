from __future__ import annotations


def get_architecture_snapshot() -> dict[str, int | str]:
    return {
        "default_role": "senior-qa-agent",
        "agent_count": 9,
        "skill_count": 8,
        "standard_count": 5,
    }
