import chessapi


def test_castling_right(self):
    self.game.reset_board()
    # Clear the pieces in between the king and the castle.
    self.game.set_piece_at_position((5, 0), None)
    self.game.set_piece_at_position((6, 0), None)
    # Attempt to castle.
    self.game.move((4, 0), (6, 0), self.player_1)
    # Assert that the castle has moved too.
    self.assertEqual(
        type(self.game.piece_at_position((5, 0))), chessapi.Rook
    )


def test_castling_left(self):
    self.game.reset_board()
    # Clear the pieces in between the king and the castle.
    self.game.set_piece_at_position((1, 0), None)
    self.game.set_piece_at_position((2, 0), None)
    self.game.set_piece_at_position((3, 0), None)
    # Attempt to castle.
    self.game.move((4, 0), (2, 0), self.player_1)
    # Assert that the castle has moved too.
    self.assertEqual(
        type(self.game.piece_at_position((3, 0))), chessapi.Rook
    )


def test_cant_castle_after_king_has_moved(self):
    self.game.reset_board()
    # Clear the necessary pieces.
    self.game.set_piece_at_position((1, 0), None)
    self.game.set_piece_at_position((2, 0), None)
    self.game.set_piece_at_position((3, 0), None)
    self.game.set_piece_at_position((5, 0), None)
    # Move the king.
    self.game.move((4, 0), (5, 0), self.player_1)
    # Set it to be white's turn again.
    self.game.colour_for_next_turn = chessapi.WHITE
    # Assert that the king cannot castle.
    with self.assertRaises(chessapi.InvalidMoveError):
        self.game.move((5, 0), (3, 0), self.player_1)


def test_cant_castle_after_having_been_in_check(self):
    self.game.reset_board()
    # Place a black rook directly in front of the white king's pawn.
    self.game.pieces.append(
        chessapi.Rook((4, 2), chessapi.BLACK, self.game)
    )
    # Remove the bishop and knight in the way of castling.
    self.game.set_piece_at_position((5, 0), None)
    self.game.set_piece_at_position((6, 0), None)
    # Assert that you can castle now.
    self.assertTrue(
        chessapi.DiscreteVector(2, 0) in \
            self.game.piece_at_position((4, 0)).get_current_moves()
    )
    # Set it to be blacks turn.
    self.game.colour_for_next_turn = chessapi.BLACK
    # Take the white king's pawn with the black rook (putting white in
    # check).
    self.game.move((4, 2), (4, 1), self.player_2)
    # Assert that white is in check.
    self.assertTrue(self.game.is_in_check(chessapi.WHITE))
    # Assert that white cannot castle.
    self.assertFalse(
        chessapi.DiscreteVector(2, 0) in \
            self.game.piece_at_position((4, 0)).get_current_moves()
    )
