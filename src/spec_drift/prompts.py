from __future__ import annotations

from .models import Condition, Scenario, Turn


OUTPUT_RULE = """Return the complete updated contents of the target Python file in exactly one fenced ```python code block. Do not return a diff."""


def initial_prompt(scenario: Scenario, starter_code: str) -> str:
    invariants = "\n".join(f"- {item}" for item in scenario.invariants)
    return f"""You are modifying an existing Python program over several turns.

NON-NEGOTIABLE REQUIREMENTS:
{invariants}

Preserve these requirements during every future modification in this conversation.

Target file: {scenario.target_file}

Current code:
```python
{starter_code.rstrip()}
```

{OUTPUT_RULE}
"""


def turn_prompt(scenario: Scenario, turn: Turn, condition: Condition) -> str:
    reminder = ""
    if condition is Condition.REINFORCED:
        invariants = "\n".join(f"- {item}" for item in scenario.invariants)
        reminder = f"\nThe non-negotiable requirements still apply:\n{invariants}\n"

    return f"""Implement this next change:

{turn.request}
{reminder}
{OUTPUT_RULE}
"""
