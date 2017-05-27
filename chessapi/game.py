from .player import Player
from .constants import WHITE, BLACK, COLOURS, BOARD_WIDTH, BOARD_HEIGHT
from .discrete_vector import DiscreteVector
from .utilities import iterable_to_discrete_vector
from .exceptions import IncorrectPlayerColourError, NotPlayersTurnError, \
    PlayerNotInGameError, InvalidMoveError

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
        self.pieces = []
        # Add pawns:
        for x_coordinate in range(0, 8):
            self.pieces.append(Pawn((x_coordinate, 1), WHITE, self))
            self.pieces.append(Pawn((x_coordinate, 6), BLACK, self))
        # Add rooks:
        for x_coordinate in (0, 7):
            self.pieces.append(Rook((x_coordinate, 0), WHITE, self))
            self.pieces.append(Rook((x_coordinate, 7), BLACK, self))
        # Add knights:
        for x_coordinate in (1, 6):
            self.pieces.append(Knight((x_coordinate, 0), WHITE, self))
            self.pieces.append(Knight((x_coordinate, 7), BLACK, self))
        # Add bishops:
        for x_coordinate in (2, 5):
            self.pieces.append(Bishop((x_coordinate, 0), WHITE, self))
            self.pieces.append(Bishop((x_coordinate, 7), BLACK, self))
        # Add queens:
        self.pieces.append(Queen((3, 0), WHITE, self))
        self.pieces.append(Queen((3, 7), BLACK, self))
        # Add kings:
        self.pieces.append(King((4, 0), WHITE, self))
        self.pieces.append(King((4, 7), BLACK, self))

    def set_piece_at_position(self, position, piece_to_add):
        position = iterable_to_discrete_vector(position)
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')

        if not isinstance(piece_to_add, Piece) and piece_to_add is not None:
            raise TypeError('piece_to_add must be None or an instance of Piece')

        for piece in self.pieces:
            if piece.position == position:
                self.pieces.remove(piece)
        if piece_to_add is not None:
            self.pieces.append(piece_to_add)

    def piece_at_position(self, position):
        position = iterable_to_discrete_vector(position)
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')
        for piece in self.pieces:
            if piece.position == position:
                # If there is a piece in the position requested, return it.
                return piece
        # Otherwise, return None.
        return None

    def move(self, position_to_move_from, position_to_move_to, player):
        # Check the the positions being fed in are positions.
        position_to_move_from = iterable_to_discrete_vector(position_to_move_from)
        position_to_move_to = iterable_to_discrete_vector(position_to_move_to)
        if (
            not isinstance(position_to_move_from, DiscreteVector) or
            not isinstance(position_to_move_to, DiscreteVector)
        ):
            raise TypeError(
                'position_to_move_to and position_to_move_from must be '
                'DiscreteVector instances'
            )

        # Check that there is a piece at the position_to_move_from.
        piece_to_move = self.piece_at_position(position_to_move_from)
        if piece_to_move is None:
            raise NoPieceAtPositionError(
                'there is no piece at {}'.format(position_to_move_from)
            )

        # Check that the player is a Player.
        if not isinstance(player, Player):
            raise TypeError('player must be a Player instance')

        # Check that the player is one of the Players playing this game.
        if player != self.white_player and player != self.black_player:
            raise PlayerNotInGameError(
                'player {} is not in this game'.format(player)
            )

        # Check that it is the players turn.
        if player.colour != self.colour_for_next_turn:
            raise NotPlayersTurnError(
                'it is not the turn of player {}'.format(player)
            )

        move = position_to_move_to - position_to_move_from
        if move in piece_to_move.current_moves:
            # If the piece can make the move, make the move.
            piece_to_move.make_move(move)
            # And toggle the turn.
            if self.colour_for_next_turn == WHITE:
                self.colour_for_next_turn = BLACK
            else: # self.colour_for_next_turn == BLACK
                self.colour_for_next_turn = WHITE
        else:
            raise InvalidMoveError(
                'the {} at {} cannot move to {}'.format(
                    piece_to_move,
                    position_to_move_from,
                    position_to_move_to
                )
            )


class Piece:
    _base_moves = []

    def __init__(self, position, colour, game):
        position = iterable_to_discrete_vector(position)
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')
        if not colour in COLOURS:
            raise ValueError('colour must be in {}'.format(str(COLOURS)))
        if not isinstance(game, Game):
            raise TypeError('game must be a Game instance')
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


class Pawn(Piece):
    def __repr__(self):
        return 'Pawn({}, {}, {})'.format(self.position, self.colour, self.game)

    def __init__(self, position, colour, game):
        super(Pawn, self).__init__(position, colour, game)
        if colour == WHITE:
            self._base_moves = [
                DiscreteVector(0, 1),
                DiscreteVector(0, 2),
                DiscreteVector(1, 1),
                DiscreteVector(-1, 1)
            ]
        elif colour == BLACK:
            self._base_moves = [
                DiscreteVector(0, -1),
                DiscreteVector(0, -2),
                DiscreteVector(1, -1),
                DiscreteVector(-1, -1)
            ]


class Rook(Piece):
    def __repr__(self):
        return 'Rook({}, {}, {})'.format(self.position, self.colour, self.game)

    _base_moves = []
    for displacement in range(-7, 8):
        if displacement != 0:
            _base_moves.append(DiscreteVector(0, displacement))
            _base_moves.append(DiscreteVector(displacement, 0))


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


class Queen(Piece):
    def __repr__(self):
        return 'Queen({}, {}, {})'.format(self.position, self.colour, self.game)

    _base_moves = Bishop._base_moves + Rook._base_moves


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
