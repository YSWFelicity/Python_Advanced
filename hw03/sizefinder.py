'''
Yingshu Wang
CS 5001, Fall 2021
Determines T-shirt sizing options based on chest measurement.
'''


def size_valid(chest_measurement, inches_min, inches_max):
    '''
        Function -- size_valid
            Test if the size is valid.
        Parameters:
            chest_measurement -- Give a random number of chest measurement in
            inches.
            inchese_min -- The minimum value of chest in inches.
            inches_max -- The maximum value of chest in inches.
        Returns:
            A boolean. If neither parameter is invalid (e.g.
            either chest_measurement is less than inchese_min or
            chest_measurement is greater than inchese_max, returns False.)
    '''
    return chest_measurement >= inches_min and chest_measurement < inches_max


def get_size(chest, inches_min, inches_max, interval):
    '''
        Function -- get_size
            Get the actual size of the chest size.
        Parameters:
            chest -- Give a random number of chest measurement in
            inches.
            inchese_min -- The minimum value of chest in inches.
            inches_max -- The maximum value of chest in inches.
            interval -- The interval of each of the size.
        Returns:
            A string. If neither parameter is invalid (e.g.
            either parameter is not within the inverval), returns
            "not available".
    '''
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4
    XXXL = 5
    if not size_valid(chest, inches_min, inches_max):
        return "not available"
    elif size_valid(chest, inches_min + interval * S,
                    inches_min + interval * M):
        return "S"
    elif size_valid(chest, inches_min + interval * M,
                    inches_min + interval * L):
        return "M"
    elif size_valid(chest, inches_min + interval * L,
                    inches_min + interval * XL):
        return "L"
    elif size_valid(chest, inches_min + interval * XL,
                    inches_min + interval * XXL):
        return "XL"
    elif size_valid(chest, inches_min + interval * XXL,
                    inches_min + interval * XXXL):
        return "XXL"
    return "XXXL"


def get_kids_size(chest):
    '''
        Function -- get_size
            Get the actual size of the kids chest size.
        Parameters:
            chest -- Give a random number of chest measurement in
            inches.
            inchese_min -- The minimum value of kids chest in inches.
            inches_max -- The maximum value of kids chest in inches.
            interval -- The interval of each of the size.
        Returns:
            A string. Get the kids size based on the parameters: chest
            measurement, the minimum and maximum chest size of kids,
            and the common interval of each step size of kids.
    '''
    KIDS_MIN = 26
    KIDS_MAX = 36
    INTERVAL_KIDS = 2
    return "Kids size: " + get_size(chest, KIDS_MIN, KIDS_MAX, INTERVAL_KIDS)


def get_womens_size(chest):
    '''
        Function -- get_size
            Get the actual size of the womens chest size.
        Parameters:
            chest -- Give a random number of chest measurement in
            inches.
            inchese_min -- The minimum value of womens chest in inches.
            inches_max -- The maximum value of womens chest in inches.
            interval -- The interval of each of the size.
        Returns:
            A string. Get the womens size based on the parameters: chest
            measurement, the minimum and maximum chest size of womens,
            and the common interval of each step size of womens.
    '''
    WOMENS_MIN = 30
    WOMENS_MAX = 42
    INTERVAL_WOMEN = 2
    return "Womens size: " + get_size(chest, WOMENS_MIN, WOMENS_MAX,
                                      INTERVAL_WOMEN)


def get_mens_size(chest):
    '''
        Function -- get_size
            Get the actual size of the mens chest size.
        Parameters:
            chest -- Give a random number of chest measurement in
            inches.
            inchese_min -- The minimum value of mens chest in inches.
            inches_max -- The maximum value of mens chest in inches.
            interval -- The interval of each of the size.
        Returns:
            A string. Get the kids size based on the parameters: chest
            measurement, the minimum and maximum chest size of mens,
            and the common interval of each step size of mens.
    '''
    MENS_MIN = 34
    MENS_MAX = 53
    INTERVAL_MEN = 3
    return "Mens size: " + get_size(chest, MENS_MIN, MENS_MAX, INTERVAL_MEN)


def main():
    MIN_INCHES = 26
    MAX_INCHES = 52
    chest = float(input("Chest measurement in inches: "))
    if size_valid(chest, MIN_INCHES, MAX_INCHES):
        print("Your size choices:")
        print(get_kids_size(chest))
        print(get_womens_size(chest))
        print(get_mens_size(chest))
    else:
        print("Sorry, we don't carry your size")


if __name__ == "__main__":
    main()
