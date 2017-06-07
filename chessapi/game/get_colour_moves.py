import json
from ..constants import COLOURS


def get_colour_moves(self, colour):
    if not colour in COLOURS:
        raise ValueError('colour must be in colours {}'.format(COLOURS))

    colour_moves = []
    for piece in self.pieces:
        if piece.colour == colour:
            for move in piece.get_current_moves():
                colour_moves.append(
                    ((piece.position.x, piece.position.y), (move.x, move.y))
                )

    return colour_moves
