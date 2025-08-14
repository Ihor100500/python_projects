from typing import Iterable


def normalize_spaces(s: str) -> str:
    return " ".join(s.split())


def sum_positive_integers(numbers: Iterable[int]) -> int:
    return sum(n for n in numbers if n > 0)
