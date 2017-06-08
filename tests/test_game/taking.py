import chessapi


def test_taking(self):
    self.game.reset_board()
    # Place a white pawn in a position to take a black pawn.
    self.game.set_piece_at_position(
        (0, 5),
        chessapi.Pawn((0, 5), chessapi.WHITE, self.game)
    )
    self.game.display_ascii_board_representation()
    # Take the black pawn.
    self.game.move((0, 5), (1, 6), self.player_1)
    self.game.display_ascii_board_representation()
    # Assert that their is now a white piece at that position.
    self.assertEqual(self.game.piece_at_position((1, 6)).colour, chessapi.WHITE)
