from pathlib import Path

from spec_drift.local_eval import run_pytest_for_code


ROOT = Path(__file__).resolve().parents[1]
SCENARIO_DIR = ROOT / "scenarios" / "file_no_overwrite"
STARTER = (SCENARIO_DIR / "starter.py").read_text(encoding="utf-8")


def test_starter_preserves_invariant() -> None:
    run = run_pytest_for_code(
        SCENARIO_DIR,
        STARTER,
        ["test_invariants.py"],
    )
    assert run.passed, run.output
