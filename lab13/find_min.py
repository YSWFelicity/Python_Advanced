'''
Yingshu Wang
CS5001 Fall 2021

Lab12
'''


def min_in_shifted_lst(lst):
    '''
    Function -- min_in_shifted_lst
        Find min in a shifted list
    Parameter:
        lst -- a sorted list but has some unkonwn number shifted
    Returns:
        Minimum of the list.
    '''
    if len(lst) > 1:
        min_value = lst[0]
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                min_value = lst[i + 1]
                break
        return min_value
    elif len(lst) == 1:
        return lst[0]
    else:
        return "The list is empty"


def main():
    # lst = [1,4,5,6,9,10,55]
    # lst = [9,10,55,0, 1,4,5,6]
    # lst = [9,10,55,120,0, 1,4,5,6]
    # lst = [18, 25, 38, 1, 12, 13]
    # lst = [2, 1]
    # lst = [1]
    lst = []
    print(min_in_shifted_lst(lst))


main()
