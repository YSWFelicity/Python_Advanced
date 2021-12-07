'''
Yingshu Wang
CS 5001, Fall 2021

Final project, milestone 4.
'''


import turtle
from .constant import ROWS, COLS, SQUARE_SIZE


class Board:
    '''
    Class -- Board
        A checkers game board.
    Attributes:
        a_turtle -- Create a turtle object.
        a_turtle.color -- Set drawing color.
    Methods:
        draw_square -- Draw a square of a given side size.
        draw_chess_quares -- Draw squares for the board.
    '''
    def __init__(self):
        '''
        Constructor -- Creates a new instance of Board.
        Parameters:
            self -- The current Board object.
        '''
        self.a_turtle = turtle.Turtle()
        self.a_turtle.color("black", "white")

    def draw_square(self, size, fill_color):
        '''
        Function -- Draw_square
            Draw a square given side size.
        Parameters:
            a_turtle -- An instance of Turtle.
            size -- The length of each side of the square.
            fill_color -- fill color for the square.
        '''
        OUTLINE_COLOR = "black"
        RIGHT_ANGLE = 90
        self.a_turtle.pendown()
        self.a_turtle.color(OUTLINE_COLOR, fill_color)
        self.a_turtle.begin_fill()
        for i in range(4):
            self.a_turtle.forward(size)
            self.a_turtle.left(RIGHT_ANGLE)
        self.a_turtle.end_fill()
        self.a_turtle.penup()

    def draw_chess_quares(self):
        '''
        Function -- draw_chess_quares
            Draw squares for a board.
        '''
        board_size = ROWS * SQUARE_SIZE
        pen_start_x = - board_size / 2
        pen_start_y = - board_size / 2
        for i in range(COLS):
            for j in range(ROWS):
                pen_x = pen_start_x + i * SQUARE_SIZE
                pen_y = pen_start_y + j * SQUARE_SIZE
                self.a_turtle.color("black", "white")
                self.a_turtle.setposition(pen_x, pen_y)
                self.a_turtle.pendown()
                fill_color = "white"
                if (i + j) % 2 != 0:
                    fill_color = "grey"
                self.draw_square(SQUARE_SIZE, fill_color)
                self.a_turtle.penup()
