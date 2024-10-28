"""Mutating functions."""

__author__ = "730740670"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)
    print(a)
    a = [1, 2, 3]


# This function mutates its input by appending b to the end of list a


def double(c: list[int]) -> None:
    idx: int = 0
    my_list: list[int] = []
    while idx < len(c):
        my_list.append(c[idx] * 2)
        idx += 1
        print(my_list)


# Must name my_list verus list for python to read the code
# This function mutates its input by looping through the list and multiply every element in list c by 2
# The purpose of my_list is to print the output one after another in a sequence

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
