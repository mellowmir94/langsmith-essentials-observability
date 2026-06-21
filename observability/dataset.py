from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DATASET_PATH = Path("data/evaluation_cases.json")
DEFAULT_DATASET_NAME = "agent-support-eval-v1"


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    user_input: str
    expected_category: str
    required_terms: list[str]

    def to_inputs(self) -> dict[str, str]:
        return {"user_input": self.user_input}

    def to_outputs(self) -> dict[str, Any]:
        return {
            "expected_category": self.expected_category,
            "required_terms": self.required_terms,
        }


def load_evaluation_cases(path: Path = DATASET_PATH) -> list[EvaluationCase]:
    raw_cases = json.loads(path.read_text(encoding="utf-8"))
    return [_parse_case(raw_case) for raw_case in raw_cases]


def _parse_case(raw_case: dict[str, Any]) -> EvaluationCase:
    return EvaluationCase(
        case_id=raw_case["case_id"],
        user_input=raw_case["user_input"],
        expected_category=raw_case["expected_category"],
        required_terms=raw_case["required_terms"],
    )
