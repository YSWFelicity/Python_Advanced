# CS5001
# Fall 2021
# HW01 
# Yingshu Wang

'''
Sample solution
CS 5001, Fall 2021
This program takes input from a user about a race and returns stats about their
performance.
My test cases
1. 5k, finished in 0 hours, 30 mins => 3.11 miles, 9:40 pace, 6.21 MPH
2. 15k, finished in 1 hour, 2 mins => 9.32 miles, 6:39 pace, 9.02 MPH
3. 50k, finished in 2 hours, 28 mins => 31.06 miles, 4:46 pace, 12.59 MPH
'''


def main():
    KM_TO_MILES = 1.61
    MINS = 60
    km = float(input("How many kilometers did you run? "))
    hours = int(input("What was your finish time? Enter hours: "))
    minutes = int(input("Enter minutes: "))

    miles = km / KM_TO_MILES
    total_minutes = hours * MINS + minutes
    mph = miles / (total_minutes / MINS)
    pace_mins = MINS // mph
    pace_sec = round((MINS / mph - pace_mins) * MINS)
    miles_str = str(round(miles, 2))
    pace_str = str(round(pace_mins)) + ":" + str(pace_sec)
    mph_str = str(round(mph, 2))
    print(miles_str + " miles, " + pace_str + " pace, " + mph_str + " MPH")


if __name__ == "__main__":
    main()