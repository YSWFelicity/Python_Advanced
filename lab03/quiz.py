'''
Yingshu Wang
CS 5001, Fall 2021
This program asks the user 3 questions and uses their answers to determine
which Harry Potter character they are.
'''


def main():
    A = "A"
    B = "B"
    C = "C"

    print("Which Harry Potter character are you?\n\n")

    print("Question 1.")
    print("When planning a trip, you...\n")
    print("A: Find the hot parties.\n")
    print("B: Sort out all the logistics.\n")
    print("C: Let everyone else take charge.\n")

    answer1 = input("Enter your choice: A, B, or C\n").upper()
    if answer1 != A and answer1 != B and answer1 != C:
        answer1 = A

    print("\n\n")
    print("Question 2.")
    print("What are you most afraid of?\n")
    print("A: Not being accepted.\n")
    print("B: Losing someone close to me.\n")
    print("C: Looking stupid in front of others.\n")

    answer2 = input("Enter your choice: A, B, or C\n").upper()
    if answer2 != A and answer2 != B and answer2 != C:
        answer2 = A
    print("\n\n")
    print("Question 3.")
    print("What was your favorite toy as a kid?\n")
    print("A: SheRa.\n")
    print("B: HeMan.\n")
    print("C: Video games.\n")

    answer3 = input("Enter your choice: A, B, or C\n").upper()
    if answer3 != A and answer3 != B and answer3 != C:
        answer3 = A
    print("\n\n")

    print("You answered:", answer1, answer2, answer3)

    result_msg = "Your result: you are"

    if answer1 == A:
        if answer2 == A:
            if answer3 == A:
                print(result_msg, "Ginny")
            elif answer3 == B:
                print(result_msg, "Draco")
            else:
                print(result_msg, "Sirius")
        elif answer2 == B:
            print(result_msg, "Dobby")
        else:
            print(result_msg, "Voldemort")
    elif answer1 == B:
        print(result_msg, "Hermione")
    else:
        if answer2 == A:
            if answer3 == A:
                print(result_msg, "Luna")
            elif answer3 == B:
                print(result_msg, "Hagrid")
            else:
                print(result_msg, "Ron")
        elif answer2 == B:
            print(result_msg, "Tonks")
            return "Tonks"
        else:
            print(result_msg, "Slughorn")


if __name__ == "__main__":
    main()
