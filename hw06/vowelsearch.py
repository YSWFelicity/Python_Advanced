'''
Yingshu Wang
CS5001 Fall 2021

A program that search the vowel in word.
'''


def voewel_search_in_word(word):
    '''
    Function -- voewel_search_in_word
        Check if there is a voewel in a string.
    Parameters:
        word -- A string
    Returns:
        True if a word contains a vowel. Otherwise, false.
    '''
    if len(word) == 0:
        return False
    elif len(word) == 1:
        if word.lower() in "aeiou":
            return True
        else:
            return False
    else:
        if voewel_search_in_word(word[0]):
            return True
        else:
            return voewel_search_in_word(word[1:])


def contains_vowel(lst_str):
    '''
    Function -- contains_vowel
        Check if there is a voewel in every string.
    Parameters:
        lst_str -- A list of strings
    Returns:
        True if every string in the list contains a vowel.Otherwise, false.
    '''
    if len(lst_str) == 0:
        return False
    elif len(lst_str) == 1:
        if voewel_search_in_word(lst_str[0]):
            return True
        else:
            return False
    else:
        if voewel_search_in_word(lst_str[0]):
            return contains_vowel(lst_str[1:])
        else:
            return False
