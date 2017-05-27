from .piece import Piece
from ..discrete_vector import DiscreteVector


class Rook(Piece):
    def __repr__(self):
        return 'Rook({}, {}, {})'.format(self.position, self.colour, self.game)

    def __init__(self, position, colour, game):
        super(Rook, self).__init__(position, colour, game)
        self.has_moved = False

    def make_move(self, move):
        super(Rook, self).make_move(move)
        self.has_moved = True

    _base_moves = []
    for displacement in range(-7, 8):
        if displacement != 0:
            _base_moves.append(DiscreteVector(0, displacement))
            _base_moves.append(DiscreteVector(displacement, 0))
