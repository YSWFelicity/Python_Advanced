'''
Yingshu Wang
CS5001 Fall 2021

A program that transfer binary to decimal.
'''


def binary_to_decimal_recur(binary_string):
    # Base cases
    if binary_string == "0":
        return 0
    elif binary_string == "1":
        return 1
    # Recursive case
    else:
        return 2*binary_to_decimal_recur(binary_string[0:-1]) \
               + binary_to_decimal_recur(binary_string[-1])
