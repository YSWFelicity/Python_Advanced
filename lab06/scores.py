'''
Yingshu Wang
CS5001 Fall 2021

A program that computes statistics for a class of students'
scores on an assignment.
'''


def smaller(grade1, grade2):
    '''
        Function - smaller
            Returns the smaller of two numbers.
        Parameters:
            num1 - The first number to consider
            num2 - The second number to consider
        Returns:
            The smaller of the two numbers.
    '''
    return min(grade1, grade2)


def larger(grade1, grade2):
    '''
        Function - larger
            Returns the larger of two numbers.
        Parameters:
            num1 - The first number to consider
            num2 - The second number to consider
        Returns:
            The larger of the two numbers.
    '''
    return max(grade1, grade2)


def average(grade1, grade2, grade3):
    '''
        Function -- average
            Calculates the mean of three numbers.
        Parameters:
            num1 - A number
            num2 - A number
            num3 - A number
        Returns:
            The mean of the parameters.
    '''
    return (grade1 + grade2 + grade3) / 3


def median(num1, num2, num3):
    '''
        Function -- median
            Calculates the median of three numbers.
        Parameters:
            num1 - A number
            num2 - A number
            num3 - A number
        Returns:
            The median of the parameters.
    '''
    smallest = min(num1, num2, num3)
    if num1 == smallest:
        return min(num2, num3)
    elif num2 == smallest:
        return min(num1, num3)
    return min(num1, num2)
