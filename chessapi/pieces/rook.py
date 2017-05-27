from .piece import Piece
from ..discrete_vector import DiscreteVector


class Rook(Piece):
    def __repr__(self):
        return 'Rook({}, {}, {})'.format(self.position, self.colour, self.game)

    _base_moves = []
    for displacement in range(-7, 8):
        if displacement != 0:
            _base_moves.append(DiscreteVector(0, displacement))
            _base_moves.append(DiscreteVector(displacement, 0))
