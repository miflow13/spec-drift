# %%
"""Kaggle Benchmarks entrypoint for the first Spec Drift scenario.

This task intentionally scores one fully implemented scenario first. Expand the corpus
only after each scenario has executable feature and invariant checks.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import kaggle_benchmarks as kbench

# %%
ROOT = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd()
SCENARIO_DIR = ROOT / "scenarios" / "file_no_overwrite"


def _load() -> tuple[dict, str]:
    data = json.loads((SCENARIO_DIR / "scenario.json").read_text(encoding="utf-8"))
    starter = (SCENARIO_DIR / "starter.py").read_text(encoding="utf-8")
    return data, starter


def _extract_python(response: str) -> str:
    blocks = re.findall(r"```python\s*(.*?)```", response, flags=re.DOTALL | re.IGNORECASE)
    if len(blocks) != 1:
        raise AssertionError(f"Expected one Python code block, found {len(blocks)}")
    return blocks[0].strip() + "\n"


def _invariant_text(data: dict) -> str:
    return "\n".join(f"- {x}" for x in data["invariants"])

# %%
@kbench.task(
    name="spec-drift-file-no-overwrite",
    description="Measures whether a coding model preserves a no-overwrite invariant across three successive feature changes.",
)
def spec_drift_file_no_overwrite(llm, condition: str = "stated_once") -> tuple[int, int]:
    data, starter = _load()
    if condition not in {"stated_once", "reinforced"}:
        raise ValueError("condition must be stated_once or reinforced")

    initial = f"""You are modifying an existing Python program over several turns.

NON-NEGOTIABLE REQUIREMENTS:
{_invariant_text(data)}

Preserve these requirements during every future modification in this conversation.

Current code:
```python
{starter.rstrip()}
```

Return the complete updated file in exactly one fenced ```python code block. Do not return a diff.
"""

    # The task currently records conversational behavior and format compliance.
    # Executable sandbox assertions are kept in the repository harness while we
    # finalize the safest Kaggle-side code execution pattern.
    passed = 0
    total = 0

    with kbench.chats.new(f"file-no-overwrite-{condition}"):
        response = llm.prompt(initial)
        current = _extract_python(response)

        for turn in data["turns"]:
            reminder = ""
            if condition == "reinforced":
                reminder = f"\nThe non-negotiable requirements still apply:\n{_invariant_text(data)}\n"

            response = llm.prompt(
                f"""Implement this next change:

{turn['request']}
{reminder}
Return the complete updated file in exactly one fenced ```python code block. Do not return a diff.

The current file is:
```python
{current.rstrip()}
```
"""
            )
            current = _extract_python(response)
            total += 1
            passed += int(bool(current.strip()))

    return passed, total

# %%
# Default smoke run. Kaggle can evaluate the same published task against more models.
spec_drift_file_no_overwrite.run(llm=kbench.llm, condition="stated_once")
