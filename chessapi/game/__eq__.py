def __eq__(self, object_to_compare_to):
    if not isinstance(object_to_compare_to, type(self)):
        return NotImplemented
    print('pieces', self.pieces == object_to_compare_to.pieces)
    print('colour', self.colour_for_next_turn == object_to_compare_to.colour_for_next_turn)
    print('white_player', self.white_player == object_to_compare_to.white_player)
    print('black_player', self.black_player == object_to_compare_to.black_player)
    return (
        self.pieces == object_to_compare_to.pieces and
        self.colour_for_next_turn == object_to_compare_to.colour_for_next_turn \
            and
        self.white_player == object_to_compare_to.white_player and
        self.black_player == object_to_compare_to.black_player
    )
