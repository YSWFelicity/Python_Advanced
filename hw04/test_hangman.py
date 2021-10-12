'''
Yingshu Wang
CS5001 Fall 2021

Test hangman.py
'''


from hangman import game
from pytest import approx


def test_game():
    word_list = ['APPLE', "OBVIOUS", 'XYLOPHONE']
    word_index = 0
    assert(game(word_list, word_index) is True)

# Not a typical way of testing: using pytest -s test_hangman.py
