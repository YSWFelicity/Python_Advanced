'''
Yingshu Wang
CS5001 Fall 2021

Create a simple hangman game.
'''


def main():
    rounds = 6
    word_list = ['APPLE', 'OBVIOUS', 'XYLOPHONE']
    word_index = 0
    win = 0
    while word_index < 3:
        if game(word_list, word_index) is True:
            win += 1
        word_index += 1
    print("You won " + str(win) + " out of 3")
    # When the user has played all 3 rounds


def game(word_list, word_index):
    rounds = 6
    guess_letter = ""
    result = False
    while rounds > 0:
        word = word_list[word_index]
        failed = 0
        for char in word:
            if char in guess_letter:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        guess = input("\nEnter a letter or word:")
        guess = guess.upper()
        if (failed == 1) or (guess == word):
            print("\nYou win!")
            result = True
            break
        if len(guess) == 1:
            guess_letter += guess
            rounds -= 1
            if guess_letter.count(guess) > 1:
                print("\nYou've already guessed that letter!")
                # If the user guesses a letter they have already guessed.
            if guess not in word:
                guess_letter = "".join(set(guess_letter))
                print("\nYour guess so far: " + guess_letter)
            if rounds == 0:
                print("\nYou lose! The word was " + word)
                break
                # Move on to the next round
    return result


if __name__ == "__main__":
    main()
