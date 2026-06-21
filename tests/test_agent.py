from observability.agent import support_agent


def test_support_agent_routes_cost_question() -> None:
    output = support_agent("How do I monitor cost and token usage?")

    assert output["category"] == "cost"
    assert output["quality_score"] >= 0.8
    assert "token" in str(output["response"]).lower()
