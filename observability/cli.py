from __future__ import annotations

from observability.agent import support_agent


def main() -> None:
    result = support_agent("How should I monitor cost and token usage for an agent?")
    print(result["response"])


if __name__ == "__main__":
    main()
