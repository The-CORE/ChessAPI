import json
from ..constants import COLOURS


def get_colour_moves_json(self, colour):
    if not colour in COLOURS:
        raise ValueError('colour must be in colours {}'.format(COLOURS))

    data_to_be_jsoned = []
    for piece in self.pieces:
        if piece.colour == colour:
            for move in piece.get_current_moves()
                data_to_be_jsoned.append(
                    ((piece.position.x, piece.position.y), (move.x, move.y))
                )

    return json.dumps(data_to_be_jsoned)
