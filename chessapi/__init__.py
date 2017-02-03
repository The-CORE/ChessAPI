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
                or not 0 <= final_position.x <= BOARD_WIDTH
                or not 0 <= final_position.y <= BOARD_HEIGHT
        ):
            return False
        return True

    def get_valid_moves(self):
        valid_moves = []
        for move in self._all_moves:
            if self.can_make_move(move):
                valid_moves.append(move)


class Pawn(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


class DiscreteVector:
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError('x must be an int')
        if not isinstance(y, int):
            raise TypeError('y must be an int')
        self.x = x
        self.y = y

    def __add__(self, object_to_add_to):
        if not isinstance(object_to_add_to, DiscreteVector):
            return NotImplemented
        return DiscreteVector(
            self.x + object_to_add_to.x,
            self.y + object_to_add_to.y
        )

    def __sub__(self, object_to_subtract_from_self):
        if not isinstance(object_to_subtract_from_self, DiscreteVector):
            return NotImplemented
        return DiscreteVector(
            self.x - object_to_subtract_from_self.x,
            self.y - object_to_subtract_from_self.y
        )

    def __mul__(self, object_to_multiply_self_by):
        if not isinstance(object_to_multiply_self_by, int):
            return NotImplemented
        return DiscreteVector(
            self.x * object_to_multiply_self_by,
            self.y * object_to_multiply_self_by
        )

    def __rmul__(self, object_to_multiply_self_by):
        return self.__mul__(object_to_multiply_self_by)

    def __truediv__(self, object_to_divide_self_by):
        '''
        Returns the DiscreteVector divided by the number given, but rounds the
        result (using the python round function (i.e. to the nearest even
        number)) the result, to keep x and y as integers.
        '''
        if not isinstance(object_to_divide_self_by, int):
            return NotImplemented
        return DiscreteVector(
            round(self.x / object_to_divide_self_by),
            round(self.y / object_to_divide_self_by)
)
