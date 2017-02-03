import unittest
import chessapi


class TestGame(unittest.TestCase):
    pass


class TestPiece(unittest.TestCase):
    def setUp(self):
        super(TestPiece, self).setUp()
        self.piece = chessapi.Piece(chessapi.DiscreteVector(0, 0), 'white')

    def test_can_make_move(self):
        with self.assertRaises(TypeError):
            self.piece.can_make_move(7)
        with self.assertRaises(TypeError):
            self.piece.can_make_move([6, 9])
        with self.assertRaises(TypeError):
            self.piece.can_make_move("82")
        self.assertFalse(
            self.piece.can_make_move(chessapi.DiscreteVector(1, 2))
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
