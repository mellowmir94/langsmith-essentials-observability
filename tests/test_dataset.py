from observability.dataset import load_evaluation_cases


def test_load_evaluation_cases() -> None:
    cases = load_evaluation_cases()

    assert len(cases) == 3
    assert cases[0].case_id == "cost_monitoring"
    assert cases[0].expected_category == "cost"
