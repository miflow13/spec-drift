from pathlib import Path

from spec_drift.loader import load_scenario
from spec_drift.models import Condition
from spec_drift.prompts import initial_prompt, turn_prompt


root = Path(__file__).resolve().parents[1]
scenario_dir = root / "scenarios" / "file_no_overwrite"
scenario = load_scenario(scenario_dir)
starter = (scenario_dir / "starter.py").read_text(encoding="utf-8")

print("=== INITIAL ===")
print(initial_prompt(scenario, starter))
for condition in Condition:
    print(f"\n=== {condition.value.upper()} ===")
    for turn in scenario.turns:
        print(turn_prompt(scenario, turn, condition))
