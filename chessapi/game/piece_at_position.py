from ..discrete_vector import DiscreteVector
from ..utilities import iterable_to_discrete_vector


def piece_at_position(self, position):
    position = iterable_to_discrete_vector(position)
    if not isinstance(position, DiscreteVector):
        raise TypeError(
            'position must be a DiscreteVector or an iterable containing two '
            'integers'
        )
    for piece in self.pieces:
        if piece.position == position:
            # If there is a piece in the position requested, return it.
            return piece
    # Otherwise, return None.
    return None
