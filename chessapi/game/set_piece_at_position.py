from ..discrete_vector import DiscreteVector
from ..pieces import Piece
from ..utilities import iterable_to_discrete_vector


def set_piece_at_position(self, position, piece_to_add):
    position = iterable_to_discrete_vector(position)
    if not isinstance(position, DiscreteVector):
        raise TypeError('position must be a DiscreteVector')

    if not isinstance(piece_to_add, Piece) and piece_to_add is not None:
        raise TypeError('piece_to_add must be None or an instance of Piece')

    for piece in self.pieces:
        if piece.position == position:
            self.pieces.remove(piece)
            
    if piece_to_add is not None:
        self.pieces.append(piece_to_add)
