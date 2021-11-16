'''
Yingshu Wang
CS5001 Fall 2021

Test upc.py
'''


from upc import is_valid_UPC


def test_is_valid_UPC():
    assert(is_valid_UPC("9780128053904") is True)
    assert(is_valid_UPC("75839523467") is False)
    assert(is_valid_UPC("796030114977") is True)
    assert(is_valid_UPC("657893408568") is False)
    assert(is_valid_UPC("1234ghc!") is False)
