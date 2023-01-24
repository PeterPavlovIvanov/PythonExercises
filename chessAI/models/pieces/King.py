from models.pieces.Piece import Piece


class King(Piece):
    def is_valid_move(self, prev_pos, new_pos, matrix):
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        npx = new_pos[0]
        npy = new_pos[1]
        if 0 < npx > 7 or 0 < npy > 7:  # are we out of the board
            return False  # we leave

        ally = False  # is the new square occupied by an ally
        if not matrix[npx][npy] is None:
            if matrix[npx][npy].color == matrix[ppx][ppy]:
                ally = True

        # if the new pos is exactly one square away and the square is not occupied by an ally
        if abs(npx - ppx) <= 1 and abs(npy - ppy) <= 1 and not ally:
            return True  # it is a valid move

        return False
