# CS5001
# Fall 2021
# HW01 
# Yingshu Wang

KILOMETERS_TO_MILES = 1.61
HOUR_TO_SEC = 3600
MIN_TO_SEC = 60
HOUR_TO_MIN = 60
# Fuction: get_race_stats
# Purpose: runners can use to calculate statistics about a race time 
# distance and the time it took that a runner to finish 

def get_race_stats(distance, hours, minutes): 
    # Convert kilometers to miles: 1.61 kilometers per 1 mile 
    miles = float(distance / KILOMETERS_TO_MILES)

    # Calculate the total hours and total minutes for pace and mph 
    total_hours = float(hours + minutes/HOUR_TO_MIN)
    total_mins = float(hours*HOUR_TO_MIN + minutes)
    total_secs = float(hours * HOUR_TO_SEC + minutes * MIN_TO_SEC)
    # Calculate pace and separate into minutes and seconds  
    total_pace_secs = round(total_secs / miles, 2)
    pace_mins = int(round(total_pace_secs // MIN_TO_SEC))
    pace_secs = int(round(total_pace_secs % MIN_TO_SEC))
    

    mph = round(float(miles / total_hours), 2)

# Define special cases 
    miles_txt = "{:.2f} miles, ".format(miles)
    pace_txt = "{}:{} pace, ".format(pace_mins, pace_secs)
    mph_txt = "{} MPH".format(mph)

    return miles_txt + pace_txt + mph_txt

# End get_race_stats 
# Gets user input regarding the length of a race they ran and how long it took them 
def get_input():
    # For floats, convert from string to float to int
    kilometers = float(input("How many kilometers did you run? "))
    hours = float(input("What was your finish time? Enter hours: "))
    mins = float(input("Enter minutes: "))

    return (kilometers, hours, mins)

kilometers, hours, mins = get_input()

print(get_race_stats(kilometers, hours, mins))

# Test cases1: 
# How many kilometers did you run? 5 
# What was your finish time? Enter hours: 0
# Enter minutes: 30
# 3.11 miles, 9:40 pace, 6.21 MPH

# Test cases2: 
# How many kilometers did you run? 10 
# What was your finish time? Enter hours: 20
# Enter minutes: 15
# 6.21 miles, 195:37 pace, 0.31 MPH

# Test cases3: 
# How many kilometers did you run? 30.5 
# What was your finish time? Enter hours: 23.4
# Enter minutes: 30.2
# 18.94 miles, 75:42 pace, 0.79 MPH