import unittest
import chessapi


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = chessapi.Player(chessapi.WHITE)
        self.player_2 = chessapi.Player(chessapi.BLACK)
        self.game = chessapi.Game(self.player_1, self.player_2)


    def test_holistically(self):
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

    def test_player_validation(self):
        self.game.reset_board()
        with self.assertRaises(chessapi.PlayerNotInGameError):
            self.game.move(
                chessapi.DiscreteVector(3, 1),
                (3, 3),
                chessapi.Player(chessapi.BLACK)
            )

    def test_player_turn_validation(self):
        self.game.reset_board()
        with self.assertRaises(chessapi.NotPlayersTurnError):
            self.game.move((1, 7), chessapi.DiscreteVector(2, 5), self.player_2)

    def test_player_colour_validation(self):
        player_1 = chessapi.Player(chessapi.WHITE)
        player_2 = chessapi.Player(chessapi.BLACK)
        with self.assertRaises(chessapi.IncorrectPlayerColourError):
            game = chessapi.Game(player_2, player_1)

    def test_moving_onto_own_pieces(self):
        self.game.reset_board()
        with self.assertRaises(chessapi.InvalidMoveError):
            self.game.move((0, 0), (0, 1), self.player_1)

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

    def test_player_cannot_move_other_players_pieces(self):
        self.game.reset_board()
        with self.assertRaises(chessapi.OtherPlayersPieceError):
            self.game.move((0, 6), (0, 4), self.player_1)
