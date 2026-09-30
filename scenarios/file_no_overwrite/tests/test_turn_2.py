from pathlib import Path

from solution import save_report


def test_custom_encoding_is_supported(tmp_path: Path) -> None:
    target = tmp_path / "report.txt"
    save_report(str(target), "caf\u00e9", encoding="utf-16")
    assert target.read_text(encoding="utf-16") == "caf\u00e9"


def test_utf8_remains_default(tmp_path: Path) -> None:
    target = tmp_path / "default.txt"
    save_report(str(target), "snowman: \u2603")
    assert target.read_text(encoding="utf-8") == "snowman: \u2603"
