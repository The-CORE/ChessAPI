import chessapi


def test_player_validation(self):
    self.game.reset_board()
    with self.assertRaises(chessapi.PlayerNotInGameError):
        self.game.move(
            chessapi.DiscreteVector(3, 1),
            (3, 3),
            chessapi.Player(chessapi.BLACK)
        )


def test_player_turn_validation(self):
    self.game.reset_board()
    with self.assertRaises(chessapi.NotPlayersTurnError):
        self.game.move((1, 7), chessapi.DiscreteVector(2, 5), self.player_2)


def test_player_colour_validation(self):
    player_1 = chessapi.Player(chessapi.WHITE)
    player_2 = chessapi.Player(chessapi.BLACK)
    with self.assertRaises(chessapi.IncorrectPlayerColourError):
        game = chessapi.Game(player_2, player_1)


def test_player_cannot_move_other_players_pieces(self):
    self.game.reset_board()
    with self.assertRaises(chessapi.OtherPlayersPieceError):
        self.game.move((0, 6), (0, 4), self.player_1)
