"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, is_equal, last, value_at, max, linkify, scale

__author__ = "730401522"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """An edge case occurs when the list is empty. Raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at_index_zero() -> None:
    """An edge case occurs when the list's index is 0. Here you should return the data of the current Node being processed on the list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_max_empty() -> None:
    """An edge case occurs when the list is empty. Raise an IndexError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_same() -> None:
    """An edge case occurs when the list's items are all the same value. The returned value should be the repeated value in the list."""
    linked_list = Node(10, Node(10, Node(10, None)))
    assert max(linked_list) == 10


def test_linkify_empty() -> None:
    """An edge case occurs when the list is empty. Returns None."""
    items: list[int] = []
    assert linkify(items) is None


def test_linkify_example() -> None:
    """An example case occurs when the Node object is [1, 2, 3]. Returns an linked list."""
    items: list[int] = [1, 2, 3]
    assert is_equal(linkify(items), Node(1, Node(2, Node(3, None))))


def test_scale_empty() -> None:
    """An edge case occurs when the list is empty. Returns None."""
    head: Node = None
    factor: int = 1
    assert scale(head, factor) is None


def test_scale_example() -> None:
    """An example case occurs when the Node object is [2, 4, 6]. Returns an linked list."""
    head: Node = Node(1, Node(2, Node(3, None)))
    factor: int = 2
    assert is_equal(scale(head, factor), Node(2, Node(4, Node(6, None))))