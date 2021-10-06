'''
Lab 4
Problem 3: Days until Friday
Yingshu Wang
'''


def hello(name):
    print("Hello", name)


def daysuntilfriday(week, day):
    for x in range(len(week)):
        if week[x] == day:
            if x < 5:
                fri = 5 - (x+1)
                return fri
            else:
                fri = x + 1
                return fri


def main():
    week = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    name = input("Enter your Name: ")
    hello(name)
    day = input("Enter the Current Day (M, Tu, W, Th, F, Sa, Su): ")
    print("Days Until Friday left:", daysuntilfriday(week, day))


if __name__ == "__main__":
    main()
