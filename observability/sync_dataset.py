from __future__ import annotations

import os

from dotenv import load_dotenv
from langsmith import Client

from observability.dataset import DEFAULT_DATASET_NAME, load_evaluation_cases


def sync_dataset() -> None:
    load_dotenv(".env")
    dataset_name = os.getenv("LANGSMITH_DATASET", DEFAULT_DATASET_NAME)
    client = Client()
    dataset = _get_or_create_dataset(client, dataset_name)
    existing_case_ids = {
        example.metadata.get("case_id")
        for example in client.list_examples(dataset_id=dataset.id)
        if example.metadata
    }

    created = 0
    for case in load_evaluation_cases():
        if case.case_id in existing_case_ids:
            continue
        client.create_example(
            dataset_id=dataset.id,
            inputs=case.to_inputs(),
            outputs=case.to_outputs(),
            metadata={"case_id": case.case_id},
        )
        created += 1

    print(f"LangSmith dataset: {dataset_name}")
    print(f"Created examples: {created}")


def _get_or_create_dataset(client: Client, dataset_name: str):
    try:
        return client.read_dataset(dataset_name=dataset_name)
    except Exception:
        return client.create_dataset(
            dataset_name=dataset_name,
            description="LangSmith essentials observability evaluation dataset.",
        )


if __name__ == "__main__":
    sync_dataset()
