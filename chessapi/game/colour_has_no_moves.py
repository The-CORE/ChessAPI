from ..constants import COLOURS


def colour_has_no_moves(self, colour):
    if not colour in COLOURS:
        raise ValueError('colour must be in colours {}'.format(COLOURS))

    moves_of_colour = []
    for piece in self.pieces:
        if piece.colour == colour:
            moves_of_colour += piece.get_current_moves()

    return len(moves_of_colour) == 0
