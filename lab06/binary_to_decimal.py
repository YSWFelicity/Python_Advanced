'''
Yingshu Wang
CS5001 Fall 2021

A program that transfer binary to decimal.
'''


def binary_to_decimal(binary_string):
    # Loop from the back of the string to the front (w/o reversing)
    pwr = 0
    total = 0
    for index in range(len(binary_string)-1, -1, -1):
        if binary_string[index] == "1":
            total += 2**pwr
            pwr += 1
        else:
            # add zero to result and increment place/power value
            pwr += 1
    return total


def binary_to_decimal_recur(binary_string):
    # Base cases
    if binary_string == "0":
        return 0
    elif binary_string == "1":
        return 1
    # Recursive case
    else:
        return 2*binary_to_decimal_recur(binary_string[0:-1]) \
               + binary_to_decimal_recur(binary_string[-1])


def main():
    binary_string = input("Enter a binary number: ")
    converted = binary_to_decimal(binary_string)
    converted_recur = binary_to_decimal_recur(binary_string)
    print(binary_string, "=", converted)
    print(binary_string, "=", converted_recur)


if __name__ == "__main__":
    main()
