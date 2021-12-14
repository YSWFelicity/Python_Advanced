'''
Yingshu Wang
CS 5001, Fall 2021

Final project.
'''


import turtle
from constant import ROWS, COLS, SQUARE_SIZE
from gamestate import GameState
from piece import Piece
from board import Board


def main():
    board_size = COLS * SQUARE_SIZE
    window_size = board_size + SQUARE_SIZE
    turtle.setup(window_size, window_size)
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")
    turtle.tracer(0, 0)
    screen = turtle.Screen()
    screen.title("Checkers")
    game = GameState()
    board = Board()
    board.draw_chess_quares()
    game.draw_pieces()
    screen.onclick(game.update)
    screen.listen()
    turtle.done()


if __name__ == "__main__":
    main()
