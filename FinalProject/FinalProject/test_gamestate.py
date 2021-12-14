from gamestate import GameState


def test_init():
    piece_board = GameState()
    assert(piece_board.selected is None)
    assert(piece_board.turn == "black")


def test_create_pieces():
    piece_board = GameState()
    assert(len(piece_board.pieces) == 8)
    assert(len(piece_board.pieces[0]) == 8)
    assert(piece_board.pieces_left_black == 12)
    assert(piece_board.pieces_left_red == 12)


def test_get_piece():
    piece_board = GameState()
    assert(piece_board.get_piece(0, 4) == 0)
    assert(piece_board.get_piece(0, 3).color == "black")
    assert(piece_board.get_piece(0, 0) == 0)


def test_turn_change():
    piece_board = GameState()
    assert(piece_board.turn == "black")
    piece_board.turn_change()
    assert(piece_board.turn == "black")


def test_remove():
    piece_board = GameState()
    piece = piece_board.get_piece(0, 3)
    piece_board.remove([piece])
    assert(piece_board.get_piece(0, 3) == 0)
