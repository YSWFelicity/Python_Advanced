'''
Yingshu Wang
CS 5001, Fall 2021

Final project, milestone 2.
'''

import turtle
from .constant import WIDTH, HEIGHT, ROWS, COLS, SQUARE_SIZE, PADDING, INI_TURN
from .piece import Piece
from .board import Board


class GameState():
    '''
    Class -- GameState
        A game state.
    Attributes:
        pieces -- A list of pieces on a board.
        turn -- Game turn, red or black.
        selected -- Any piece is selected or not; Boolean type.
        valid_moves -- A dictionary to include valid moves and skipped pieces.
        pieces_left_red -- Number of red pieces left.
        pieces_left_black -- Number of black pieces left.
        a_turtle -- Create a turtle object.
    Methods:
        create_pieces -- Creates initiaive pieces; 12 reds and 12 blacks.
        draw_pieces -- Draw pieces.
        get_piece -- Get a piece based on row and column.
        turn_change -- Change turn.
        remove -- Remove pieces that are skipped.
        draw_valid_move -- Draw blue squares indicating valid moves.
        draw_square -- Draw a square given side size.
        move_a_piece_on_game -- Move a piece on a board.
        select -- Select a piece and moving destination cell.
        _move -- Take a validate move.
        update -- Update display every turn.
        search_valid_moves -- Create a dictionary indicating valid moves and
                              skipped pieces.
        left_search_moves -- Search valid cells and skipped cells in the left
                             direction.
        right_search_moves -- Search valid cells and skipped cells in the right
                              direction.
        isWinner -- Check if there is winner and who.
    '''
    def __init__(self):
        '''
        Constructor -- Creates a new instance of PlayingCard
        Parameters:
            pieces -- A list of pieces on a board.
            turn -- Game turn, red or black.
            selected -- Any piece is selected or not; Boolean type.
            valid_moves -- A dictionary includes valid moves and skipped pieces
            pieces_left_red -- Number of red pieces left.
            pieces_left_black -- Number of black pieces left.
            a_turtle -- Create a turtle object.
        '''
        self.pieces = []
        self.create_pieces()
        self.turn = "black"
        self.selected = None
        self.valid_moves = {}
        self.pieces_left_red = self.pieces_left_black = 12
        self.a_turtle = turtle.Turtle()
        self.a_turtle.color("black", "white")

    def create_pieces(self):
        '''
        create_pieces -- Creates initiaive pieces; 12 reds and 12 blacks.
                         It creats a matrix(list of list) with 0 indicating
                         cells without pieces.
        Parameters:
            self -- The current GameState object.
        '''
        for i in range(ROWS):
            self.pieces.append([])
            for j in range(COLS):
                if (i + j) % 2 == 0:
                    self.pieces[i].append(0)
                elif i < 3:
                    self.pieces[i].append(Piece(i, j, "black"))
                elif i > 4:
                    self.pieces[i].append(Piece(i, j, "red"))
                else:
                    self.pieces[i].append(0)

    def draw_pieces(self):
        '''
        draw_pieces -- Draw pieces.
        Parameters:
            self -- The current GameState object.
        '''
        for i in range(ROWS):
            for j in range(COLS):
                if self.pieces[i][j] != 0:
                    self.pieces[i][j].draw_piece()

    def get_piece(self, row, col):
        '''
        get_piece -- Get a piece based on its row and column.
        Parameters:
            self -- The current GameState object.
            row -- A row where the piece locates in.
            col -- A col where the piece locates in.
        Return:
            A piece object corresponding to row and col.
        '''
        return self.pieces[row][col]

    def turn_change(self):
        '''
        urn_change -- Change turn.
        Parameters:
            self -- The current GameState object.
        '''
        self.valid_moves = {}
        print(self.valid_moves, "valid moves")
        if self.turn == "red":
            return "black"
        else:
            return "red"

    def remove(self, skipped):
        '''
        remove -- Remove pieces that are skipped.
        Parameters:
            self -- The current GameState object.
            skipped -- Pieces that captured, a list of Piece object.
        '''
        for item in skipped:
            if item != 0:
                if item.color == "red":
                    self.pieces_left_red -= 1
                elif item.color == "black":
                    self.pieces_left_black -= 1
                self.pieces[item.row][item.col] = 0

    def draw_valid_move(self, moves):
        '''
        draw_valid_move -- Draw blue squares indicating valid moves.
        Parameters:
            self -- The current GameState object.
            moves -- A dictionary indicating valid moves; (row, col) of valid
                     move as key while a list of captured pieces as value.
        '''
        board_size = ROWS * SQUARE_SIZE
        for key in moves:
            i_row, i_col = key
            self.a_turtle.setposition(i_col * SQUARE_SIZE - board_size / 2,
                                      i_row * SQUARE_SIZE - board_size / 2)
            self.draw_square(SQUARE_SIZE, "blue")

    def draw_square(self, size, fill_color):
        '''
        Function -- draw_square
            Draw a square given side size.
        Parameters:
            self -- The current GameState object.
            size -- The length of each side of the square.
            fill_color -- Filled color of the square
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

    def move_a_piece_on_game(self, to_row, to_col, piece):
        '''
        move_a_piece_on_game -- Move a piece on a board. Change
                                corresponding coordinates.
        Parameters:
            self -- The current GameState object.
            to_row -- A row that the piece wants to move to
            to_col -- A col that the piece wants to move to
            piece -- A Piece object that is going to move.
        '''
        if piece != 0 and piece.color == self.turn:
            self.pieces[piece.row][piece.col], self.pieces[to_row][to_col] = \
                self.pieces[to_row][to_col], self.pieces[piece.row][piece.col]
            self.pieces[to_row][to_col].move(to_row, to_col)

    def select(self, x, y):
        '''
        select -- Select a piece or moving destination cell.
        Parameters:
            self -- The current GameState object.
            x -- X coordinate that come from onclick function.
            y -- Y ccoordinate that come from onclick function.
        Returns:
            True if a piece is selected. Otherwise, False.
        '''
        row = int((y + COLS * SQUARE_SIZE / 2) // SQUARE_SIZE)
        col = int((x + COLS * SQUARE_SIZE / 2) // SQUARE_SIZE)
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.search_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        '''
        _move -- Take a validate move.
        Parameters:
            self -- The current GameState object.
            row -- A row that the piece gonna move to.
            col -- A col that the piece gonna to move to.
        Returns:
            True if a move really occurs. Otherwise, False.
        '''
        piece = self.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.move_a_piece_on_game(row, col, self.selected)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.remove(skipped)
            self.turn = self.turn_change()
            return True
        else:
            return False

    def update(self, x, y):
        '''
        update -- Update display every turn.
        Parameters:
            self -- The current GameState object.
            x -- X coordinate that come from onclick function.
            y -- Y ccoordinate that come from onclick function.
        '''
        board = Board()
        self.select(x, y)
        board.draw_chess_quares()
        self.draw_valid_move(self.valid_moves)
        self.draw_pieces()
        if self.isWinner() is not None:
            self.isWinner()

    def search_valid_moves(self, current_piece):
        '''
        valid_move -- Create a dictionary indicating valid moves and skipped
                      pieces.
        Parameters:
            self -- The current GameState object.
            current_piece -- Current piece. The piece that click on it.
        Return:
            A dictionary with valid moves as key, and a list of skipped pieces
            as value
        '''
        if isinstance(current_piece, Piece):
            valid_moves_dic = {}
            left = current_piece.col - 1
            right = current_piece.col + 1
            row = current_piece.row
            if current_piece.color == "red" or current_piece.isKing:
                valid_moves_dic.update(self.left_search_moves(row - 1,
                                       max(row-3, -1), -1, current_piece.color,
                                       left))
                valid_moves_dic.update(self.right_search_moves(row - 1,
                                       max(row-3, -1), -1, current_piece.color,
                                       right))
            if current_piece.color == "black" or current_piece.isKing:
                valid_moves_dic.update(self.left_search_moves(row + 1,
                                       min(row + 3, ROWS), 1,
                                       current_piece.color, left))
                valid_moves_dic.update(self.right_search_moves(row + 1,
                                       min(row + 3, ROWS), 1,
                                       current_piece.color, right))
            return valid_moves_dic

    def left_search_moves(self, start, end, step, color, left, skipped=[]):
        '''
        left_search_moves -- Search valid cells and skipped cells in the left
                             direction.
        Parameters:
            self -- The current GameState object.
            start -- The begining row of a search.
            end --  The ending row of a search
            step -- -1 for upward search direction and 1 for downward search
                    direction
            color -- Piece color
            skipped -- A list of pieces skipped. Initiated is a empty list.
        Return:
            A dictionary with valid moves as key, and a list of skipped pieces
            as value
        '''
        moves = {}
        last = []
        for i in range(start, end, step):
            if left < 0:
                break
            current = self.pieces[i][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i, left)] = last + skipped
                else:
                    moves[(i, left)] = last
                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    moves.update(self.left_search_moves(i + step, row, step,
                                 color, left - 1, skipped=last))
                    moves.update(self.right_search_moves(i + step, row, step,
                                 color, left + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def right_search_moves(self, start, end, step, color, right, skipped=[]):
        '''
        right_search_moves -- Search valid cells and skipped cells in the right
                             direction.
        Parameters:
            self -- The current GameState object.
            start -- The begining row of a search.
            end --  The ending row of a search
            step -- -1 for upward search direction and 1 for downward search
                    direction
            color -- Piece color
            skipped -- A list of pieces skipped. Initiated is a empty list.
        Return:
            A dictionary with valid moves as key, and a list of skipped pieces
            as value
        '''
        moves = {}
        last = []
        for i in range(start, end, step):
            if right >= COLS:
                break

            current = self.pieces[i][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i, right)] = last + skipped
                else:
                    moves[(i, right)] = last
                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    moves.update(self.left_search_moves(i + step, row, step,
                                 color, right - 1, skipped=last))
                    moves.update(self.right_search_moves(i + step, row, step,
                                 color, right + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def isWinner(self):
        '''
        isWinner -- Check if there is a winner. If so, print the winter.
        Parameters:
            self -- The current GameState object.
        '''
        if self.pieces_left_black <= 0:
            self.a_turtle.setposition(- COLS * SQUARE_SIZE / 2 +
                                      SQUARE_SIZE, 0)
            self.a_turtle.color('yellow')
            self.a_turtle.write("The winner is Red", font=("Arial", 30,
                                'normal', 'bold', 'italic'))
        if self.pieces_left_red <= 0:
            self.a_turtle.setposition(-COLS*SQUARE_SIZE / 2 + SQUARE_SIZE, 0)
            self.a_turtle.color('yellow')
            self.a_turtle.write("The winner is black", font=("Arial", 30,
                                'normal', 'bold', 'italic'))
        return None
