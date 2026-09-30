from pathlib import Path

import pytest

from solution import save_report


def test_existing_file_is_never_overwritten(tmp_path: Path) -> None:
    target = tmp_path / "report.txt"
    target.write_text("original", encoding="utf-8")

    with pytest.raises(FileExistsError):
        save_report(str(target), "replacement")

    assert target.read_text(encoding="utf-8") == "original"
