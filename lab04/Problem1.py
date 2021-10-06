'''
Lab 4
Problem 1: Eating out with a group
Yingshu Wang
'''


def calculate_total_bill(total_bill, tip_percent):
    if total_bill < 0 or tip_percent > 1:
        return -1
    return (1+tip_percent) * total_bill


def split_bill(total_amount_bill, num_people):
    if total_amount_bill < 0 or num_people < 1:
        return -1
    return total_amount_bill / num_people


def main():
    total_bill = float(input("Enter the bill amount: "))
    tip_percent = float(input("Enter the tip percentage: "))
    total_amount_bill = calculate_total_bill(total_bill, tip_percent)
    if total_amount_bill == -1:
        print("Provid a valid input.")
        return
    num_people = int(input("Enter the number of people: "))
    share = split_bill(total_amount_bill, num_people)
    print("Share of each person: $" + str(share))


if __name__ == "__main__":
    main()
