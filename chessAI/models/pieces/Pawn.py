from models.pieces.Piece import Piece


class Pawn(Piece):
    def is_valid_move(self, prev_pos, new_pos, matrix):
        if not Piece.is_valid_move(self, prev_pos, new_pos, matrix):
            return False
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        npx = new_pos[0]
        npy = new_pos[1]

        if ppx == 1 and self.color == 'black' or ppx == 6 and self.color == 'white':  # if pawn hasn't moved
            if (ppx + 2 == npx and ppy == npy and self.color == 'black') \
                    or (ppx - 2 == npx and ppy == npy and self.color == 'white'):  # and tries to double move
                return True  # we allow the double move

        if (ppx + 1 == npx and ppy == npy and self.color == 'black') \
                or (ppx - 1 == npx and ppy == npy and self.color == 'white'):  # tries to move forward
            if matrix[npx][npy] is None:  # and there is no one there
                return True  # we allow one square move

        if (ppx + 1 == npx and (ppy - 1 == npy or ppy + 1 == npy) and self.color == 'black') \
                or (ppx - 1 == npx and (ppy - 1 == npy or ppy + 1 == npy) and self.color == 'white'):  # tries to capture diagonally
            if matrix[npx][npy] is not None:  # there is some piece there
                if matrix[npx][npy].color != self.color:  # is an enemy
                    return True  # we allow to capture

        # todo en pasant

        return False
