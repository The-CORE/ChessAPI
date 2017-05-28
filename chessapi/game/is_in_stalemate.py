from ..constants import COLOURS


def is_in_stalemate(self, colour):
    if not colour in COLOURS:
        raise ValueError('colour must be in colours {}'.format(COLOURS))

    # A player is in stalemate if they have no valid moves, and are NOT in
    # check.
    return not self.is_in_check(colour) and self.colour_has_no_moves(colour)
