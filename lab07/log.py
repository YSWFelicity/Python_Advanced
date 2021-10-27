'''
Yingshu Wang
CS5001 Fall 2021

Calculates the log base 2 of a given positive integer that is a power of 2
'''


def log2_recursive(number):
    # Base cases
    if number == 1:
        return 0
    elif number == 2:
        return 1
    # Recursive case
    else:
        return 1 + log2_recursive(number//2)
