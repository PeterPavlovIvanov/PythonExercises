from models.pieces.Piece import Piece


class Queen(Piece):
    def is_valid_move(self, prev_pos, new_pos, matrix):
        return Piece.is_valid_direct_move(self, prev_pos, new_pos, matrix)\
               or Piece.is_valid_diagonal_move(self, prev_pos, new_pos, matrix)
