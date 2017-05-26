from .player import Player
from .constants import WHITE, BLACK, COLOURS, BOARD_WIDTH, BOARD_HEIGHT
from .discrete_vector import DiscreteVector
from .utilities import tuple_to_discrete_vector
from .exceptions import IncorrectPlayerColourError, NotPlayersTurnError, \
    PlayerNotInGameError

class Game:
    def __init__(self, white_player, black_player):
        if (
                not isinstance(white_player, Player) or
                not isinstance(black_player, Player)
        ):
            raise TypeError(
                'both white_player and black_player must be Player instances'
            )
        if white_player.colour != WHITE or black_player.colour != BLACK:
            raise IncorrectPlayerColourError(
                'white_player must have colour set to \'white\', and '
                'black_player must have colour set to \'black\''
            )
        self.white_player = white_player
        self.black_player = black_player
        self.reset_board()
        self.colour_for_next_turn = WHITE

    def reset_board(self):
        self.peices = []
        # Add pawns:
        for x_coordinate in range(0, 8):
            self.peices.append(Pawn((x_coordinate, 1), WHITE, self))
            self.peices.append(Pawn((x_coordinate, 6), BLACK, self))
        # Add rooks:
        for x_coordinate in (0, 7):
            self.peices.append(Rook((x_coordinate, 0), WHITE, self))
            self.peices.append(Rook((x_coordinate, 7), BLACK, self))
        # Add knights:
        for x_coordinate in (1, 6):
            self.peices.append(Knight((x_coordinate, 0), WHITE, self))
            self.peices.append(Knight((x_coordinate, 7), BLACK, self))
        # Add bishops:
        for x_coordinate in (2, 5):
            self.peices.append(Bishop((x_coordinate, 0), WHITE, self))
            self.peices.append(Bishop((x_coordinate, 7), BLACK, self))
        # Add queens:
        self.peices.append(Queen((3, 0), WHITE, self))
        self.peices.append(Queen((3, 7), BLACK, self))
        # Add kings:
        self.peices.append(King((4, 0), WHITE, self))
        self.peices.append(King((4, 7), BLACK, self))

    def peice_at_position(self, position):
        position = tuple_to_discrete_vector(position)
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')
        for peice in self.peices:
            if peice.position == position:
                # If there is a peice in the position requested, return it.
                return peice
        # Otherwise, return None.
        return None

    def move(self, position_to_move_from, position_to_move_to, player):
        position_to_move_from = tuple_to_discrete_vector(position_to_move_from)
        position_to_move_to = tuple_to_discrete_vector(position_to_move_to)
        if (
            not isinstance(position_to_move_from, DiscreteVector) or
            not isinstance(position_to_move_to, DiscreteVector)
        ):
            raise TypeError(
                'position_to_move_to and position_to_move_from must be '
                'DiscreteVector instances'
            )

        piece_to_move = self.peice_at_position(position_to_move_from)
        if piece_to_move is None:
            raise NoPieceAtPositionError(
                'there is no peice at position_to_move_from'
            )

        if not isinstance(player, Player):
            raise TypeError('player must be a Player instance')

        if player != self.white_player and player != self.black_player:
            raise PlayerNotInGameError('player is not in this game')

        if player.colour != self.colour_for_next_turn:
            raise NotPlayersTurnError('it is not the turn of player')

        move = position_to_move_to - position_to_move_from
        if piece_to_move.can_make_move(move):
            piece_to_move.position = position_to_move_to
            if self.colour_for_next_turn == WHITE:
                self.colour_for_next_turn = BLACK
            else: # self.colour_for_next_turn == BLACK
                self.colour_for_next_turn = WHITE
        else:
            raise InvalidMoveError(
                'the item at position_to_move_from cannot move to '
                'position_to_move_to'
            )


class Piece:
    _all_moves = []

    def __init__(self, position, colour, game):
        position = tuple_to_discrete_vector(position)
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')
        if not colour in COLOURS:
            raise ValueError('colour must be in {}'.format(str(COLOURS)))
        if not isinstance(game, Game):
            raise TypeError('game must be a Game instance')
        self.position = position
        self.colour = colour

    def can_make_move(self, move):
        # This needs many more qualifications.
        move = tuple_to_discrete_vector(move)
        if not isinstance(move, DiscreteVector):
            raise TypeError('move must be a DiscreteVector')
        final_position = self.position + move
        if (
                move not in self._all_moves
                or not 0 <= final_position.x < BOARD_WIDTH
                or not 0 <= final_position.y < BOARD_HEIGHT
        ):
            return False
        return True

    def get_valid_moves(self):
        valid_moves = []
        for move in self._all_moves:
            if self.can_make_move(move):
                valid_moves.append(move)


class Pawn(Piece):
    def __init__(self, position, colour, game):
        super(Pawn, self).__init__(position, colour, game)
        if colour == WHITE:
            self._all_moves = [
                DiscreteVector(0, 1),
                DiscreteVector(0, 2),
                DiscreteVector(1, 1),
                DiscreteVector(-1, 1)
            ]
        elif colour == BLACK:
            self._all_moves = [
                DiscreteVector(0, -1),
                DiscreteVector(0, -2),
                DiscreteVector(1, -1),
                DiscreteVector(-1, -1)
            ]


class Rook(Piece):
    _all_moves = []
    for displacement in range(-7, 8):
        if displacement != 0:
            _all_moves.append(DiscreteVector(0, displacement))
            _all_moves.append(DiscreteVector(displacement, 0))


class Knight(Piece):
    _all_moves = [
        DiscreteVector(-1, 2),
        DiscreteVector(1, 2),
        DiscreteVector(2, 1),
        DiscreteVector(2, -1),
        DiscreteVector(1, -2),
        DiscreteVector(-1, -2),
        DiscreteVector(-2, -1),
        DiscreteVector(-2, 1)
    ]


class Bishop(Piece):
    _all_moves = []
    for distance in range(1, 8):
        _all_moves.append(DiscreteVector(distance, distance))
        _all_moves.append(DiscreteVector(-distance, distance))
        _all_moves.append(DiscreteVector(-distance, -distance))
        _all_moves.append(DiscreteVector(distance, -distance))


class Queen(Piece):
    _all_moves = Bishop._all_moves + Rook._all_moves


class King(Piece):
    _all_moves = []
    # range(-1, 2) will run for -1, 0, and 1.
    for x_coordinate in range(-1, 2):
        for y_coordinate in range(-1, 2):
            if x_coordinate == 0 and y_coordinate == 0:
                continue
            _all_moves.append(DiscreteVector(x_coordinate, y_coordinate))
