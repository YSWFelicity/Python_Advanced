'''
Yingshu Wang
CS5001 Fall 2021

Reading the datest and calculate the number of positive reviews.
'''


def getReviewValue(line):
    '''
    Function -- getReviewValue
        Get review value from a line
    Parameters:
        line -- a string line with value at the end of the line
    Returns:
        Integer type value
    '''
    try:
        data = line.split(".")
        data_remove = data[-1].split("?")
        data_remove_special= data_remove[-1].split("!")
        data_remove_spe2 = data_remove_special[-1].split("+")
        data_remove_spe3 = data_remove_spe2[-1].split("10")
        data_remove_spe4 = data_remove_spe3[-1].split(":)")
        return int(data_remove_spe4[-1].strip())
    except IndexError:
        print("Error processing the file")
    except ValueError:
        print("Error processing the file")


def main():
    positive_review = 0
    isFile = False
    while not isFile:
        path = input("Enter the path to the IMDB dataset: ")
        try:
            with open(path, 'r') as file:
                isFile = True
                for line in file:
                    positive_review += getReviewValue(line)
            print("Positive reviews\tNegative reviews")
            print(positive_review, "\t\t\t", 1000-positive_review)
            return positive_review
        except FileNotFoundError:
            print("File not found!")


if __name__ == "__main__":
    main()
