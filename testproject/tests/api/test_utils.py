import pytest
from src.mytests.utils import normalize_spaces, sum_positive_integers


def test_normalize_spaces() -> None:
    assert normalize_spaces("  Hello   World  ") == "Hello World"
    assert normalize_spaces("NoSpaces") == "NoSpaces"
    assert normalize_spaces("  Multiple   Spaces   Here  ") == "Multiple Spaces Here"
    assert normalize_spaces("") == ""


def test_sum_positive_integers() -> None:
    assert sum_positive_integers([1, -2, 3, 4]) == 8
    assert sum_positive_integers([-1, -2, -3]) == 0
    assert sum_positive_integers([0, 0, 0]) == 0
    assert sum_positive_integers([]) == 0
    assert sum_positive_integers([5, 10, -5, 15]) == 30
    assert sum_positive_integers([1, 2, 3]) == 6


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("  Hello   World  ", "Hello World"),
        ("NoSpaces", "NoSpaces"),
        ("  Multiple   Spaces   Here  ", "Multiple Spaces Here"),
        ("", ""),
        ("    ", ""),
        ("  Leading and trailing spaces  ", "Leading and trailing spaces"),
    ],
)
def test_normalize_space_parametrized(raw: str, expected: str) -> None:
    assert normalize_spaces(raw) == expected
