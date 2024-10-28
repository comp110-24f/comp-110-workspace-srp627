__author__ = "730740670"

"""This program will test my functions with unit tests."""

from exercises.ex05.utils import only_evens, sub, add_at_index, pytest


def test_only_evens_return() -> None:
    """Tests only_evens with a use case."""
    assert only_evens([2, 3, 7, 8]) == [2, 8]


# Returns expected value


def test_only_evens_mutate() -> None:
    """Mutates the input of only_evens and tests it."""
    my_list: list[int] = [2, 9, 0, 3]
    my_list.append(4)
    assert only_evens(my_list) == [2, 0, 4]


# Mutates the input in the expected way


def test_only_evens_edge() -> None:
    """Tests only_evens with an edge case."""
    assert only_evens([1, 3, 5]) == []


# Returns the correct value in case of an unconventional input


def test_sub_return() -> None:
    """Tests sub with a use case."""
    assert sub([5, 6, 7, 8], 0, 3) == [5, 6, 7]


# Returns expected value


def test_sub_mutate() -> None:
    """Mutates the input of sub and tests it."""
    my_list: list[int] = [2, 4, 6, 8]
    my_list.append(9)
    assert sub(my_list, 1, 3) == [4, 6]


# Mutates the input in the expected way


def test_sub_edge() -> None:
    """Tests sub with an edge case."""
    assert sub([], 0, 2) == []


# Returns the correct value in case of an unconventional input


def test_add_at_index_return() -> None:
    """Tests add_at_index with a use case."""
    list_1 = [1, 3]
    assert add_at_index(list_1, 2, 1) == None


# Returns expected value


def test_add_at_index_mutate() -> None:
    """ "Mutates the input of add_at_index and tests it."""
    list_1: list[int] = [8, 9, 10, 12]
    list_1.append(11)
    assert add_at_index(list_1, 11, 3) == None


# Mutates the input in the expected way


def test_add_at_index_edge():
    """Test that add_at_index raises an IndexError for an invalid index."""
    list_1: list[int] = []

    with pytest.raises(IndexError):
        add_at_index(list_1, 3, 1)


# Index is out of bounds for the input list
# Pytest is used to test that a function raises an index error
# Returns the correct value in case of an unconventional input
