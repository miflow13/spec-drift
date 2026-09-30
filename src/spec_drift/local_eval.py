from __future__ import annotations

import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TestRun:
    passed: bool
    returncode: int
    output: str


def run_pytest_for_code(
    scenario_dir: str | Path,
    code: str,
    test_files: list[str],
    *,
    timeout_seconds: int = 15,
) -> TestRun:
    """Execute one candidate in an isolated temporary directory.

    This helper is intended for trusted benchmark development fixtures. Model-produced
    code should be executed only in an appropriately sandboxed environment.
    """
    scenario_dir = Path(scenario_dir)
    with tempfile.TemporaryDirectory(prefix="spec-drift-") as tmp:
        work = Path(tmp)
        (work / "solution.py").write_text(code, encoding="utf-8")
        tests_dir = work / "tests"
        tests_dir.mkdir()
        for name in test_files:
            shutil.copy2(scenario_dir / "tests" / name, tests_dir / name)

        proc = subprocess.run(
            ["python", "-m", "pytest", "-q", str(tests_dir)],
            cwd=work,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
        output = proc.stdout + proc.stderr
        return TestRun(passed=proc.returncode == 0, returncode=proc.returncode, output=output)
