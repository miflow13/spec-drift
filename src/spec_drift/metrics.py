from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoreCard:
    feature_passed: int
    feature_total: int
    invariant_passed: int
    invariant_total: int

    @property
    def feature_success_rate(self) -> float:
        return self.feature_passed / self.feature_total if self.feature_total else 1.0

    @property
    def constraint_retention_rate(self) -> float:
        return self.invariant_passed / self.invariant_total if self.invariant_total else 1.0

    @property
    def spec_drift_rate(self) -> float:
        return 1.0 - self.constraint_retention_rate


def score_checks(feature_results: list[bool], invariant_results: list[bool]) -> ScoreCard:
    return ScoreCard(
        feature_passed=sum(feature_results),
        feature_total=len(feature_results),
        invariant_passed=sum(invariant_results),
        invariant_total=len(invariant_results),
    )
