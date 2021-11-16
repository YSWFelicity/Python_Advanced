'''
Yingshu Wang
CS5001 Fall 2021

Test hangman.py
'''


from hangman import (check, print_guess_msg)


def test_check():
    assert(check("APLEQP", "APPLE") is True)
    assert(check("APEQWE", "APPLE") is False)


def test_print_guess_msg():
    assert(print_guess_msg("APLEQP", "APPLE", 0) == (0, "APPLE"))
    assert(print_guess_msg("APLOYT", "APPLE", 0) == (1, "APPL_"))
