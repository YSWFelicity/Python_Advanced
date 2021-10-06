'''
Lab 4
Problem 4: Test Days until Friday
Yingshu Wang
'''


from Problem3 import daysuntilfriday


def test_daysuntilfriday():
    assert(daysuntilfriday(["M", "Tu", "W", "Th", "F", "Sa", "Su"], "Tu") == 3)
