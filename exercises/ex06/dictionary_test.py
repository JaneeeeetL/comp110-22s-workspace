"""Tests for ex06 -- dictionary utilities."""
__author__: str = "730401522"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Test for invert."""
    a: dict[str, str]
    a = {}
    assert invert(a) == {}


def test_invert_single_entry() -> None:
    """Test for invert."""
    a: dict[str, str]
    a = {"1": "2"}
    assert invert(a) == {"2": "1"}


def test_favorite_color_empty() -> None:
    """Test for favortie_color."""
    b: dict[str, str]
    b = {}
    assert favorite_color(b) == ""


def test_favorite_color_one_color() -> None:
    """Test for favorite_color."""
    b: dict[str, str]
    b = {"Michael": "White"}
    assert favorite_color(b) == "White"


def test_favorite_color__multiple_color() -> None:
    """Test for favorite_color."""
    b: dict[str, str]
    b = {"Michael": "White", "Janet": "Blue", "Nathan": "Pink"}
    assert favorite_color(b) == "White"


def test_count_empty() -> None:
    """Test for count."""
    c: list[str] = list()
    assert count(c) == {}


def test_count_multiple_items() -> None:
    """Test for count."""
    c: list[str] = list()
    c.append("1")
    c.append("1")
    c.append("1")
    c.append("2")
    assert count(c) == {"1": 3, "2": 1}


def test_count_multiple_items_again() -> None:
    """Test for count."""
    c: list[str] = list()
    c.append("Janet")
    c.append("loves")
    c.append("Nathan")
    c.append("!")
    assert count(c) == {"Janet": 1, "loves": 1, "Nathan": 1, "!": 1}