from ..constants import COLOURS


def is_in_checkmate(self, colour):
    if not colour in COLOURS:
        raise ValueError('colour must be in colours {}'.format(COLOURS))

    # Because moves that leave a player in check are not in their current moves
    # lists, a player is in checkmate if there are in check, and they have no
    # possible moves.
    return self.is_in_check(colour) and self.colour_has_no_moves(colour)
