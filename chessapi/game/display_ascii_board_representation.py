from ..constants import BOARD_WIDTH, BOARD_HEIGHT

def display_ascii_board_representation(self):
    print()
    for row in reversed(range(0, BOARD_HEIGHT)):
        row_text = ' ' + str(row) + ' '
        for column in range(0, BOARD_WIDTH):
            piece = self.piece_at_position((column, row))
            if piece is not None:
                row_text += piece.colour[0].upper() + piece.symbol + ' '
            else:
                row_text += '++ '
        print(row_text)
        print()
    print('    ' + '  '.join([str(column) for column in range(BOARD_WIDTH)]))
    print()
