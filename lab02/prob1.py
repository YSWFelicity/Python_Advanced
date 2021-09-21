'''
Lab 1
Problem 1: Eating out with a group 
Yingshu Wang 
'''

def main(total_bill, tip_percent, num_people):
    tip_amount = total_bill * tip_percent
    return round((total_bill + tip_amount) / num_people, 2)

# Test runs 
print("Test runs\nExpected results: 24.0, 21.26, 40.0")
print(main(60, 0.2, 3))
print(main(110.9, 0.15, 6))
print(main(20, 1, 1))

if __name__ == "__main__":
    main()