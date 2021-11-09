'''
Yingshu Wang
CS5001 Fall 2021

Test recipes_py
'''


from recipes import isListEmpty, convertFilename


def test_isListEmpty():
    assert(isListEmpty(","))
    assert(not isListEmpty("cake,"))
    assert(not isListEmpty("vegitable, ,cake"))
    assert(isListEmpty(" "))


def test_convertFilename():
    assert(convertFilename("PB&J d") == "pbj_d")
    assert(convertFilename("!!!") == "")
    assert(convertFilename(" PB)J d ") == "pbj_d")
    assert(convertFilename("testing") == "testing")
