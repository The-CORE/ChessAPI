import json
from ..constants import BOARD_WIDTH, BOARD_HEIGHT, WHITE, BLACK
from ..exceptions import InvalidJsonError
from ..pieces import Pawn, Rook, Knight, Bishop, Queen, King


strings_pieces = {
    'P': Pawn,
    'R': Rook,
    'N': Knight,
    'B': Bishop,
    'Q': Queen,
    'K': King
}

strings_colours = {
    'W': WHITE,
    'B': BLACK
}


def build_board_from_json(self, json_string_representation):
    """
    This function takes a json string representing the location of pieces on
    the board (in the style of one outputted from get_json_from_board), and
    places the pieces on this board in those locations. It modifies this board
    in place, and only modifies the pieces.
    """

    try:
        piece_coordinate_map = json.loads(json_string_representation)
    except ValueError:
        raise InvalidJsonError('invalid json')

    for x_coordinate in range(BOARD_WIDTH):
        for y_coordinate in range(BOARD_HEIGHT):
            try:
                piece_representation = piece_coordinate_map[x_coordinate][\
                    y_coordinate]
            except KeyError:
                raise InvalidJsonError('incorrect key mappings')

            position = (x_coordinate, y_coordinate)

            if piece_representation == 'None':
                self.set_piece_at_position(position, None)
                continue

            colour = strings_colours[piece_representation[0]]
            piece_type = strings_pieces[piece_representation[1]]
            piece_to_set = piece_type(position, colour, self)
            self.set_piece_at_position(position, piece_to_set)
