'''
Yingshu Wang
CS5001 Fall 2021

Test password.py
'''


from password import is_valid_length, has_letter, has_number, has_special


def test_is_valid_length():
    assert(is_valid_length("Hello123") is False)
    assert(is_valid_length("Oops") is False)
    assert(is_valid_length("this is the greatest password ever") is False)
    assert(is_valid_length("") is False)
    assert(is_valid_length("abcefg123") is True)
    assert(is_valid_length("abc123!@98") is True)
    assert(is_valid_length("         ") is True)


def test_has_letter():
    assert(has_letter("Password") is True)
    assert(has_letter("123!@#") is False)
    assert(has_letter("") is False)
    assert(has_letter("        ") is False)
    assert(has_letter("123456abc") is True)
    assert(has_letter("123456ABC") is True)
    assert(has_letter("z") is True)
    assert(has_letter("abc123!@#ZYX") is True)
    assert(has_letter("  554321!@#~`[]24 d") is True)


def test_has_number():
    assert(has_number("Pa$$word24") is True)
    assert(has_number("Pa$$word") is False)
    assert(has_number("") is False)
    assert(has_number("1") is True)
    assert(has_number("!@#$%^&") is False)
    assert(has_number("abcdefghijklmon4") is True)


def test_has_special():
    assert(has_special("Pa$$word") is True)
    assert(has_special("NoSpecials23") is False)
    assert(has_special("%^&*-_+=") is False)
    assert(has_special("Hello!") is True)
    assert(has_special("P@ssword") is True)
    assert(has_special("#Password#") is True)
    assert(has_special("") is False)
    assert(has_special("   ") is False)
