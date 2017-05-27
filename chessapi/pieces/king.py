from .piece import Piece
from ..discrete_vector import DiscreteVector


class King(Piece):
    def __repr__(self):
        return 'King({}, {}, {})'.format(self.position, self.colour, self.game)

    _base_moves = []
    # range(-1, 2) will run for -1, 0, and 1.
    for x_coordinate in range(-1, 2):
        for y_coordinate in range(-1, 2):
            if x_coordinate == 0 and y_coordinate == 0:
                continue
            _base_moves.append(DiscreteVector(x_coordinate, y_coordinate))
