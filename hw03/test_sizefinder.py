'''
Yingshu Wang
CS 5001, Fall 2021
Test cases for sizefinder.py
'''

from sizefinder import size_valid, get_size, get_kids_size, get_womens_size, \
                       get_mens_size


def test_size_valid():
    assert(size_valid(45, 32, 46) == 1)
    assert(size_valid(32, 32, 46) == 1)
    assert(size_valid(46, 32, 46) == 0)


def test_get_size():
    assert(get_size(30, 25, 28, 2) == "not available")
    assert(get_size(30, 30, 32, 2) == "S")
    assert(get_size(40, 37, 43, 3) == "M")


def test_get_kids_size():
    assert(get_kids_size(30) == 'Kids size: L')
    assert(get_kids_size(25) == 'Kids size: not available')
    assert(get_kids_size(37) == 'Kids size: not available')


def test_get_womens_size():
    assert(get_womens_size(37) == 'Womens size: XL')
    assert(get_womens_size(29) == 'Womens size: not available')
    assert(get_womens_size(43) == 'Womens size: not available')


def test_get_mens_size():
    assert(get_mens_size(42) == 'Mens size: L')
    assert(get_mens_size(33) == 'Mens size: not available')
    assert(get_mens_size(54) == 'Mens size: not available')
