__author__ = "730740670"
"""This program will test my functions defined in find_max using unit tests."""

from find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    """Tests find_and_remove_max with a use case."""
    assert find_and_remove_max(input=[7, 8, 4, 3]) == 8


# Returns expected value


def test_find_and_remove_max_mutate() -> None:
    """Mutates the input of find_and_remove_max and tests it."""
    input = [2, 4, 6, 8]
    input.append(1)
    assert find_and_remove_max(input) == 8


# Mutates the input in the expected way


def test_find_and_remove_max_edge() -> None:
    """Tests find_and remove_max with an edge case."""
    assert find_and_remove_max(input=[]) == -1


# Returns the correct value in case of an unconventional input
