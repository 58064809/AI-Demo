from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.enterprise_ai_test_agents.context import get_architecture_snapshot


def main() -> None:
    snapshot = get_architecture_snapshot()
    print(snapshot)


if __name__ == "__main__":
    main()
