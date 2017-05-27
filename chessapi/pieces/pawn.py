from .piece import Piece
from ..constants import WHITE, BLACK
from ..discrete_vector import DiscreteVector


class Pawn(Piece):
    def __repr__(self):
        return 'Pawn({}, {}, {})'.format(self.position, self.colour, self.game)

    def __init__(self, position, colour, game):
        super(Pawn, self).__init__(position, colour, game)
        if colour == WHITE:
            self._base_moves = [
                DiscreteVector(0, 1),
                DiscreteVector(0, 2),
                DiscreteVector(1, 1),
                DiscreteVector(-1, 1)
            ]
        elif colour == BLACK:
            self._base_moves = [
                DiscreteVector(0, -1),
                DiscreteVector(0, -2),
                DiscreteVector(1, -1),
                DiscreteVector(-1, -1)
            ]

    symbol = 'P'
