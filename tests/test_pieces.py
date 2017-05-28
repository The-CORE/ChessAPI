import unittest
import chessapi


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
