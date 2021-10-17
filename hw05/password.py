'''
Yingshu Wang
CS5001 Fall 2021

A program that checks if it is a secure password.
'''


def is_valid_length(password):
    '''
        Function -- is_valid_length
            Checks if the length of a given password is between 9 and 12.
        Parameter:
            password -- The string to check password
        Returns:
            True if a given string is in the range of 9 to 12, False otherwise.
    '''
    return 9 <= len(password) <= 12


def has_letter(password):
    '''
        Function -- has_letter
            Checks if a given password has lowercase or uppercase letters.
        Parameter:
            password -- The string to check password
        Returns:
            True if a given string has letters, False otherwise.
    '''
    VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for char in password:
        if char in VALID_LETTERS:
            return True
    return False


def has_number(password):
    '''
        Function -- has_number
            Checks if a given password has digit(0-9).
        Parameter:
            password -- The string to check password
        Returns:
            True if a given string has digit(0-9), False otherwise.
    '''
    VALID_NUMBERS = "0123456789"
    for char in password:
        if char in VALID_NUMBERS:
            return True
    return False


def has_special(password):
    '''
        Function -- has_special
            Checks if a given password has special characters.
        Parameter:
            password -- The string to check password
        Returns:
            True if a given string has special characters, False otherwise.
    '''
    VALID_SPECIALS = "$#@!"
    for char in password:
        if char in VALID_SPECIALS:
            return True
    return False


def main():
    password = input("Please choose a password:\n")
    error = ""

    # Test if password is valid, include error message if not.
    # Not limited to one error message.
    if not is_valid_length(password):
        error += "must be between 9 and 12 characters, inclusive\n"
    if not has_letter(password):
        error += "must contain at least 1 letter\n"
    if not has_number(password):
        error += "must contain at least 1 number\n"
    if not has_special(password):
        error += "must contain at least 1 special character ($, #, @, !)\n"

    # If error is empty, password passed all tests
    if error == "":
        print("Password is valid")
    else:
        print("Password is invalid:\n" + error.strip())
        # strip removes trailing newline


if __name__ == "__main__":
    main()
