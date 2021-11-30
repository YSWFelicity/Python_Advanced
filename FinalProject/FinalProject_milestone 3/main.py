'''
Yingshu Wang
CS 5001, Fall 2021

Final project, milestone 3.
'''


import turtle
from MileStone3.constant import ROWS, COLS, SQUARE_SIZE
from MileStone3.gamestate import GameState
from MileStone3.piece import Piece
from MileStone3.board import Board


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
