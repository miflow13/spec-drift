from pathlib import Path


def save_report(path: str, content: str) -> None:
    target = Path(path)

    if target.exists():
        raise FileExistsError(path)

    target.write_text(content, encoding="utf-8")
