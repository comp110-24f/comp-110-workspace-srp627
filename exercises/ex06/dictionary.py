___author__ = "730740670"
"""This program will create and use dictionary functions."""


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """This function will invert the keys and values to where the keys become the values of the output and vice versa."""
    duplicates: list[str] = []
    dict2: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in duplicates:
            raise KeyError("Cannot have multiple of the same key!")
        else:
            duplicates.append(dict1[key])  # Adds duplicate key to the duplicates list
    for item in dict1:
        dict2[(dict1[item])] = item  # Reassigns the value in dict2 to the item
    return dict2


# This function reverses the keys and values in the output


def favorite_color(input_colors: dict[str, str]) -> str:
    """This function will return the most popular color."""
    popular_color: dict[str, int] = {}

    for color in input_colors:
        if input_colors[color] in popular_color:
            popular_color[input_colors[color]] += 1
        # Continues to loop through popular_color
        else:
            popular_color[input_colors[color]] = 1
            # Reassigns the popular_color

    max_count = 0
    favorite = ""
    for color in popular_color:
        if popular_color[color] > max_count:
            max_count = popular_color[color]
            favorite = color
    return favorite


# If there is a tie for the most popular color this returns the color that appeared in the dictionary first
# This function returns the color that appers most in the dictionary


def count(input_values: list[str]) -> dict[str, int]:
    """This function will create a dictionary with the key being a value in the list and the intger being the number of times the value appeared in the list."""
    dict2: dict[str, int] = {}

    for value in input_values:
        if value in dict2:
            dict2[value] += 1  # Continues to loop through dict2
        else:
            dict2[value] = 1  # Reassigns dict2
    return dict2


# This function returns a dictionary with the value in the list as the key and the number of times it appered as the value.


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Produces a dictionary where the key is a letter and the valye is a list of words that begin with that letter."""
    categorize_words: dict[str, list[str]] = {}

    for x in words:
        first_letter = x[
            0
        ].lower()  # .lower() takes in no arguments and returns the lower cased string of a given string
        if first_letter in categorize_words:
            categorize_words[first_letter].append(x)  # Replaces the first letter with x
        else:
            categorize_words[first_letter] = [x]  # Sets the first letter to x
    return categorize_words


# Given a list of strings, this function categorizes them by their first letter


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """This function will mutate and return the attendance dictionary after given new attendance information."""
    if day in attendance:
        if student in attendance:
            attendance[day].append(
                student
            )  # Adds the student who attended to the attendance
    else:
        attendance[day] = [student]


# Given an attendance list for the days of the week, this function upadates the attendence at the days of the week students attend.
