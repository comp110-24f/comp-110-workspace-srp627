"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730740670"


def main() -> None:
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


# Overarching function that acts as a summary


def input_word() -> str:
    """This function will gather input from the user"""
    word_choice: str = input("Enter a 5-character word: ")
    if len(word_choice) == 5:
        return word_choice
    else:
        print("Error: Word must contain 5 characters.")
        exit()


# exit() makes the code stop if theres an error
# len counts the length of a word


def input_letter() -> str:
    """This function will gather a letter for the user"""
    letter_choice: str = input("Enter a single character: ")
    if len(letter_choice) == 1:
        return letter_choice
    else:
        print("Error: Character must be a single character.")
        exit()


# Asking the user for a letter


def contains_char(word: str, letter: str) -> None:
    """This function will determine at which indexes a letter appears."""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    index: int = 0
    # count: int = 0 and index: int = 0 ensures counting starts at index 0
    # Determines at what indicies a letter appears

    while len(word) > index:
        if word[index] == letter:
            count = count + 1
            print(letter + " found at index " + str(index))
        index = index + 1
    # index = index + 1 allows the function to continue going through letters and not stop at the next letter

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# Prints weather or not the letter appears

if __name__ == "__main__":
    main()
