from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.enterprise_ai_test_agents.context import get_architecture_snapshot, is_architecture_ready


def main() -> None:
    snapshot = get_architecture_snapshot()

    print("=== AI-Demo Architecture Smoke Check ===")
    print(f"project_name={snapshot['project_name']}")
    print(f"default_role={snapshot['default_role']}")
    print(f"agent_count={snapshot['agent_count']}")
    print(f"standard_count={snapshot['standard_count']}")
    print(f"skill_count={snapshot['skill_count']}")
    print(f"template_count={snapshot['template_count']}")
    print(f"doc_count={snapshot['doc_count']}")
    print(f"routing_enabled={snapshot['routing_enabled']}")
    print(f"architecture_layering_enabled={snapshot['architecture_layering_enabled']}")
    print(f"engineering_support_enabled={snapshot['engineering_support_enabled']}")
    print(f"architecture_ready={is_architecture_ready()}")


if __name__ == "__main__":
    main()