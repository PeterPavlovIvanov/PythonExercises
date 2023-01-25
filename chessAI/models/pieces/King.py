import GlobalVariables
from models.pieces.Piece import Piece
from models.pieces.Rook import Rook


class King(Piece):

    def save_king_pos(self, new_pos):
        if self.color == 'white':
            GlobalVariables.w_king_position = new_pos
        else:
            GlobalVariables.b_king_position = new_pos

    def is_valid_move(self, prev_pos, new_pos, matrix):
        if not Piece.is_valid_move(self, prev_pos, new_pos, matrix):
            return False

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
            if not self.moved:
                self.moved = True
            self.save_king_pos(new_pos)  # save the king's position
            return True  # it is a valid move

        if not self.moved:  # if we haven't moved the king and we try to castle
            if ppy + 2 == npy and ppx == npx:  # we try to castle king side
                if matrix[ppx][ppy + 1] is None and matrix[ppx][ppy + 2] is None:  # square on the right of the king are empty
                    if self.color == 'white':  # white king castle
                        if isinstance(matrix[7][7], Rook):  # we have a piece on the right that is a rook
                            if not matrix[7][7].moved:  # if the rook hasn't moved
                                matrix[7][7].position = (7, 5)
                                matrix[7][5] = matrix[7][7]
                                matrix[7][7] = None  # we delete the rook from the bottom right square
                                self.save_king_pos(new_pos)  # save the king's position
                                return True
                    else:
                        if isinstance(matrix[0][7], Rook):  # we have a piece on the right that is a rook
                            if not matrix[0][7].moved:  # if the rook hasn't moved
                                matrix[0][7].position = (0, 5)
                                matrix[0][5] = matrix[0][7]
                                matrix[0][7] = None  # we delete the rook from the bottom right square
                                self.save_king_pos(new_pos)  # save the king's position
                                return True
            elif ppy - 2 == npy and ppx == npx: # we try to castle queen side
                if matrix[ppx][ppy - 1] is None and matrix[ppx][ppy - 2] is None:  # square on the right of the king are empty
                    if self.color == 'white':  # white king castle
                        if isinstance(matrix[7][0], Rook):  # we have a piece on the right that is a rook
                            if not matrix[7][0].moved:  # if the rook hasn't moved
                                matrix[7][0].position = (7, 3)
                                matrix[7][3] = matrix[7][0]
                                matrix[7][0] = None  # we delete the rook from the bottom right square
                                self.save_king_pos(new_pos)  # save the king's position
                                return True
                    else:
                        if isinstance(matrix[0][0], Rook):  # we have a piece on the right that is a rook
                            if not matrix[0][0].moved:  # if the rook hasn't moved
                                matrix[0][0].position = (0, 3)
                                matrix[0][3] = matrix[0][0]
                                matrix[0][0] = None  # we delete the rook from the bottom right square
                                self.save_king_pos(new_pos)  # save the king's position
                                return True
        return False
