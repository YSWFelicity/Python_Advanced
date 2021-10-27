'''
Yingshu Wang
CS5001 Fall 2021

Determines the greatest common divisor of two or more numbers using recursion.
'''


def gcd_recursive(num1, num2):
    '''
    Determines the greatest common divisor of two numbers using recursion.
    num1, num2 -- Non-zero positive integers.
    '''
    if num2 == 0:
        return num1
    else:
        return gcd_recursive(num2, num1 % num2)


def gcd_multiple_nums(int_list):
    '''
    Determines the greatest common divisor of an arbitrary
    amount of positive integers.
    int_list -- A list of positive Integers with length >= 2.
    '''
    first_two_gcd = gcd_recursive(int_list[0], int_list[1])
    if len(int_list) == 2:
        return first_two_gcd
    else:
        return gcd_multiple_nums([first_two_gcd] + int_list[2:])
