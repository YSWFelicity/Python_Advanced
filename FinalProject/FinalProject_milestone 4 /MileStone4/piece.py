'''
Yingshu Wang
CS 5001, Fall 2021

This code will get you started with the final project, milestone 4.
'''


import turtle
from .constant import ROWS, COLS, SQUARE_SIZE, PADDING


class Piece():
    '''
    Class -- Piece
        A piece
    Attributes:
        row -- The row where a piece locates; an integer from 0 to 7.
        col -- The column where a piece locates; an integer from 0  to 7.
        color -- The color that a piece is: String data type.
        isKing -- If the piece is king; Boolean type.
        center_x -- x coordinate; center is zero.
        center_y -- y coordinate, center is zero.
        a_turtle -- Create a turtle object.
    Methods:
        _calc_x_y_from_col_row -- Calculate x and y coordinates for a piece;
                                  private method.
        _make_king -- Make a piece to be a king; private function.
        move -- Move a piece.
        draw_piece -- Draw a piece.
        _draw_circle -- Draw a circle; private function.
    '''
    def __init__(self, row, col, color):
        '''
        Constructor -- Creates a new instance of PlayingCard
        Parameters:
            self -- The current Piece object.
            row -- The row where a piece locates; an integer from 0 to 7.
            col -- The column where a piece locates; an integer from 0  to 7.
            color -- The color that a piece is: String type.
        '''
        self.row = row
        self.col = col
        self.color = color
        self.isKing = False
        self.center_x, self.center_y = self._calc_x_y_from_col_row()
        self.a_turtle = turtle.Turtle()


    def _calc_x_y_from_col_row(self):
        '''
        Method -- _calc_x_y_from_col_row
            Calculate x and y coordinates for a piece based on row and column.
        Parameter:
            self -- The current piece object
        Returns:
            x and y coordinates.
        '''
        self.center_x = self.col * SQUARE_SIZE + SQUARE_SIZE / 2
        self.center_y = self.row * SQUARE_SIZE + SQUARE_SIZE / 2
        return self.center_x, self.center_y

    def _make_king(self):
        '''
        Method -- _make_king
            Make a piece to be a king.
        Parameter:
            self -- The current Piece object.
        '''
        self.isKing = True

    def move(self, to_row, to_col):
        '''
        Method -- move
            Move a piece to destination row and column.
        Parameter:
            self -- The current Piece object
            to_row -- The row of destination cell that the piece gonna move to.
            to_col -- The col of destination cell that the piece gonna move to.
        '''
        self.row = to_row
        self.col = to_col
        if self.row == 0 and self.color == "red":
            self._make_king()
        if self.row == ROWS - 1 and self.color == "black":
            self._make_king()
        self.center_x, self.center_y = self._calc_x_y_from_col_row()

    def draw_piece(self):
        '''
        Method -- draw_piece
            Draw a piece.
        Parameter:
            self -- The current Piece object
        '''
        radius = SQUARE_SIZE / 2 - PADDING
        self.a_turtle.setposition(- COLS * SQUARE_SIZE / 2 + self.center_x,\
                                  - COLS * SQUARE_SIZE / 2 + self.center_y \
                                  - radius)
        self._draw_circle(radius, self.color)
        if self.isKing:
            self._draw_circle(radius, self.color, "yellow")

    def _draw_circle(self, radius, fill_color, outline_color = "black"):
        '''
        Function -- _draw_circle
            Draw a circle. Piece drawing is based on this method.
        Parameters:
            self -- The current Piece object
            radius -- the radius of the circle.
            fill_color -- Circle filled color.
            outline_color -- The outline color is assumed to be black. When a
                             piece become a king, the outline color become
                             yellow.
        Returns:
            Nothing. Draws a circle in the graphics window.
        '''
        self.a_turtle.pendown()
        self.a_turtle.color(outline_color, fill_color)
        self.a_turtle.begin_fill()
        self.a_turtle.circle(radius)
        self.a_turtle.end_fill()
        self.a_turtle.penup()
