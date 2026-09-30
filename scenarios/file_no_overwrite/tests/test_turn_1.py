from pathlib import Path

from solution import save_report


def test_missing_parent_directories_are_created(tmp_path: Path) -> None:
    target = tmp_path / "one" / "two" / "report.txt"
    save_report(str(target), "hello")
    assert target.read_text(encoding="utf-8") == "hello"
