from pathlib import Path

from solution import save_report


def test_final_behavior_still_writes_new_file(tmp_path: Path) -> None:
    target = tmp_path / "nested" / "final.txt"
    save_report(str(target), "final", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == "final"
