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
        self.game.set_piece_at_position(
            (4, 1),
            chessapi.Rook(
                (4, 1),
                chessapi.BLACK,
                self.game
            )
        )
        self.assertTrue(self.game.is_in_check(chessapi.WHITE))

    def test_black_in_check_check(self):
        self.game.reset_board()
        self.game.set_piece_at_position(
            (4, 6),
            chessapi.Rook(
                (4, 6),
                chessapi.WHITE,
                self.game
            )
        )
        self.assertTrue(self.game.is_in_check(chessapi.BLACK))

    def test_white_in_checkmate_check(self):
        pass

    def test_black_in_checkmate_check(self):
        pass

    def test_checkmate_validation(self):
        pass

    def test_stalemate_validation(self):
        pass

    def test_cant_castle_after_having_been_in_check(self):
        pass

    def test_cant_move_into_check(self):
        pass

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


class TestPieces(unittest.TestCase):
    def setUp(self):
        self.piece = chessapi.Piece(
            chessapi.DiscreteVector(0, 0),
            chessapi.WHITE,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )

    def test_initialisation(self):
        """
        Makes sure that basic initialisation of the pieces does not raise any
        errors.
        """
        chessapi.Pawn(
            chessapi.DiscreteVector(0, 0),
            chessapi.WHITE,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )
        chessapi.Rook(
            chessapi.DiscreteVector(0, 0),
            chessapi.BLACK,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )
        chessapi.Knight(
            chessapi.DiscreteVector(0, 0),
            chessapi.WHITE,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )
        chessapi.Bishop(
            chessapi.DiscreteVector(0, 0),
            chessapi.BLACK,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )
        chessapi.Queen(
            chessapi.DiscreteVector(0, 0),
            chessapi.WHITE,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )
        chessapi.King(
            chessapi.DiscreteVector(0, 0),
            chessapi.BLACK,
            chessapi.Game(
                chessapi.Player(chessapi.WHITE),
                chessapi.Player(chessapi.BLACK)
            )
        )

class TestDiscreteVector(unittest.TestCase):
    def test_initialisation(self):
        with self.assertRaises(TypeError):
            chessapi.DiscreteVector(0.452, 5), TypeError
        with self.assertRaises(TypeError):
            chessapi.DiscreteVector(0, 'asd'), TypeError

    def test_addition(self):
        a = chessapi.DiscreteVector(1, 2)
        b = chessapi.DiscreteVector(3, -5)
        c = a + b
        self.assertEqual(c.x, 4)
        self.assertEqual(c.y, -3)

    def test_subtraction(self):
        a = chessapi.DiscreteVector(-23, 17)
        b = chessapi.DiscreteVector(-8, 12)
        c = a - b
        self.assertEqual(c.x, -15)
        self.assertEqual(c.y, 5)

    def test_addition_validation(self):
        a = chessapi.DiscreteVector(1, 2)
        with self.assertRaises(TypeError):
            b = a + 5
        with self.assertRaises(TypeError):
            b = a + 'fgasfdg'
        with self.assertRaises(TypeError):
            b = a + 0.2342345667

    def test_subtraction_validation(self):
        a = chessapi.DiscreteVector(8, -2)
        with self.assertRaises(TypeError):
            b = a - 3
        with self.assertRaises(TypeError):
            b = a - 'Dadfasdfhukj.ad'
        with self.assertRaises(TypeError):
            b = a - 2334.678467

    def test_multiplication(self):
        a = chessapi.DiscreteVector(-6, 7)
        b = a * -9
        self.assertEqual(b.x, 54)
        self.assertEqual(b.y, -63)
        c = 2 * b
        self.assertEqual(c.x, 108)
        self.assertEqual(c.y, -126)

    def test_multiplication_validation(self):
        a = chessapi.DiscreteVector(16, -42)
        with self.assertRaises(TypeError):
            b = a * a
        with self.assertRaises(TypeError):
            b = a * 'eeeeeeeeeeeeedssad'
        with self.assertRaises(TypeError):
            b = a * 2334.678467

    def test_division(self):
        a = chessapi.DiscreteVector(-6, 7)
        b = a / 2
        self.assertEqual(b.x, -3)
        self.assertEqual(b.y, 4)

    def test_division_validation(self):
        a = chessapi.DiscreteVector(3, -2)
        with self.assertRaises(TypeError):
            b = a / a
        with self.assertRaises(TypeError):
            b = a / ';"/756fa'
        with self.assertRaises(TypeError):
            b = a / 3.14295
        with self.assertRaises(TypeError):
            b = 5 / a


unittest.main()
