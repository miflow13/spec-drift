from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class Condition(StrEnum):
    STATED_ONCE = "stated_once"
    REINFORCED = "reinforced"


@dataclass(frozen=True)
class Turn:
    id: str
    request: str


@dataclass(frozen=True)
class Scenario:
    id: str
    title: str
    category: str
    target_file: str
    invariants: tuple[str, ...]
    turns: tuple[Turn, ...]
