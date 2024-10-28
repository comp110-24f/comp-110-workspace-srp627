"""Summing the elements of a list using different loops"""

__author__ = "730740670"


def w_sum(vals: list[float]) -> float:
    """This function will add all the items in a list and return a float"""
    index: int = 0
    end_value: float = 0.0
    while index < len(vals):
        end_value += vals[index]
        index += 1
    if len(vals) == 0:
        return 0.0  # Returns 0 if the list is empty
    print(end_value)
    return end_value


# Purpose of end_value is to add each value one at a time
# This function adds the values in a list with a while loop
# Test with w_sum([1.1, 0.9, 1.0])


def f_sum(vals: list[float]) -> float:
    """This function will add the items in a list using a for...in... loop"""
    numbers: float = 0.0
    for num in vals:
        numbers += num
    print(numbers)
    return numbers


# Num and numbers must have differentiated names for code to run
# This function adds the numbers in a list using a for.. in... loop which iterates over the elements versus indexes


def f_range_sum(vals: list[float]) -> float:
    """This functipon adds the numbers in the list using the range() feature"""
    numbers: float = 0.0
    for index in range(0, len(vals)):
        numbers += vals[index]
    print(numbers)
    return numbers


# vals[index] ensures its not adding up the indexes but is adding the values in the list
# This function adds the values in a list using range() which iterates over each indexes
