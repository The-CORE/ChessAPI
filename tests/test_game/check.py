import chessapi


def test_white_in_check_check(self):
    self.game.reset_board()
    # Replace the pawn in front of the white king with a black rook.
    self.game.set_piece_at_position(
        (4, 1),
        chessapi.Rook(
            (4, 1),
            chessapi.BLACK,
            self.game
        )
    )
    # Assert that white is now in check.
    self.assertTrue(self.game.is_in_check(chessapi.WHITE))


def test_black_in_check_check(self):
    # Same as above except with a black king and a white rook.
    self.game.reset_board()
    self.game.set_piece_at_position(
        (4, 6),
        chessapi.Rook((4, 6), chessapi.WHITE, self.game)
    )
    self.assertTrue(self.game.is_in_check(chessapi.BLACK))


def test_cant_move_into_check(self):
    self.game.reset_board()
    # Remove the pawn in front of the black king.
    self.game.set_piece_at_position((4, 6), None)
    # Place a white pawn in a position to attack the empty square now in
    # front of the black king.
    self.game.pieces.append(
        chessapi.Pawn((3, 5), chessapi.WHITE, self.game)
    )
    # Assert that the black king has no possible moves.
    self.assertEqual(
        self.game.piece_at_position((4, 7)).get_current_moves(),
        []
    )
