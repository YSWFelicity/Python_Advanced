'''
Yingshu Wang
CS5001 Fall 2021

A program that test if a UPC has been entered incorrectly during checkout.
'''


def is_valid_UPC(str_UPC):
    '''
        Function -- is_valid_UPC
            Checks if a given string is a valid UPC.
        Parameter:
            str_UPC -- The string to check
        Returns:
            True if a given string is a multiple of 10, False otherwise.
    '''
    if not str_UPC.isdigit():
        return False
    total = 0
    # iterate from left to right in UPC
    for i, char in enumerate(reversed(str_UPC)):
        EVEN_DENOMINATOR = 2
        if i % EVEN_DENOMINATOR == 0:
            # Add numbers in even positions to toal
            total += int(char)
        else:
            # Multiply numbers in odd positions by 3 then add to total
            ODD_MULTIPLIER = 3
            total += ODD_MULTIPLIER * int(char)

    # Test if total is a multiple of 10
    EVEN_MULTIPLIER = 10
    return total % EVEN_MULTIPLIER == 0


def main():
    upc = input("Enter a UPC number:\n")
    if is_valid_UPC(upc):
        print("Valid UPC!")
    else:
        print("Not a valid UPC.")


if __name__ == "__main__":
    main()
