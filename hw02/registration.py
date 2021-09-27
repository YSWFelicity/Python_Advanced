'''
CS5001, Fall 2021
Yingshu Wang

A basic course registration system
'''


def main():
    X101 = "X101"
    X102 = "X102"
    B500 = "B500"
    B525 = "B525"
    B701 = "B701"

    course_number = input("Enter a course number: ").upper()
    course_number = course_number.replace(" ", "")
    if course_number == X101 or course_number == X102:
        print("You have successfully registered for", course_number)
    elif (course_number == B500 or course_number == B525 or
          course_number == B701):
        prereq1 = input("Waht grade did you get for X101? ").upper()
        prereq2 = input("Waht grade did you get for X102? ").upper()
        if (prereq1 == "A" or prereq1 == "B") and prereq2 >= "A" and \
           prereq2 <= "C":
            print("You meet all the prerequistites and have successfully "
                  "registered for", course_number)
        else:
            print("You do not meet the prerequisites for", course_number)
    else:
        print("Invalid course number")


if __name__ == "__main__":
    main()
