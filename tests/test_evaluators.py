from observability.evaluators import category_match, minimum_quality_score, required_terms_present


def test_category_match() -> None:
    assert category_match({"category": "cost"}, {"expected_category": "cost"})


def test_required_terms_present() -> None:
    assert required_terms_present(
        {"response": "Track cost, token usage, and budget alerts."},
        {"required_terms": ["cost", "token", "budget"]},
    )


def test_minimum_quality_score() -> None:
    assert minimum_quality_score({"quality_score": 0.9})
    assert not minimum_quality_score({"quality_score": 0.5})
