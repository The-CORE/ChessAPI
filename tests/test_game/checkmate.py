import chessapi


def test_white_in_checkmate_check(self):
    self.game.reset_board()
    # Remove the pawn in front of the white king.
    self.game.set_piece_at_position((4, 1), None)
    # Remove the white king's knight.
    self.game.set_piece_at_position((6, 0), None)
    # Replace the bishop and the queen with pawns
    self.game.set_piece_at_position(
        (5, 0),
        chessapi.Pawn((5, 0), chessapi.WHITE, self.game)
    )
    self.game.set_piece_at_position(
        (3, 0),
        chessapi.Pawn((3, 0), chessapi.WHITE, self.game)
    )
    # Add a black rook, putting the white king in checkmate.
    self.game.pieces.append(
        chessapi.Rook((4, 3), chessapi.BLACK, self.game)
    )
    self.assertTrue(self.game.is_in_checkmate(chessapi.WHITE))


def test_black_in_checkmate_check(self):
    # Same as above, but for the opposite colours.
    self.game.reset_board()
    self.game.set_piece_at_position((4, 6), None)
    self.game.set_piece_at_position((6, 7), None)
    self.game.set_piece_at_position(
        (5, 7),
        chessapi.Pawn((5, 7), chessapi.BLACK, self.game)
    )
    self.game.set_piece_at_position(
        (3, 7),
        chessapi.Pawn((3, 7), chessapi.BLACK, self.game)
    )
    self.game.pieces.append(
        chessapi.Rook((4, 3), chessapi.WHITE, self.game)
    )
    self.assertTrue(self.game.is_in_checkmate(chessapi.BLACK))
