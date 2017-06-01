import unittest
import chessapi


class TestJson(unittest.TestCase):
    def test_json(self):
        player_1 = chessapi.Player(chessapi.WHITE)
        player_2 = chessapi.Player(chessapi.BLACK)
        first_game = chessapi.Game(player_1, player_2)

        first_game.move((1, 0), (2, 2), player_1)

        json_representation = first_game.get_json_from_board()
        second_game = chessapi.Game(player_1, player_2)
        second_game.build_board_from_json(json_representation)
        second_game.colour_for_next_turn = chessapi.BLACK

        self.assertEqual(
            first_game.piece_at_position((2, 2)),
            second_game.piece_at_position((2, 2))
        )
