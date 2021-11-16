'''
Yingshu Wang
CS5001 Fall 2021

Test palinfrome.py
'''


from palindrome import is_palindrome


def test_case_insensitive():
    assert(is_palindrome("ABBA"))
    assert(is_palindrome("RaceCar"))
    assert(is_palindrome("Hannah"))
    assert(not is_palindrome("banana"))
    assert(not is_palindrome("racecars"))
    assert(not is_palindrome("parachute"))


def test_punctuation():
    assert(is_palindrome("!Kayak!"))
    assert(not is_palindrome("A man, a plan, a canal, Panama!"))


def test_spaces():
    assert(is_palindrome("A man a plan a canal Panama"))
    assert(not is_palindrome("apples and pears"))
