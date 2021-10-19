'''
Yingshu Wang
CS5001 Fall 2021

Test scores.py
'''


from scores import smaller, larger, average, median


def test_smaller():
    assert(smaller(98, 99) == 98)


def test_larger():
    assert(larger(98, 99) == 99)


def test_average():
    assert(average(98, 99, 100) == 99)


def test_median():
    assert(median(95, 96, 98) == 96)
