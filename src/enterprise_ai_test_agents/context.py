from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True, slots=True)
class ArchitectureSnapshot:
    default_role: str = "senior-test-engineer"
    agent_count: int = 8
    skill_count: int = 8
    standard_count: int = 5
    routing_enabled: bool = True


def get_architecture_snapshot() -> dict[str, int | str]:
    return asdict(ArchitectureSnapshot())
