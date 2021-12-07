'''
Yingshu Wang
CS5001 Fall 2021

Lab12
'''


def binary_search(lst, item):
    '''
    Function -- binary_search
        Searches for the given list.
    Parameters:
        lst -- The list to search in.
        item -- The item to search for.
    Returns:
        True if item is in lst, False otherwise.
    '''
    length_lst = len(lst)
    if length_lst > 0:
        left_pos = 0
        right_pos = length_lst - 1
        mid = length_lst // 2
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            right_pos = mid
            return binary_search(lst[:right_pos], item)
        else:
            left_pos = mid
            return binary_search(lst[left_pos + 1:], item)
    else:
        return False


def main():
    lst = [1, 4, 5, 6, 9, 10, 55]
    item = 55
    print(binary_search(lst, item))


main()
