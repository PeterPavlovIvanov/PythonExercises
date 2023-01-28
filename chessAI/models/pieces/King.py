import GlobalVariables
from models.pieces.Piece import Piece
from models.pieces.Rook import Rook


class King(Piece):

    def is_safe_from_enemy_rook_or_Queen(self, npx, npy, matrix):
        # up check
        r = npx - 1
        c = npy
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Rook' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or rook
                    return False  # it is invalid
                else:  # if it is not enemy queen or rook
                    break  # we consider it valid move depending on queens or rooks
            r = r - 1

        # down check
        r = npx + 1
        c = npy
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Rook' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or rook
                    return False  # it is invalid
                else:  # if it is not enemy queen or rook
                    break  # we consider it valid move depending on queens or rooks
            r = r + 1

        # left check
        r = npx
        c = npy - 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Rook' in str(type(cur_piece)) or 'Queen' in str(type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or rook
                    return False  # it is invalid
                else:  # if it is not enemy queen or rook
                    break  # we consider it valid move depending on queens or rooks
            c = c - 1

        # right check
        r = npx
        c = npy + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Rook' in str(type(cur_piece)) or 'Queen' in str(type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or rook
                    return False  # it is invalid
                else:  # if it is not enemy queen or rook
                    break  # we consider it valid move depending on queens or rooks
            c = c + 1

        return True

    def is_safe_from_enemy_bishop_or_Queen(self, npx, npy, matrix):
        # up left check
        r = npx - 1
        c = npy - 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r - 1
            c = c - 1

        # down right check
        r = npx + 1
        c = npy + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r + 1
            c = c + 1

        # up right check
        r = npx - 1
        c = npy + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r - 1
            c = c + 1

        # down left check
        r = npx + 1
        c = npy - 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r + 1
            c = c - 1

        return True

    def is_safe_from_enemy_knights(self, npx, npy, matrix):
        if 0 <= npx - 2 < 8 and 0 <= npy - 1 < 8 and matrix[npx - 2][npy - 1] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx - 2][npy - 1])) and matrix[npx - 2][npy - 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx - 2 < 8 and 0 <= npy + 1 < 8 and matrix[npx - 2][npy + 1] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx - 2][npy + 1])) and matrix[npx - 2][npy + 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx - 1 < 8 and 0 <= npy + 2 < 8 and matrix[npx - 1][npy + 2] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx - 1][npy + 2])) and matrix[npx - 1][npy + 2].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 1 < 8 and 0 <= npy + 2 < 8 and matrix[npx + 1][npy + 2] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx + 1][npy + 2])) and matrix[npx + 1][npy + 2].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 2 < 8 and 0 <= npy + 1 < 8 and matrix[npx + 2][npy + 1] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx + 2][npy + 1])) and matrix[npx + 2][npy + 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 2 < 8 and 0 <= npy - 1 < 8 and matrix[npx + 2][npy - 1] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx + 2][npy - 1])) and matrix[npx + 2][npy - 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 1 < 8 and 0 <= npy - 2 < 8 and matrix[npx + 1][npy - 2] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx + 1][npy - 2])) and matrix[npx + 1][npy - 2].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx - 1 < 8 and 0 <= npy - 2 < 8 and matrix[npx - 1][npy - 2] is not None:  # found piece on the board
            if 'Knight' in str(type(matrix[npx - 1][npy - 2])) and matrix[npx - 1][npy - 2].color != self.color:  # and its enemy knight
                return False

        return True

    def is_safe_from_enemy_pawn(self, npx, npy, matrix):
        direction = 1 if self.color == 'black' else -1

        if 0 <= npy - 1 < 8 and (0 <= npx + direction < 8):  # don't go out of the matrix
            if matrix[npx + direction][npy - 1] is not None:  # find a piece
                if 'Pawn' in str(type(matrix[npx + direction][npy - 1])) \
                        and matrix[npx + direction][npy - 1].color != self.color:  # if it's enemy pawn
                    return False

        if 0 <= npy + 1 < 8 and (0 <= npx + direction < 8):  # don't go out of the matrix
            if matrix[npx + direction][npy + 1] is not None:  # there is a piece on the right down/up from the new pos
                if 'Pawn' in str(type(matrix[npx + direction][npy + 1])) \
                        and matrix[npx + direction][npy + 1].color != self.color:  # if it's enemy pawn
                    return False

        return True

    def is_safe_from_enemy_king(self, npx, npy, matrix):
        if 0 <= npx - 1 < 8 and 0 <= npy - 1 < 8:           # out of board check
            if matrix[npx - 1][npy - 1] is not None:        # top left piece found
                if 'King' in str(type(matrix[npx - 1][npy - 1])) and matrix[npx - 1][npy - 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx < 8 and 0 <= npy - 1 < 8:               # out of board check
            if matrix[npx][npy - 1] is not None:            # top center piece found
                if 'King' in str(type(matrix[npx][npy - 1])) and matrix[npx][npy - 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx + 1 < 8 and 0 <= npy - 1 < 0:           # out of board check
            if matrix[npx + 1][npy - 1] is not None:        # top right piece found
                if 'King' in str(type(matrix[npx + 1][npy - 1])) and matrix[npx + 1][npy - 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx - 1 < 8 and 0 <= npy < 8:               # out of board check
            if matrix[npx - 1][npy] is not None:            # center left piece found
                if 'King' in str(type(matrix[npx - 1][npy])) and matrix[npx - 1][npy].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx + 1 < 8 and 0 <= npy < 8:               # out of board check
            if matrix[npx + 1][npy] is not None:            # center right piece found
                if 'King' in str(type(matrix[npx + 1][npy])) and matrix[npx + 1][npy].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx - 1 < 8 and 0 <= npy + 1 < 8:           # out of board check
            if matrix[npx - 1][npy + 1] is not None:        # bot left piece found
                if 'King' in str(type(matrix[npx - 1][npy + 1])) and matrix[npx - 1][npy + 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx < 8 and 0 <= npy + 1 < 8:               # out of board check
            if matrix[npx][npy + 1] is not None:            # bot center piece found
                if 'King' in str(type(matrix[npx][npy + 1])) and matrix[npx][npy + 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx + 1 < 8 and 0 <= npy + 1 < 8:           # out of board check
            if matrix[npx + 1][npy + 1] is not None:        # bot right piece found
                if 'King' in str(type(matrix[npx + 1][npy + 1])) and matrix[npx + 1][npy + 1].color != self.color:  # and it's enemy king
                    return False

        return True

    def is_going_into_free_square(self, new_pos, matrix):
        npx = new_pos[0]
        npy = new_pos[1]
        if not self.is_safe_from_enemy_king(npx, npy, matrix):
            return False

        if not self.is_safe_from_enemy_pawn(npx, npy, matrix):
            return False

        if not self.is_safe_from_enemy_knights(npx, npy, matrix):
            return False

        if not self.is_safe_from_enemy_bishop_or_Queen(npx, npy, matrix):
            return False

        if not self.is_safe_from_enemy_rook_or_Queen(npx, npy, matrix):
            return False

        return True

    def is_valid_move(self, prev_pos, new_pos, matrix):
        if not Piece.is_valid_move(self, prev_pos, new_pos, matrix):
            return False

        if not self.is_going_into_free_square(new_pos, matrix):
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
            if self.color == 'white':  # save kings pos
                GlobalVariables.w_king_position = new_pos
            else:
                GlobalVariables.b_king_position = new_pos
            return True  # it is a valid move

        if not self.moved:  # if we haven't moved the king and we try to castle
            if ppy + 2 == npy and ppx == npx:  # we try to castle king side
                if not self.is_going_into_free_square((ppx, ppy + 1), matrix) \
                        or not self.is_going_into_free_square((ppx, ppy + 2), matrix):  # king's way is attacked
                    return False
                if matrix[ppx][ppy + 1] is None and matrix[ppx][ppy + 2] is None:  # square on the right of the king are empty
                    if self.color == 'white':  # white king castle
                        if isinstance(matrix[7][7], Rook):  # we have a piece on the right that is a rook
                            if not matrix[7][7].moved:  # if the rook hasn't moved
                                matrix[7][7].position = (7, 5)
                                matrix[7][5] = matrix[7][7]
                                matrix[7][7] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
                    else:
                        if isinstance(matrix[0][7], Rook):  # we have a piece on the right that is a rook
                            if not matrix[0][7].moved:  # if the rook hasn't moved
                                matrix[0][7].position = (0, 5)
                                matrix[0][5] = matrix[0][7]
                                matrix[0][7] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
            elif ppy - 2 == npy and ppx == npx:  # we try to castle queen side
                if not self.is_going_into_free_square((ppx, ppy - 1), matrix) \
                        or not self.is_going_into_free_square((ppx, ppy - 2), matrix):  # king's way is attacked
                    return False
                if matrix[ppx][ppy - 1] is None and matrix[ppx][ppy - 2] is None:  # square on the right of the king are empty
                    if self.color == 'white':  # white king castle
                        if isinstance(matrix[7][0], Rook):  # we have a piece on the right that is a rook
                            if not matrix[7][0].moved:  # if the rook hasn't moved
                                matrix[7][0].position = (7, 3)
                                matrix[7][3] = matrix[7][0]
                                matrix[7][0] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
                    else:
                        if isinstance(matrix[0][0], Rook):  # we have a piece on the right that is a rook
                            if not matrix[0][0].moved:  # if the rook hasn't moved
                                matrix[0][0].position = (0, 3)
                                matrix[0][3] = matrix[0][0]
                                matrix[0][0] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
        return False
