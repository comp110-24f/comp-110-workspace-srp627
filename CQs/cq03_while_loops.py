"""This function will use a while string to iterate over a string."""

__author__ = "730740670"


def num_instances(phrase: str, search_char: str) -> int:
    """This function should return the count of occurances of search_char in phrase"""
    count: int = 0
    index: int = 0
    while len(phrase) > index:
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    print(count)
    return count


# count: int = 0 tells the computer to start counting at index 0
# count + 1 and index + 1 countinues the loop instead of stopping at 2

num_instances(phrase="HelloHelloHello", search_char="e")
