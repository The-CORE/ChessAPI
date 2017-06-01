from ..discrete_vector import DiscreteVector
from ..pieces import Piece
from ..utilities import iterable_to_discrete_vector


def set_piece_at_position(self, position, piece_to_add):
    position = iterable_to_discrete_vector(position)
    if not isinstance(position, DiscreteVector):
        raise TypeError('position must be a DiscreteVector')

    if not isinstance(piece_to_add, Piece) and piece_to_add is not None:
        raise TypeError('piece_to_add must be None or an instance of Piece')

    pieces_to_remove = []

    for piece in self.pieces:
        print('here', piece in self.pieces)
        if piece.position == position:
            print('there', piece in self.pieces)
            # pieces_to_remove.append(piece)
            self.pieces.remove(piece)
            break

    # print(self.pieces)
    self.display_ascii_board_representation()
    # print(repr(self.piece_at_position((0, 0))))
    # for piece in pieces_to_remove:
    #     print(piece in self.pieces)
    #     self.pieces.remove(piece)

    if piece_to_add is not None:
        self.pieces.add(piece_to_add)
