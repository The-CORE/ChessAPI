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

    def __repr__(self):
        return 'DiscreteVector({}, {})'.format(self.x, self.y)
