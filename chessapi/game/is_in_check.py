from ..constants import COLOURS, WHITE, BLACK
from ..pieces import King
from ..exceptions import TwoKingsWithSameColourOnBoardError

def is_in_check(self, colour):
    if not colour in COLOURS:
        raise ValueError('colour must be in {}'.format(COLOURS))\

    king = None
    for piece in self.pieces:
        if isinstance(piece, King) and piece.colour == colour:
            if king is not None:
                # There are two kings of the same colour on the board.
                raise TwoKingsWithSameColourOnBoardError(
                    'there are two kings with color {} on the board'.format(
                        colour
                    )
                )
            king = piece
            
    if king is None:
        # This is no king of colour colour on the board.
        raise NoKingOnBoard(
            'there is no king of colour {} on the board'.format(
                colour
            )
        )

    for piece in self.pieces:
        if piece.colour == colour:
            # You can't be in check from your own pieces.
            continue

        for move in piece.current_moves:
            final_position = piece.position + move
            if final_position == king.position:
                # If it could take the king next turn, the king is in check.
                return True

    return False
