'''
Yingshu Wang
CS5001 Fall 2021

A program that get basic directions on the Seattle Link light rail.
'''

LINK_STATIONS = ("Northgate", "Roosevelt", "U District",
                 "University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(station):
    '''
        Function -- is_valid_station
            Checks if a given string is a valid Seattle light rail station.
            Provided station must match a station name exactly. For example,
            "mount baker" would not be valid because the case doesn't match.
        Parameter:
            station -- The string to check
        Returns:
            True if a given string is a valid Seattle light rail station
            name, False otherwise.
    '''
    return station in LINK_STATIONS


def get_direction(start, end):
    '''
    Function -- get_direction
        Given start and end station names, determines if the direction is
        Northbound or Southbound.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        "Northbound" if the end station is north of the start station, or
        "Southbound" if the end station is south of the start station. If
        either station is invalid, or start and end stations are the same,
        return "No destination found".
    '''
    start_i = LINK_STATIONS.index(start)
    end_i = LINK_STATIONS.index(end)

    # Find difference of indexes to find direction.
    # Stops further north will have smaller indexes than stops to the south.
    diff = start_i - end_i
    message = ""
    if diff < 0:
        message = "Southbound"
    elif diff > 0:
        message = "Northbound"
    else:
        # Same stop
        message = "No destination found"
    return message


def get_num_stops(start, end):
    '''
    Function -- get_num_stops
        Calculates the number of stops from start to end.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        The number of stops from start to end. If either station is invalid
        or both stations are the same, return 0.
    '''
    start_i = LINK_STATIONS.index(start)
    end_i = LINK_STATIONS.index(end)

    # Absolute value of the indexes equals the number of stops
    stops = abs(start_i - end_i)
    return stops
