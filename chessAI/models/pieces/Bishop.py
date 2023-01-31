from models.pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, color, new_pos, image):
        Piece.__init__(self, color, new_pos, image)
        self.value = 300

    def is_valid_move(self, prev_pos, new_pos):
        if not Piece.is_valid_move(self, prev_pos, new_pos):
            return False
        return Piece.is_valid_diagonal_move(self, prev_pos, new_pos)
