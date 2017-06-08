import chessapi


def test_stalemate_check(self):
    self.game.reset_board()
    # Remove all of blacks pieces.
    for x_coordinate in range(chessapi.constants.BOARD_WIDTH):
        for y_coordinate in (6, 7):
            self.game.set_piece_at_position(
                (x_coordinate, y_coordinate),
                None
            )
    # Place a black king in the corner.
    self.game.pieces.append(
        chessapi.King((7, 7), chessapi.BLACK, self.game)
    )
    # Put it in a stalemate with white rooks.
    self.game.pieces.append(
        chessapi.Rook((6, 5), chessapi.WHITE, self.game)
    )
    self.game.pieces.append(
        chessapi.Rook((5, 6), chessapi.WHITE, self.game)
    )
    self.assertTrue(self.game.is_in_stalemate(chessapi.BLACK))
