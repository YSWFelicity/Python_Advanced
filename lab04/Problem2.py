'''
Lab 4
Unit test of Problem 1
Yingshu Wang
'''

from Problem1 import calculate_total_bill, split_bill


def test_calculate_total_bill():
    assert(calculate_total_bill(60, 0.2) == 72)
    assert(calculate_total_bill(-1, 1.2) == -1)


def test_split_bill():
    assert(split_bill(-1, 2) == -1)
    assert(split_bill(10, 0) == -1)
    assert(split_bill(20, 4) == 5)
