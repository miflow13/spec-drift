from __future__ import annotations

import re

_CODE_BLOCK = re.compile(r"```python\s*(.*?)```", re.DOTALL | re.IGNORECASE)


class CodeExtractionError(ValueError):
    pass


def extract_python(response: str) -> str:
    matches = _CODE_BLOCK.findall(response)
    if len(matches) != 1:
        raise CodeExtractionError(
            f"Expected exactly one fenced Python block, found {len(matches)}."
        )
    code = matches[0].strip()
    if not code:
        raise CodeExtractionError("Python block was empty.")
    return code + "\n"
