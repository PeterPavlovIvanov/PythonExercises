from models.pieces.Piece import Piece


class Queen(Piece):
    def __init__(self, color, new_pos, image):
        Piece.__init__(self, color, new_pos, image)
        self.value = 900

    def is_valid_move(self, prev_pos, new_pos):
        if not Piece.is_valid_move(self, prev_pos, new_pos):
            return False
        return Piece.is_valid_direct_move(self, prev_pos, new_pos)\
               or Piece.is_valid_diagonal_move(self, prev_pos, new_pos)
