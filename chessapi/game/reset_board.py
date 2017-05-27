from ..pieces import Pawn, Rook, Knight, Bishop, Queen, King
from ..constants import WHITE, BLACK


def reset_board(self):
    self.pieces = []
    # Add pawns:
    for x_coordinate in range(0, 8):
        self.pieces.append(Pawn((x_coordinate, 1), WHITE, self))
        self.pieces.append(Pawn((x_coordinate, 6), BLACK, self))
    # Add rooks:
    for x_coordinate in (0, 7):
        self.pieces.append(Rook((x_coordinate, 0), WHITE, self))
        self.pieces.append(Rook((x_coordinate, 7), BLACK, self))
    # Add knights:
    for x_coordinate in (1, 6):
        self.pieces.append(Knight((x_coordinate, 0), WHITE, self))
        self.pieces.append(Knight((x_coordinate, 7), BLACK, self))
    # Add bishops:
    for x_coordinate in (2, 5):
        self.pieces.append(Bishop((x_coordinate, 0), WHITE, self))
        self.pieces.append(Bishop((x_coordinate, 7), BLACK, self))
    # Add queens:
    self.pieces.append(Queen((3, 0), WHITE, self))
    self.pieces.append(Queen((3, 7), BLACK, self))
    # Add kings:
    self.pieces.append(King((4, 0), WHITE, self))
    self.pieces.append(King((4, 7), BLACK, self))
