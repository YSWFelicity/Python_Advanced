from piece import Piece


def test_init():
    piece = Piece(1, 2, "red")
    assert(piece.row == 1)
    assert(piece.col == 2)
    assert(piece.color == "red")
    assert(piece.isKing is False)


def test_move():
    piece = Piece(1, 1, "red")
    assert(piece.row == 1)
    assert(piece.col == 1)
    piece.move(5, 6)
    assert(piece.row == 5)
    assert(piece.col == 6)


def test_make_king():
    piece = Piece(1, 1, "red")
    assert(piece.isKing is False)
    piece._make_king()
    assert(piece.isKing is True)
