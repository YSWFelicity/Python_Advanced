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
    total_secs = float(total_hours * HOUR_TO_SEC + total_mins * MIN_TO_SEC)
    # Calculate pace and separate into minutes and seconds  
    
    pace_mins = round(miles / total_mins)
    pace_secs = float(float(miles / total_mins) - pace_mins) * MIN_TO_SEC
    

    mph = float(miles / total_hours)

# Define special cases 
    if miles == 1:
        miles_txt = "1 mile\n"
    else: 
        miles_txt = "{:.2f} miles\n".format(miles)

    pace_txt = "{pace_mins}:{pace_mins}".format(pace_mins, pace_secs)
    mph_txt = "{:.2f}".format(mph)

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

get_race_stats(kilometers, hours, mins))

