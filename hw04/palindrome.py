'''
Yingshu Wang
CS5001 Fall 2021
A program that test if the string is a palindrome or not.
'''


def is_pal(string):
    string = string.replace(' ', '').lower()
# purpose:
# Checks if a given string is palindrome (e.g. spelled the same forwards
# and backwards). Whitespace in the front, middle or back of a word does not
# affect the outcome, neither do the case of characters. Punctuation marks do
# influence the outcome.

    if len(string) < 2:
        # Automatic sucess cases
        return False
    else:
        # Seperate string at midpoint
        s_len = len(string)
        mid_point = s_len // 2
        if s_len % 2 == 0:
            # Even strings are seperated between middle two chars
            s_start = string[:mid_point]
            s_end = string[mid_point:]
        else:
            # Odd strings ignore middle char so each substring is equal length
            s_start = string[:mid_point]
            s_end = string[mid_point+1:]

        # Reverse end of string for equality testing
        s_end_rev = s_end[::-1]

        return s_start == s_end_rev


def main():
    test_str = input('Enter a word or phrase:\n')
    if is_pal(test_str):
        print(test_str.strip(), 'is a palindrome')
    else:
        print(test_str.strip(), 'is not a palindrome')


if __name__ == "__main__":
    main()
