from ..utilities import iterable_to_discrete_vector
from ..discrete_vector import DiscreteVector
from ..constants import COLOURS


class Piece:
    _base_moves = []

    def __init__(self, position, colour, game):
        position = iterable_to_discrete_vector(position)
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')
        if not colour in COLOURS:
            raise ValueError('colour must be in {}'.format(str(COLOURS)))
        # Note, game is not validated because it makes imports difficult to do
        # that.
        self.position = position
        self.colour = colour
        self.game = game

    @property
    def current_moves(self):
        return self.get_standardly_valid_moves(
            self.get_specifically_valid_moves(self._base_moves)
        )

    def get_standardly_valid_moves(moves_to_validate):
        """
        This function returns a modified version of moves_to_validate that only
        contains valid moves. However, this is only insofar as the generic
        restrictions that affect all pieces. If the ends on the board, and any
        piece that is there has a different colour than this piece, this will
        say it is vlaid, otherwise, it will say it is not.
        """
        valid_moves = []

        def is_valid(move):
            move = iterable_to_discrete_vector(move)
            if not isinstance(move, DiscreteVector):
                raise TypeError(
                    'move must be a DiscreteVector or an iterable with two '
                    'items in it'
                )
            final_position = self.position + move
            piece_to_take = self.game.piece_at_position(final_position)
            colour_of_piece_to_take = None if piece_to_take is None else \
                piece_to_take.colour

            if (
                    0 <= final_position.x < BOARD_WIDTH and
                    0 <= final_position.y < BOARD_HEIGHT and
                    self.colour != colour_of_piece_to_take
            ):
                return True
            return False

        try:
            for move in moves_to_validate:
                if is_valid(move):
                    valid_moves.append(move)
        except TypeError:
            raise TypeError('moves_to_validate must be iterable')

    def make_move(self, move):
        move = iterable_to_discrete_vector(move)
        if not isinstance(move, DiscreteVector):
            raise TypeError(
                'move must be a DiscreteVector or an iterable with two items '
                'in it'
            )

        self.position += move
