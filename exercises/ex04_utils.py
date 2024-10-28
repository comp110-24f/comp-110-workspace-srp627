"""This program will"""

__author__ = "730740670"


def all(a: list[int], b: int) -> bool:
    index: int = 0

    if len(a) == 0:
        return False
    while index < len(a):
        if a[index] != b:
            return False
        index += 1

    return True


# Assigning every possible answer to a bool fixes the error under the return type bool
# This function returns True if every number in the list is equal to the number assigned


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    max_value: int = 0

    while index < len(input):
        if input[index] > input[max_value]:
            max_value = index
        index += 1

    return input[max_value]


# This function looops through each index and returns the largest value
# The function holds the max_value and compars it to the proceeding indexes


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    if len(list_1) != len(list_2):
        return False
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True


# This function loops through each index and determines if they are the same
# Two empty lists are technically the same


def extend(list_1: list[int], list_2: list[int]) -> None:
    for element in list_2:
        list_1.append(element)


# Using append instead of adding the lists ensures the new list is pointing to list_1
# This function combines two lists into one
