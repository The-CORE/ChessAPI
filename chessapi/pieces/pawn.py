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
            ]
        elif colour == BLACK:
            self._base_moves = [
                DiscreteVector(0, -1),
                DiscreteVector(0, -2),
            ]

    symbol = 'P'

    def get_specifically_valid_moves(self, base_moves):
        """
        This will add the diagonal attack moves if there are pieces to take
        there.
        """
        valid_moves = base_moves.copy()
        move_y_coordinate = 1 if self.colour == WHITE else -1
        for move_x_coordinate in (1, -1):
            move = DiscreteVector(move_x_coordinate, move_y_coordinate)
            final_position = self.position + move
            if self.game.piece_at_position(final_position) is not None:
                valid_moves.append(
                    DiscreteVector(move_x_coordinate, move_y_coordinate)
                )
        return valid_moves
