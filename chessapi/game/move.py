from ..discrete_vector import DiscreteVector
from ..player import Player
from ..utilities import iterable_to_discrete_vector
from ..exceptions import NoPieceAtPositionError, NotPlayersTurnError, \
    PlayerNotInGameError, InvalidMoveError, OtherPlayersPieceError
from ..constants import WHITE, BLACK
from ..pieces import King


def move(
        self,
        position_to_move_from,
        position_to_move_to,
        player,
        ignore_check=False
    ):
    # If ignore check is true this will not stop a player from moving into
    # check. You probably don't want to set it to true.
    # Check the the positions being fed in are positions.
    position_to_move_from = iterable_to_discrete_vector(position_to_move_from)
    position_to_move_to = iterable_to_discrete_vector(position_to_move_to)
    if (
        not isinstance(position_to_move_from, DiscreteVector) or
        not isinstance(position_to_move_to, DiscreteVector)
    ):
        raise TypeError(
            'position_to_move_to and position_to_move_from must be '
            'DiscreteVector instances or iterables containing two integers'
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

    # Check that the piece belongs to the player.
    if player.colour != piece_to_move.colour:
        raise OtherPlayersPieceError(
            'player {} does not control {} and so cannot move it'.format(
                player,
                piece_to_move
            )
        )

    move = position_to_move_to - position_to_move_from
    if move in piece_to_move.get_current_moves(ignore_check):
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

    # If we aren't ignoring check, if any king has just been put in check, make
    # sure they know it.
    if not ignore_check:
        for piece in self.pieces:
            if isinstance(piece, King) and self.is_in_check(piece.colour):
                piece.has_moved_or_been_in_check = True
