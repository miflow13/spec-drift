from spec_drift.metrics import score_checks


def test_metrics() -> None:
    score = score_checks([True, True, False], [True, False, False, True])
    assert score.feature_success_rate == 2 / 3
    assert score.constraint_retention_rate == 0.5
    assert score.spec_drift_rate == 0.5
