from __future__ import annotations

from typing import Any


def category_match(outputs: dict[str, Any], reference_outputs: dict[str, Any]) -> bool:
    return outputs.get("category") == reference_outputs.get("expected_category")


def required_terms_present(outputs: dict[str, Any], reference_outputs: dict[str, Any]) -> bool:
    response = str(outputs.get("response", "")).lower()
    required_terms = [str(term).lower() for term in reference_outputs.get("required_terms", [])]
    return all(term in response for term in required_terms)


def minimum_quality_score(outputs: dict[str, Any], minimum_score: float = 0.8) -> bool:
    return float(outputs.get("quality_score", 0)) >= minimum_score
