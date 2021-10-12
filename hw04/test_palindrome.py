'''
Yingshu Wang
CS5001 Fall 2021

Test palinfrome.py
'''


from palindrome import is_pal


def test_is_pal():
    assert(is_pal("home") is False)
    assert(is_pal("appa") is True)
    assert(is_pal("") is False)
    assert(is_pal("cdde   abc  cba eddc  ") is True)
    assert(is_pal("madam  Im adam") is True)
    assert(is_pal("a") is False)
    assert(is_pal("RADar") is True)
    assert(is_pal("!!!!") is True)
