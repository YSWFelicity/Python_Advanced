'''
Yingshu Wang
CS5001 Fall 2021

Test palinfrome.py
'''


from palindrome import is_pal


def test_is_pal():
    assert(is_pal("home") is False)
    assert(is_pal("appa") is True)
    assert(is_pal("") is True)
    assert(is_pal("cdde   abc  cba eddc  ") is True)
