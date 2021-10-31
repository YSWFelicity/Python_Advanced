'''
Yingshu Wang
CS5001 Fall 2021
Create a simple hangman game.
'''


def main():
    MAX_GUESSES = 6
    word_list = ['APPLE', 'OBVIOUS', 'XYLOPHONE']
    word_index = 0
    win = 0
    while word_index < len(word_list):
        turns = 0
        guesses_letter = ""
        result = False
        while turns < MAX_GUESSES:
            word = word_list[word_index]
            failed = 0
            failed, guess_string = print_guess_msg(guesses_letter,
                                                   word, failed)
            print(guess_string)
            guess = input("\nEnter a letter or word:")
            guess = guess.upper()
            if len(guess) == 1:
                if guesses_letter.count(guess) == 1:
                    print("You've already guessed that letter!")
                else:
                    guesses_letter += guess
                    turns += 1
                if guess not in word:
                    print("Your guess so far: " + guesses_letter)
            if (((failed == 1) and check(guesses_letter, word)) or
                    (guess == word)):
                print("You win!")
                result = True
                break
            if turns == MAX_GUESSES:
                print("You lose! Th word was " + word)
                break
        if result is True:
            win += 1
        word_index += 1
    print("You won " + str(win) + " out of 3")
    # When the user has played all 3 rounds


def check(guesses_letter, word):
    '''
    Function: check - this is used to check if the all characters in the word
    exist in guesses_letter

    Parameters:
    guesses_letter: all letters that have been guessed so far
    word: the secret word

    Return:
    Boolean values: True if all characters in the word exist
    in guesses_letter, False otherwise
    '''
    guesses_letter_set = set(guesses_letter)
    for char in word:
        if char not in guesses_letter_set:
            return False
    return True


def print_guess_msg(guesses_letter, word, failed):
    '''
    Function: print the guess msg to let the user know how many characters
    does the word has and the correct characters that the user guessed

    Parameter:
    guesses letter: all letters that have been guessed so far
    word: the secret word

    Return:
    string: "_" for unguessed/unrevealed characters and any characters that
    the user correctly guessed
    '''
    string = ""
    for char in word:
        if char in guesses_letter:
            string += char
            # print(char, end="")
        else:
            string += "_"
            # print("_", ends="")
            failed += 1
    return (failed, string)


if __name__ == "__main__":
    main()
