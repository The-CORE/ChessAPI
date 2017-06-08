import unittest
import chessapi


class TestGame(unittest.TestCase):
    from .pawn_getting_to_end import \
        test_black_pawn_getting_to_the_end_becomes_a_queen, \
        test_white_pawn_getting_to_the_end_becomes_a_queen
    from .validation import test_player_validation, \
        test_player_turn_validation, test_player_colour_validation, \
        test_player_cannot_move_other_players_pieces
    from .castling import test_castling_right, test_castling_left, \
        test_cant_castle_after_king_has_moved, \
        test_cant_castle_after_having_been_in_check
    from .moves import test_move, test_moving_onto_own_pieces, \
        test_cant_move_over_pieces, test_knight_can_move_over_pieces, \
        test_pawn_can_take_diagonally, test_pawn_cant_normally_move_diagonally
    from .check import test_white_in_check_check, test_black_in_check_check, \
        test_cant_move_into_check
    from .checkmate import test_white_in_checkmate_check, \
        test_black_in_checkmate_check
    from .stalemate import test_stalemate_check
    from .taking import test_taking

    def setUp(self):
        self.player_1 = chessapi.Player(chessapi.WHITE)
        self.player_2 = chessapi.Player(chessapi.BLACK)
        self.game = chessapi.Game(self.player_1, self.player_2)
