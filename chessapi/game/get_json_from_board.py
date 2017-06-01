import json
from ..constants import BOARD_WIDTH, BOARD_HEIGHT


def get_json_from_board(self):
    two_dimensional_list_representation = []
    for x_coordinate in range(BOARD_WIDTH):
        column = []
        for y_coordinate in range(BOARD_HEIGHT):
            column.append(
                str(self.piece_at_position((x_coordinate, y_coordinate)))
            )
        two_dimensional_list_representation.append(column)
    return json.dumps(two_dimensional_list_representation)
