from .piece import Piece
from ..discrete_vector import DiscreteVector
from ..constants import WHITE
from .rook import Rook


class King(Piece):
    def __repr__(self):
        return 'King({}, {}, {})'.format(self.position, self.colour, self.game)

    def __init__(self, position, colour, game):
        super(King, self).__init__(position, colour, game)
        self.has_moved_or_been_in_check = False

    def make_move(self, move):
        super(King, self).make_move(move)
        self.has_moved_or_been_in_check = True
        # If you moved two to the left or right, you just castled, so, move the
        # castle. If this happens without the move actually having been allowed,
        # you will get some weird results, but, you were warned.
        if move.x == -2:
            self.game.piece_at_position((0, self.position.y)).position = \
                DiscreteVector(3, self.position.y)
        if move.x == 2:
            self.game.piece_at_position((7, self.position.y)).position = \
                DiscreteVector(5, self.position.y)


    def get_specifically_valid_moves(self, base_moves):
        """
        This will add castling moves to the list of possible moves provided the
        king has not yet moved or been in check and the rook on that side has
        not moved. These moves may still take it onto friendly pieces, but, if
        that is the case, they will be removed by get_standardly_valid_moves.
        """
        valid_moves = base_moves.copy()
        if not self.has_moved_or_been_in_check:
            for rook_x_coordinate, move_x_coordinate in ((0, -2), (7, 2)):
                if (
                        type(self.game.piece_at_position((rook_x_coordinate, \
                            self.position.y))) == Rook and
                        self.game.piece_at_position((rook_x_coordinate, \
                            self.position.y)).colour == self.colour and
                        not self.game.piece_at_position((rook_x_coordinate, \
                            self.position.y)).has_moved
                ):
                    # If the rook is there, is your colour, and hasn't moved
                    # (and then moved back), you can castle
                    valid_moves.append(DiscreteVector(move_x_coordinate, 0))
        return valid_moves

    _base_moves = []
    # range(-1, 2) will run for -1, 0, and 1.
    for x_coordinate in range(-1, 2):
        for y_coordinate in range(-1, 2):
            if x_coordinate == 0 and y_coordinate == 0:
                continue
            _base_moves.append(DiscreteVector(x_coordinate, y_coordinate))
    symbol = 'K'
