import unittest
import chessapi


class TestGame(unittest.TestCase):
    def test_holistically(self):
        player_1 = chessapi.Player(chessapi.WHITE)
        player_2 = chessapi.Player(chessapi.BLACK)
        game = chessapi.Game(player_1, player_2)
        game.move(chessapi.DiscreteVector(3, 1), (3, 3), player_1)
        game.move((1, 7), chessapi.DiscreteVector(2, 5), player_2)
        self.assertEqual(type(game.peice_at_position((2, 5))), chessapi.Knight)
        self.assertIsNone(game.peice_at_position(chessapi.DiscreteVector(3, 1)))

    def test_player_validation(self):
        game = chessapi.Game(
            chessapi.Player(chessapi.WHITE),
            chessapi.Player(chessapi.BLACK)
        )
        with self.assertRaises(chessapi.exceptions.PlayerNotInGameError):
            game.move(
                chessapi.DiscreteVector(3, 1), (3, 3),
                chessapi.Player(chessapi.BLACK)
            )

    def test_player_turn_validation(self):
        player = chessapi.Player(chessapi.BLACK)
        game = chessapi.Game(chessapi.Player(chessapi.WHITE), player)
        with self.assertRaises(chessapi.exceptions.NotPlayersTurnError):
            game.move((1, 7), chessapi.DiscreteVector(2, 5), player)

    def test_player_colour_validation(self):
        player_1 = chessapi.Player(chessapi.WHITE)
        player_2 = chessapi.Player(chessapi.BLACK)
        with self.assertRaises(chessapi.exceptions.IncorrectPlayerColourError):
            game = chessapi.Game(player_2, player_1)


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

    def test_base_can_make_move(self):
        with self.assertRaises(TypeError):
            self.piece.can_make_move(7)
        with self.assertRaises(TypeError):
            self.piece.can_make_move([6, 9])
        with self.assertRaises(TypeError):
            self.piece.can_make_move("82")
        self.assertFalse(
            self.piece.can_make_move(chessapi.DiscreteVector(1, 2))
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
