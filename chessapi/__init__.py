from .discrete_vector import DiscreteVector


BOARD_WIDTH = 8
BOARD_HEIGHT = 8
COLOURS = ['white', 'black']


class Game:
    pass


class Piece:
    _all_moves = []

    def __init__(self, position, colour):
        if not isinstance(position, DiscreteVector):
            raise TypeError('position must be a DiscreteVector')
        if not colour in COLOURS:
            raise ValueError('colour must be in {}'.format(str(COLOURS)))
        self.position = position
        self.colour = colour

    def can_make_move(self, move):
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
    def __init__(self, position, colour):
        super(Pawn, self).__init__(position, colour)
        if colour == 'white':
            self._all_moves = [
                DiscreteVector(0, 1),
                DiscreteVector(0, 2),
                DiscreteVector(1, 1),
                DiscreteVector(-1, 1)
            ]
        elif colour == 'black':
            self._all_moves = [
                DiscreteVector(0, -1),
                DiscreteVector(0, -2),
                DiscreteVector(1, -1),
                DiscreteVector(-1, -1)
            ]


class Rook(Piece):
    _all_moves = []
    for i in range(-7, 8):
        if i != 0:
            _all_moves.append(DiscreteVector(0, i))
            _all_moves.append(DiscreteVector(i, 0))


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
    for i in range(1, 8):
        _all_moves.append(DiscreteVector(i, i))
        _all_moves.append(DiscreteVector(-i, i))
        _all_moves.append(DiscreteVector(-i, -i))
        _all_moves.append(DiscreteVector(i, -i))


class Queen(Piece):
    _all_moves = Bishop._all_moves + Rook._all_moves


class King(Piece):
    _all_moves = [
        DiscreteVector(-1, 1),
        DiscreteVector(0, 1),
        DiscreteVector(1, 1),
        DiscreteVector(1, 0),
        DiscreteVector(1, -1),
        DiscreteVector(0, -1),
        DiscreteVector(-1, -1),
        DiscreteVector(-1, 0),
    ]
