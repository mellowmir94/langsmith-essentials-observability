from __future__ import annotations

from dataclasses import dataclass

from langsmith import traceable


@dataclass(frozen=True)
class AgentResponse:
    response: str
    category: str
    quality_score: float


@traceable(name="support_agent", run_type="chain")
def support_agent(user_input: str) -> dict[str, str | float]:
    response = _generate_response(user_input)
    return {
        "response": response.response,
        "category": response.category,
        "quality_score": response.quality_score,
    }


def _generate_response(user_input: str) -> AgentResponse:
    normalized = user_input.lower()

    if "cost" in normalized or "token" in normalized:
        return AgentResponse(
            response=(
                "Problem: cost visibility is needed. Evidence: token usage can grow with "
                "agent traffic. Impact: spend may exceed budget without alerts. "
                "Recommended action: track input tokens, output tokens, and cost per run."
            ),
            category="cost",
            quality_score=0.92,
        )

    if "security" in normalized or "secret" in normalized:
        return AgentResponse(
            response=(
                "Problem: security monitoring is required. Evidence: agent prompts and outputs "
                "can accidentally expose secrets. Impact: leaked credentials create operational "
                "risk. Recommended action: scan traces for secret patterns and unsafe actions."
            ),
            category="security",
            quality_score=0.9,
        )

    if "quality" in normalized or "eval" in normalized:
        return AgentResponse(
            response=(
                "Problem: model quality can drift. Evidence: agent outputs are probabilistic "
                "and may miss required fields. Impact: users may receive weak recommendations. "
                "Recommended action: run evaluations against a dataset before changing prompts."
            ),
            category="quality",
            quality_score=0.91,
        )

    return AgentResponse(
        response=(
            "Problem: request needs triage. Evidence: no specific monitoring area was detected. "
            "Impact: unclear routing can slow incident response. Recommended action: classify "
            "the request as cost, quality, product analytics, or security."
        ),
        category="general",
        quality_score=0.82,
    )
