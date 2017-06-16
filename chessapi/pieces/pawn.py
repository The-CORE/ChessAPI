from .piece import Piece
from .queen import Queen
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
        valid_moves = base_moves.copy()

        # Remove any moves that would take a piece, as the only moves in valid
        # moves so far are those that move directly forward, and pawns cannot
        # take with these moves. Also remove the two square move if the pawn is
        # not on the starting square.
        for move in base_moves:
            final_position = self.position + move
            if self.game.piece_at_position(final_position) is not None:
                valid_moves.remove(move)
                continue

            game_starting_position_y = 1 if self.colour == WHITE else 6
            if abs(move.y) == 2 and self.position.y != game_starting_position_y:
                # If this is a two square move but this piece isn't at the
                # starting square...
                valid_moves.remove(move)

        # Add the diagonal attack moves if there are pieces to take there.
        move_y_coordinate = 1 if self.colour == WHITE else -1
        for move_x_coordinate in (1, -1):
            move = DiscreteVector(move_x_coordinate, move_y_coordinate)
            final_position = self.position + move
            if self.game.piece_at_position(final_position) is not None:
                valid_moves.append(
                    DiscreteVector(move_x_coordinate, move_y_coordinate)
                )

        return valid_moves

    def make_move(self, move):
        super(Pawn, self).make_move(move)
        other_side_y_coordinate = 7 if self.colour == WHITE else 0
        if self.position.y == other_side_y_coordinate:
            # If the pawn has moved to the furthest side of the board...
            self.game.set_piece_at_position(
                self.position,
                Queen(self.position, self.colour, self.game)
            )
