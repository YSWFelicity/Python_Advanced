'''
Yingshu Wang
CS5001 Fall 2021

Test lightrail.py
'''


from lightrail import is_valid_station, get_direction, get_num_stops


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))
    assert(is_valid_station("Northgate"))


def test_get_direction():
    assert(get_direction("Northgate", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "Northgate")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_num_stops():
    assert(get_num_stops("Northgate", "Angle Lake") == 18)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University of Washington", "Angle Lake") == 15)
