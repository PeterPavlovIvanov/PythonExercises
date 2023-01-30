from models.pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, prev_pos, new_pos, matrix):
        Piece.__init__(self, prev_pos, new_pos, matrix)
        self.value = 300

    def is_valid_move(self, prev_pos, new_pos, matrix):
        if not Piece.is_valid_move(self, prev_pos, new_pos, matrix):
            return False
        return Piece.is_valid_diagonal_move(self, prev_pos, new_pos, matrix)
