'''
Yingshu Wang
CS5001 Fall 2021

Part 3--display selected reviews
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


def getComment(line):
    '''
    Function -- getComment
        Get comment from a line
    Parameters:
        line -- a string line with value at the end of the line
    Returns:
        String type comment
    '''
    try:
        data = line.split("0")
        data_remove = data[0].split("1")
        return data_remove[0].strip()
    except IndexError:
        print("Error processing the file")
    except ValueError:
        print("Error processing the file")


def main():
    index = input("Enter an index of a comment(p index/n index/q): ")
    path = "imdb_labelled.txt"
    while index != "q":
        index_part = index.split(" ")
        try:
            review_index = int(index_part[1])
            with open(path, "r") as file:
                count = 0
                if index_part[0].lower() == "p":
                        for line in file:
                            value = getReviewValue(line)
                            if value == 1:
                                count += 1
                                if count == review_index:
                                    print(getComment(line))
                                    break
                elif index_part[0].lower() == "n":
                        for line in file:
                            value = getReviewValue(line)
                            if value == 0:
                                count += 1
                                if count == review_index:
                                    print(getComment(line))
                                    break
                if count < review_index and count != review_index:
                    raise IndexError("The user provides a valid int but out of range")
        except ValueError:
            print("The user doesn't provide a valid integer")
        index = input("Enter an index of a comment(p index/n index/q): ")


if __name__ == "__main__":
    main()
