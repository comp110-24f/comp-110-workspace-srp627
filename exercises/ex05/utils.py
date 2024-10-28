"""This program will modify lists using their utility functions."""

__author__ = "730740670"


def only_evens(input: list[int]) -> list[int]:
    """This function returns the even numbers present in a list."""
    index: int = 0
    list_2: list[int] = []
    while index < len(input):
        if input[index] % 2 == 0:  # Even numbers have a remainder (modulo) of 0
            list_2.append(input[index])
        index += 1
    return list_2


# This function returns the even numbers in a list by looping through each index and testing if the remainder is 0


def sub(input: list[int], start_index: int, end_index: int) -> list[int]:
    """This function generates a list that is a subset of the input list between the start and end index"""
    new_list: list[int] = []

    if start_index < 0:
        start_index = 0
    if end_index > len(input):
        end_index = len(input)
    if len(input) == 0:
        return new_list
    if start_index >= len(input):
        return new_list
    if end_index <= 0:
        print(new_list)
        return new_list
    else:
        for x in range(start_index, end_index):
            new_list.append(input[x])
    return new_list


# Must use if statements instead of elif because multiple of the if statements can be true
# This function returns the values at the indicies specified (start index to end index)

# a_list = [10, 20, 30, 40]
# print(sub(a_list, -1, 6))


def add_at_index(input: list[int], element: int, index: int) -> None:
    """ "This function modifys the input list to place the element at a given index."""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(element)  # Adds element to the end of the list

    for x in range(
        len(input) - 1, index, -1
    ):  # The -1 causes the loop to start from the end of the list
        input[x] = input[x - 1]
    input[index] = element


# This function adds an integer to the list and places it in chronological order
