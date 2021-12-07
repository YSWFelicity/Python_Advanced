'''
Yingshu Wang
CS5001 Fall 2021

Lab12
'''

from find_min import min_in_shifted_lst


def test_min_in_shifted_lst():
    assert(min_in_shifted_lst([18, 25, 38, 1, 12, 13]) == 1)
    assert(min_in_shifted_lst([25, 38, 40, 12, 13]) == 12)
    assert(min_in_shifted_lst([12, 13, 25, 38]) == 12)
    assert(min_in_shifted_lst([1]) == 1)
    assert(min_in_shifted_lst([2, 1]) == 1)
