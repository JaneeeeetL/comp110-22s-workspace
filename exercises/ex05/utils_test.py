"""Test programs for ex05."""
__author__: str = "730401522"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item_odd() -> None:
    xs: list[int] = [1]
    assert only_evens(xs) == []


def test_only_evens_single_item_even() -> None:
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_multiple_items() -> None:
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_sub_empty() -> None:
    a_list: list[int] = []
    assert sub(a_list, 0, 0) == []


def test_sub_out_of_range_parameter_empty_list() -> None:
    a_list: list[int] = [1, 2, 3]
    assert sub(a_list, 4, -1) == []


def test_sub_out_of_range_parameter_corrected_range() -> None:
    a_list: list[int] = [1, 2, 3]
    assert sub(a_list, -1, 4)


def test_concat_empty() -> None:
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_run_single_element() -> None:
    list_one: list[int] = [1]
    list_two: list[int] = [2]
    assert concat(list_one, list_two) == [1, 2]


def test_concat_run_multiple_element() -> None:
    list_one: list[int] = [1, 2]
    list_two: list[int] = [2, 3]
    assert concat(list_one, list_two) == [1, 2, 2, 3]