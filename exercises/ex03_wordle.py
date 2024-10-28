"""This program will prompt the user for a 5 character word and respomd accordingly"""

__author__ = "730740670"


def input_guess(user_guess: int) -> str:
    secret_word_len: str = input(
        "Enter a " + str(user_guess) + " character word: "
    )  # The input function prompts the user with a question to answer in the REPL
    while len(secret_word_len) != user_guess:
        secret_word_len = input(f"That wasn't {user_guess} chars! Try again: ")

    return secret_word_len


# This function tests if the length of guessed word is equal to the length of the word the user is trying to guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Function will test each index of the first parameter string to see if it matches
    the second parameter"""
    assert len(char_guess) == 1
    index: int = 0

    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False

    # This function goes through each character of the secret word to see if any characters match the character guessed


def emojified(guess: str, secret: str) -> str:
    """This function returns a green, yellow, or white emoji depending on the letter
    and its placement"""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    index: int = 0

    emojified_str: str = ""
    # emojified_str allows the emojis to appear in the terminal one after another
    # assigning a blank string allows emojis to be added to the string
    while index < len(secret):
        if guess[index] == secret[index]:
            index += 1
            emojified_str += green_box

        elif contains_char(secret, guess[index]):
            index += 1
            emojified_str += yellow_box
        # Contains_char results in a boolean vlaue and therefore must do the same inside emojified

        else:
            index += 1
            emojified_str += white_box

    return emojified_str


# emojified retruns emojis based on placement of the letters in the guessed word - this function resembles the game wordle


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turns = (
        1  # Setting turns to 1 ensures the function prints try 1/6 instead of try 0/6
    )
    max_turns = 6
    won = False

    while (
        turns <= max_turns and not won
    ):  # <= ensures the function runs through 6 turns instead of stopping at 5 with only <
        print(
            f"=== Turn {turns}/{max_turns} ===="
        )  # f-strings are used for better formatting
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)
        # Instead of X/6 the code should be able to run as if 6 could vary -> max_turns
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


# The main function incorporates all of the other defined functions to run the game
# The main function takes the secret word as input, tracks the number of turns taken by the user, determines if the user has won or lost, and manages the flow of the game

if __name__ == "__main__":
    main(secret="codes")
