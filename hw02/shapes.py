'''
Yingshu Wang
CS5001, Fall 2021

This program calculates the area of a shape based on its dimenstions.
'''


def main():
    TRIANGLE = "triangle"
    SQUARE = "square"
    RECTANGLE = "rectangle"

    the_shape = input("Select a shape (triangle, square, or rectangle): ")\
        .lower()
    if the_shape != TRIANGLE and the_shape != SQUARE and \
       the_shape != RECTANGLE:
        print("Unknown shape")
    else:
        width = float(input("Enter the width: "))
        if width <= 0:
            print("Invalid width")
        else:
            height = width
            if the_shape != SQUARE:
                height = float(input("Enter the height: "))
            if height >= 0:
                area = width * height
                if the_shape == TRIANGLE:
                    area = area / 2
                print("The area of the {} is {:.2f}".format(the_shape, area))
            else:
                print("Invalid height")


if __name__ == "__main__":
    main()
