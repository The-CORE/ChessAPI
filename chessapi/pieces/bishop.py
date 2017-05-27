from .piece import Piece
from ..discrete_vector import DiscreteVector

class Bishop(Piece):
    def __repr__(self):
        return 'Bishop({}, {}, {})'.format(
            self.position,
            self.colour,
            self.game
        )

    _base_moves = []
    for distance in range(1, 8):
        _base_moves.append(DiscreteVector(distance, distance))
        _base_moves.append(DiscreteVector(-distance, distance))
        _base_moves.append(DiscreteVector(-distance, -distance))
        _base_moves.append(DiscreteVector(distance, -distance))
