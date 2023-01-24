from models.pieces.Piece import Piece


class Bishop(Piece):
    def is_valid_move(self, prev_pos, new_pos, matrix):
        return Piece.is_valid_diagonal_move(self, prev_pos, new_pos, matrix)
