'''
Yingshu Wang
CS5001 Fall 2021

A program that about the Caesar cipher.
'''


def decrypt(str, shift, slide):
    new_str = ""
    for i in range(len(str)):
        new_str += chr(ord(str[i]) - shift)
    slide_str = [None] * len(new_str)
    for j in range(len(new_str)):
        slide_str[j - slide] = new_str[j]
    return slide_str


def main():
    print(decrypt("tfbu nz tipsu", 1, 1))


if __name__ == "__main__":
    main()
