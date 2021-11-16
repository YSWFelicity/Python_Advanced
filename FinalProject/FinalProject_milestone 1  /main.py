'''
Yingshu Wang
CS 5001, Fall 2021

This code will get you started with the final project, milestone 1.
'''
import turtle


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    print("Clicked at ", x, y)


def draw_square(a_turtle, size, fill_color):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
            fill_color -- fill color for the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    OUTLINE_COLOR = "black"
    RIGHT_ANGLE = 90
    a_turtle.pendown()
    a_turtle.color(OUTLINE_COLOR, fill_color)
    a_turtle.begin_fill()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_chess_quares(a_turtle, size, num_row_squares, num_col_squares):
    '''
        Function -- draw_chess_quares
            Draw squares for a chess
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
            num_row_squares -- number of squares for row
            num_col_squares -- number of squares for column
        Returns:
            Nothing. Draws a chess in the graphics window.
    '''
    board_size = num_row_squares * size
    pen_start_x = -board_size / 2
    pen_start_y = -board_size / 2
    for i in range(num_col_squares):
        for j in range(num_row_squares):
            pen_x = pen_start_x + i * size
            pen_y = pen_start_y + j * size
            a_turtle.color("black", "white")
            a_turtle.setposition(pen_x, pen_y)
            a_turtle.pendown()
            fill_color = "white"
            if (i + j) % 2 != 0:
                fill_color = "grey"
            draw_square(a_turtle, size, fill_color)
            a_turtle.penup()


def draw_circle(a_turtle, size, fill_color):
    '''
    Function -- draw_init_pieces
        Draw initial pieces
    Parameters:
        a_turtle -- an instance of Turtle
        size -- the diameter of the circle
        fill_color -- circle fill color
    Returns:
        Nothing. Draws a circle in the graphics window.
    '''
    OUTLINE_COLOR = "black"
    a_turtle.pendown()
    a_turtle.color(OUTLINE_COLOR, fill_color)
    a_turtle.begin_fill()
    a_turtle.circle(size / 2)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_init_pieces(a_turtle, size, num_row_squares, num_col_squares,
                     user_fill_color, AI_fill_color):
    '''
        Function -- draw_init_pieces
            Draw initiated peices for user and AI
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the diameter of the circle
            num_row_squares -- number of squares for row
            num_col_squares -- number of squares for column
            user_fill_color -- circle fill color
            AI_fill_color -- AI fill color
        Returns:
            Nothing. Draws initiated pieces for user
    '''
    board_size = num_row_squares * size
    pen_start_x = -board_size / 2 + size / 2
    pen_start_y = -board_size / 2
    for i in range(num_row_squares):
        for j in range(num_col_squares):
            pen_x = pen_start_x + j * size
            pen_y = pen_start_y + i * size
            a_turtle.setposition(pen_x, pen_y)
            if (j + i) % 2 != 0 and i != 3 and i != 4:
                if i < 3:
                    draw_circle(a_turtle, size, user_fill_color)
                else:
                    draw_circle(a_turtle, size, AI_fill_color)
            a_turtle.penup()


def main():
    NUM_SQUARES = 8
    # The number of squares on each row.
    SQUARE = 50
    # The size of each square in the checkerboard.
    SQUARE_COLORS = ("light gray", "white")

    board_size = NUM_SQUARES * SQUARE
    # Create the UI window.
    window_size = board_size + SQUARE
    # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)
    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")
    # The window's background color
    turtle.tracer(0, 0)
    # makes the drawing appear immediately
    pen = turtle.Turtle()
    # This variable does the drawing.
    pen.penup()
    # This allows the pen to be moved.
    # pen.hideturtle() # This gets rid of the triangle cursor.
    pen.color("black", "white")
    # YOUR CODE HERE
    draw_chess_quares(pen, SQUARE, NUM_SQUARES, NUM_SQUARES)
    # Place initial pieces
    draw_init_pieces(pen, SQUARE, NUM_SQUARES, NUM_SQUARES, "black", "red")
    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler)
    # report click coordinates
    turtle.done()
    # Stops the window from closing.


if __name__ == "__main__":
    main()
