from .piece import Piece
from .bishop import Bishop
from .rook import Rook


class Queen(Piece):
    def __repr__(self):
        return 'Queen({}, {}, {})'.format(self.position, self.colour, self.game)

    _base_moves = Bishop._base_moves + Rook._base_moves
