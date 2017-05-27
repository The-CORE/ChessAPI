from .piece import Piece
from ..discrete_vector import DiscreteVector


class Knight(Piece):
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
    symbol = 'N'
    # Yes, I know knight begins with a k, but, so does a king.

    def __repr__(self):
        return 'Knight({}, {}, {})'.format(
            self.position,
            self.colour,
            self.game
        )

    def can_move_along_path(self, move):
        return True
