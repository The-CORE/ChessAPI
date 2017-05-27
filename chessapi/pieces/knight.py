from .piece import Piece
from ..discrete_vector import DiscreteVector


class Knight(Piece):
    def __repr__(self):
        return 'Knight({}, {}, {})'.format(
            self.position,
            self.colour,
            self.game
        )

    _base_moves = [
        DiscreteVector(-1, 2),
        DiscreteVector(1, 2),
        DiscreteVector(2, 1),
        DiscreteVector(2, -1),
        DiscreteVector(1, -2),
        DiscreteVector(-1, -2),
        DiscreteVector(-2, -1),
        DiscreteVector(-2, 1)
    ]

    def can_move_along_path_to_position(self, position):
        return True
