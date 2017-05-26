from .constants import COLOURS


class Player:
    def __init__(self, colour):
        if colour not in COLOURS:
            raise ValueError('colour must be in {}'.format(str(COLOURS)))
        self.colour = colour
