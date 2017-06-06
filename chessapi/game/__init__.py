from ..player import Player
from ..constants import WHITE, BLACK
from ..exceptions import IncorrectPlayerColourError

class Game:
    def __init__(self, white_player, black_player):
        if (
                not isinstance(white_player, Player) or
                not isinstance(black_player, Player)
        ):
            raise TypeError(
                'both white_player and black_player must be Player instances'
            )
        if white_player.colour != WHITE and black_player.colour != BLACK:
            raise IncorrectPlayerColourError(
                'white_player must have colour set to \'white\', and '
                'black_player must have colour set to \'black\''
            )
        self.white_player = white_player
        self.black_player = black_player
        self.reset_board()
        self.colour_for_next_turn = WHITE

    from .reset_board import reset_board
    from .set_piece_at_position import set_piece_at_position
    from .piece_at_position import piece_at_position
    from .move import move
    from .display_ascii_board_representation import \
        display_ascii_board_representation
    from .is_in_check import is_in_check
    from .is_in_checkmate import is_in_checkmate
    from .colour_has_no_moves import colour_has_no_moves
    from .is_in_stalemate import is_in_stalemate
    from .get_json_from_board import get_json_from_board
    from .build_board_from_json import build_board_from_json
    from .get_colour_moves_json import get_colour_moves_json
