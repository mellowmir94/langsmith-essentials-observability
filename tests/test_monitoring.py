from observability.monitoring import run_monitoring_summary


def test_run_monitoring_summary_passes_dataset() -> None:
    summary = run_monitoring_summary()

    assert "Monitoring summary: 3/3 cases passed" in summary
    assert "PASS cost_monitoring" in summary
