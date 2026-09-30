import pytest

from spec_drift.extract import CodeExtractionError, extract_python


def test_extracts_one_python_block() -> None:
    assert extract_python("```python\nprint('ok')\n```") == "print('ok')\n"


def test_rejects_multiple_blocks() -> None:
    with pytest.raises(CodeExtractionError):
        extract_python("```python\na=1\n```\n```python\nb=2\n```")
