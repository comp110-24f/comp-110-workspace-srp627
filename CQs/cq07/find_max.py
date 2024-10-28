__author__ = "730740670"
"""This program will write a function that modifies a list"""


def find_and_remove_max(input: list[int]) -> int:
    """Find, return, and remove the largest number in the input list."""

    if len(input) == 0:
        return -1

    max_value: int = 0
    index: int = 1
    # Setting max_value and index to different indexes ensure the same indexes aren't being compared

    while index < len(input):
        if input[index] > max_value:
            max_value = input[index]
        index += 1
    index = 0  # Reassigning the index to zero resets the index and allows the program to continue to the 2nd while loop
    # This while loop finds and returns the largest number in the list

    while index < len(input):
        if input[index] == max_value:
            input.pop(index)
        else:
            index += 1
    # This while loop removes every instance of the largest number from the list

    return max_value


# a: list[int] = []
# b: list[int] = [10, 9, 8, 7, 10]
# find_and_remove_max(input=b)
