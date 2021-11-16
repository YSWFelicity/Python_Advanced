'''
Yingshu Wang
CS5001 Fall 2021

Lab10
'''


import turtle


def draw_polygon(line_size, a_turtle, corner_angle, line_num, draw_color):
    '''
    Function -- draw_polygon
        Draw polygon
    Parameters:
        line_size -- line size
        a_turtle -- an instance of Turtle
        corner_angle -- corner angle. 36 for five star
        line_num -- number of lines
        draw_color -- drawing color
    Returns:
        Nothing. Draws polygon
    '''
    a_turtle.pendown()
    a_turtle.color(draw_color)
    for i in range(line_num):
        a_turtle.forward(line_size)
        a_turtle.right(180 - corner_angle)  # angle = 36 for each corner
    a_turtle.penup()


def draw_special_star(line_size, a_turtle, increasing_size):
    '''
    Function -- draw_special_star
        Draw a special star with each side decreasing size
    Parameters:
        line_size -- line size
        a_turtle -- an instance of Turtle
        increasing_size -- increasing magnitude each time
    Returns:
        Nothing. Draws the special star
    '''
    a_turtle.pendown()
    a_turtle.setheading(90 - 18)
    dic_color = {"0": "green", "1": "blue", "2": "brown", "3": "red", "4": "yellow"}
    for i in range(5):
        a_turtle.color(dic_color["{}".format(i)])
        a_turtle.forward(line_size + i * increasing_size)
        a_turtle.right(180 - 36)  # angle = 36 for each corner
    a_turtle.penup()


def draw_special_stars(line_size, a_turtle, increasing_size):
    '''
    Function -- draw_special_stars
        Draw a serial of special stars with each side decreasing size
        recursive function
    Parameters:
        line_size -- line size
        a_turtle -- an instance of Turtle
        increasing_size -- increasing size
    Returns:
        Nothing. Draws the special stars
    '''
    LAST_TRY_LINE = 300
    if line_size >= LAST_TRY_LINE:
        return draw_special_star(LAST_TRY_LINE, a_turtle, increasing_size)
    else:
        draw_special_star(line_size, a_turtle, increasing_size)
        return draw_special_stars(line_size + increasing_size * 5, a_turtle, increasing_size)


def main():
    pen = turtle.Turtle()  # Create a variable of data type Turtle with label turt
    pen.color('yellow')  # Modify the color of the turtle you just made
    draw_special_stars(100, pen, 10)
    turtle.done()
    # Stops the window from closing.


if __name__ == "__main__":
    main()
