from __future__ import annotations

import json
import os

from dotenv import load_dotenv

from observability.fleet_agent import fleet_meta_ads_agent


def main() -> None:
    load_dotenv(".env")
    os.environ.setdefault("LANGSMITH_PROJECT", "langsmith-essentials-observability")

    result = fleet_meta_ads_agent(
        {
            "spend": 100,
            "leads": 5,
            "clicks": 80,
            "impressions": 4000,
        }
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
