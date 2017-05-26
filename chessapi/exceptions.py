class ChessAPIError(Exception):
    pass


class PlayerNotInGameError(ChessAPIError):
    pass


class NotPlayersTurnError(ChessAPIError):
    pass


class IncorrectPlayerColourError(ChessAPIError):
    pass


class NoPieceAtPositionError(ChessAPIError):
    pass


class InvalidMoveError(ChessAPIError):
    pass
