'''
Yingshu Wang
CS5001 Fall 2021

Test vowelsearch.py
'''


from vowelsearch import voewel_search_in_word, contains_vowel


def test_voewel_search_in_word():
    assert(voewel_search_in_word("garage"))
    assert(voewel_search_in_word("this"))
    assert(not voewel_search_in_word("fffff"))
    assert(not voewel_search_in_word(""))


def test_contains_vowel():
    assert(contains_vowel(["garage", "this", "man"]))
    assert(not contains_vowel(["ffff", "this", "man"]))
    assert(not contains_vowel([]))
    assert(not contains_vowel([""]))
    assert(not contains_vowel(["", ""]))
