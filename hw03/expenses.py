'''
Yingshu Wang
CS 5001, Fall 2021
This module contains functions for calculating business trip mileage expenses.
'''


def calculate_mileage(start, end):
    '''
        Function -- calculate_mileage
            Calculates miles driven using the start and end odometer values.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
                number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
                number greater than 0 and greater than the start value.
        Returns:
            The miles driven, a number. If either parameter is invalid (e.g.
            either parameter is negative or end is less than start), returns 0.
    '''
    if start < 0 or end < 0 or end <= start:
        return 0
    return end - start


def get_reimbursement_amount(mileage):
    '''
        Function -- get_reimbursement_amount
            Calculates the amount in dollars that the employee should be
            reimbursed based on their mileage and the standard rate per mile.
            The standard rate for 2020 is 57.5 cents per mile.
        Parameters:
            mileage -- The number of miles driven.
        Returns:
            The amount the employee should be reimbursed in dollars, a float
            rounded to 2 decimal places.
    '''
    MILEAGE_RATE = 0.575
    return round(mileage * 0.575, 2)


def get_actual_mileage_rate(mpg, fuel_price):
    '''
        Function -- get_actual_mileage_rate
            Calculates the actual trip cost per mile in dollars based on the
            car's MPG and the fuel price.
        Parameters:
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel cost in dollars per gallon, a non-negative
            float.
        Returns:
            The actual cost per mile in dollars, a float rounded to 4 decimal
            places. If supplied arguments are invalid, returns 0.0
    '''
    if valid_arguments(mpg, fuel_price):
        return round(fuel_price / mpg, 4)
    return 0.0


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
        Function -- get_actual_trip_cost
            Calculates the cost of a trip in dollars based on the miles driven,
            the MPG of the car, and the fuel price per gallon.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
                number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
                number greater than 0 and greater than the start value.
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel price per gallon, a non-negative float.
        Returns:
            The cost of the drive in dollars, a float rounded to 2 decimal
            places. If any of the supplied arguments are invalid, returns 0.0
    '''
    miles = calculate_mileage(start, end)
    if valid_arguments(mpg, fuel_price):
        gallons_used = get_actual_mileage_rate(mpg, fuel_price)
        return round(gallons_used * miles, 2)
    return 0.0


def valid_arguments(mpg, fuel_price):
    '''
        Function -- valid_arguments
            Checks that the mpg and fuel price arguments are both valid.
        Parameters:
            mpg -- The car's MPG. Must be greater than 0.
            fuel_price -- The cost of fuel. Must be non-negative.
        Returns:
            True if both values are valid. False otherwise.
    '''
    return mpg > 0 and fuel_price >= 0


def main():
    print("MILEAGE REIMBURSEMENT CALCULATOR")
    print("Options:")
    print("1 - Calculate reimbursement amount from odometer readings")
    print("2 - Calculate reimbursement amount from miles traveled")
    print("3 - Calculate the actual cost of your trip")
    choice = int(input("Enter your choice (1, 2, or 3): "))
    if choice < 1 or choice > 3:
        print("Not a valid choice")
    else:
        if choice == 1 or choice == 3:
            start = int(input("Enter your starting odometer reading: "))
            end = int(input("Enter your ending odometer reading: "))
            if choice == 3:
                mpg = int(input("Enter your car's MPG: "))
                fuel = float(input("Enter the fuel price per gallon: "))
                print("Your trip cost ${:.2f}"
                      .format(get_actual_trip_cost(start, end, mpg, fuel)))
            else:
                miles_traveled = calculate_mileage(start, end)
        elif choice == 2:
            miles_traveled = int(input("Enter the number of miles traveled: "))
        if choice == 1 or choice == 2:
            print("You will be reimbursed ${:.2f}"
                  .format(get_reimbursement_amount(miles_traveled)))


if __name__ == "__main__":
    main()
