import chessapi


def test_black_pawn_getting_to_the_end_becomes_a_queen(self):
    self.game.reset_board()
    self.game.set_piece_at_position((0, 0), None)
    self.game.set_piece_at_position((0, 1), None)
    self.game.pieces.append(
        chessapi.Pawn((0, 1), chessapi.BLACK, self.game)
    )
    self.game.colour_for_next_turn = chessapi.BLACK
    self.game.move((0, 1), (0, 0), self.player_2)
    self.assertEqual(
        type(self.game.piece_at_position((0, 0))),
        chessapi.Queen
    )
    self.assertEqual(
        self.game.piece_at_position((0, 0)).colour,
        chessapi.BLACK
    )


def test_white_pawn_getting_to_the_end_becomes_a_queen(self):
    self.game.reset_board()
    self.game.set_piece_at_position((7, 7), None)
    self.game.set_piece_at_position((7, 6), None)
    self.game.pieces.append(
        chessapi.Pawn((7, 6), chessapi.WHITE, self.game)
    )
    self.game.move((7, 6), (7, 7), self.player_1)
    self.assertEqual(
        type(self.game.piece_at_position((7, 7))),
        chessapi.Queen
    )
    self.assertEqual(
        self.game.piece_at_position((7, 7)).colour,
        chessapi.WHITE
    )
