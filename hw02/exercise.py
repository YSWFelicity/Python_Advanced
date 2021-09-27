'''
Yingshu Wang
CS5001, Fall 2021

Create an exercise plan based on the day of the week and the weather
'''


def main():
    YES = "Y"
    NO = "N"
    MIN_TEMP = 35
    MAX_TEMP = 75
    DEFAULT_DURATION = 45
    SHORT_DURATION = 30

    day = input("What day is it? ").upper()
    holiday = input("Is it a holiday? ").upper()
    raining = input("Is it raining? ").upper()
    temp = float(input("What is the temperature? "))

    valid_day = day == "M" or day == "TU" or day == "W" or day == "TH" or \
        day == "F" or day == "SA" or day == "SU"
    valid_holiday = holiday == YES or holiday == NO
    valid_raining = raining == YES or raining == NO

    if not valid_day or not valid_holiday or not valid_raining:
        print("Swim for 35 minitues")
    else:
        is_holiday = holiday == YES
        is_raining = raining == YES
        is_workout_day = is_holiday or day == "M" or day == "W" or day == "F" \
            or day == "SA"
        too_cold = temp < MIN_TEMP
        too_hot = temp > MAX_TEMP
        if not is_workout_day:
            print("Take a rest day")
        else:
            duration = DEFAULT_DURATION
            exercise = "RUN"
            if is_raining:
                exercise = "Swim"
            elif day == "SA" or is_holiday:
                exercise = "Hike"
            elif too_cold or too_hot:
                duration = SHORT_DURATION
            print("{} for {} minutes".format(exercise, duration))


if __name__ == "__main__":
    main()
