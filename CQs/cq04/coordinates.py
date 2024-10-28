"""Function will print formatted pairs of each character input"""

__author__ = "730740670"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0
    while index < len(xs):
        idx: int = 0
        while idx < len(ys):
            print("(" + xs[index] + "," + ys[idx] + ")")
            idx += 1
            index += 1


# The outer while loop is used to iterate over the letters in xs and the inner while loop iterates over the letters in ys
# This is called a nested while loop

get_coords("hi", "bye")
