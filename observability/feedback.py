from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeedbackRecord:
    run_id: str
    score: int
    comment: str


def classify_feedback(record: FeedbackRecord) -> str:
    if record.score >= 4:
        return "positive"
    if record.score <= 2:
        return "negative"
    return "neutral"


def summarize_feedback(records: list[FeedbackRecord]) -> dict[str, int]:
    summary = {"positive": 0, "neutral": 0, "negative": 0}
    for record in records:
        summary[classify_feedback(record)] += 1
    return summary
