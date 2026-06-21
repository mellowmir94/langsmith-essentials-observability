from __future__ import annotations

from observability.agent import support_agent
from observability.dataset import load_evaluation_cases
from observability.evaluators import category_match, minimum_quality_score, required_terms_present


def run_monitoring_summary() -> str:
    cases = load_evaluation_cases()
    results = []

    for case in cases:
        output = support_agent(case.user_input)
        reference = case.to_outputs()
        passed = all(
            [
                category_match(output, reference),
                required_terms_present(output, reference),
                minimum_quality_score(output),
            ]
        )
        results.append((case.case_id, passed))

    passed_count = sum(1 for _, passed in results if passed)
    lines = [f"Monitoring summary: {passed_count}/{len(results)} cases passed"]
    lines.extend(f"- {'PASS' if passed else 'FAIL'} {case_id}" for case_id, passed in results)
    return "\n".join(lines)


def main() -> None:
    print(run_monitoring_summary())


if __name__ == "__main__":
    main()
