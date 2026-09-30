from __future__ import annotations

import json
from pathlib import Path

from .models import Scenario, Turn


def load_scenario(path: str | Path) -> Scenario:
    scenario_dir = Path(path)
    data = json.loads((scenario_dir / "scenario.json").read_text(encoding="utf-8"))
    return Scenario(
        id=data["id"],
        title=data["title"],
        category=data["category"],
        target_file=data["target_file"],
        invariants=tuple(data["invariants"]),
        turns=tuple(Turn(id=t["id"], request=t["request"]) for t in data["turns"]),
    )
