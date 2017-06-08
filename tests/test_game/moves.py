import chessapi


def test_move(self):
    self.game.reset_board()
    self.game.move(chessapi.DiscreteVector(3, 1), (3, 3), self.player_1)
    self.game.move((1, 7), chessapi.DiscreteVector(2, 5), self.player_2)
    self.assertEqual(
        type(self.game.piece_at_position((2, 5))),
        chessapi.Knight
    )
    self.assertIsNone(
        self.game.piece_at_position(chessapi.DiscreteVector(3, 1))
    )


def test_moving_onto_own_pieces(self):
    self.game.reset_board()
    with self.assertRaises(chessapi.InvalidMoveError):
        self.game.move((0, 0), (0, 1), self.player_1)


def test_cant_move_over_pieces(self):
    self.game.reset_board()
    # Assert that the rook can't move straight over the pawns
    with self.assertRaises(chessapi.InvalidMoveError):
        self.game.move((0, 0), (0, 7), self.player_1)


def test_knight_can_move_over_pieces(self):
    self.game.reset_board()
    # Assert that the knight can jump right over the pawns in front of it
    # (without erroring).
    self.game.move((1, 0), (2, 2), self.player_1)


def test_pawn_can_take_diagonally(self):
    self.game.reset_board()
    self.game.pieces.append(
        chessapi.Pawn((0, 2), chessapi.BLACK, self.game)
    )
    self.game.move((1, 1), (0, 2), self.player_1)


def test_pawn_cant_normally_move_diagonally(self):
    self.game.reset_board()
    with self.assertRaises(chessapi.InvalidMoveError):
        self.game.move((3, 1), (4, 2), self.player_1)
