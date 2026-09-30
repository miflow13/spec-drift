from pathlib import Path

from spec_drift.loader import load_scenario
from spec_drift.models import Condition
from spec_drift.prompts import turn_prompt


ROOT = Path(__file__).resolve().parents[1]
SCENARIO = load_scenario(ROOT / "scenarios" / "file_no_overwrite")


def test_stated_once_does_not_repeat_invariant() -> None:
    prompt = turn_prompt(SCENARIO, SCENARIO.turns[0], Condition.STATED_ONCE)
    assert "never overwrite" not in prompt.lower()


def test_reinforced_repeats_invariant() -> None:
    prompt = turn_prompt(SCENARIO, SCENARIO.turns[0], Condition.REINFORCED)
    assert "never overwrite" in prompt.lower()
