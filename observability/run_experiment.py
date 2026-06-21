from __future__ import annotations

import os

from dotenv import load_dotenv
from langsmith import evaluate

from observability.agent import support_agent
from observability.dataset import DEFAULT_DATASET_NAME
from observability.evaluators import category_match, required_terms_present


def target(inputs: dict) -> dict:
    return support_agent(str(inputs["user_input"]))


def main() -> None:
    load_dotenv(".env")
    dataset_name = os.getenv("LANGSMITH_DATASET", DEFAULT_DATASET_NAME)
    evaluate(
        target,
        data=dataset_name,
        evaluators=[category_match, required_terms_present],
        experiment_prefix="langsmith-essentials",
        description="LangSmith essentials experiment with deterministic support agent.",
        max_concurrency=1,
    )


if __name__ == "__main__":
    main()
