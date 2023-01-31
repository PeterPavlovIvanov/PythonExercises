import GlobalVariables
from models.pieces.Piece import Piece
from models.pieces.Rook import Rook


class King(Piece):
    def __init__(self, color, new_pos, image):
        Piece.__init__(self, color, new_pos, image)
        self.value = 100

    def is_safe_from_enemy_rook_or_Queen(self, prev_pos, npx, npy):
        # up check
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        r = npx - 1
        c = npy
        if ppx + 1 == npx and ppy == npy:  # start from the next square if we moved in the opposite direction
            r = r - 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
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
        if ppx - 1 == npx and ppy == npy:  # start from the next square if we moved in the opposite direction
            r = r + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
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
        if ppy + 1 == npy and ppx == npx:  # start from the next square if we moved in the opposite direction
            c = c - 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Rook' in str(type(cur_piece)) or 'Queen' in str(type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or rook
                    return False  # it is invalid
                else:  # if it is not enemy queen or rook
                    break  # we consider it valid move depending on queens or rooks
            c = c - 1

        # right check
        r = npx
        c = npy + 1
        if ppy - 1 == npy and ppx == npx:  # start from the next square if we moved in the opposite direction
            c = c + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Rook' in str(type(cur_piece)) or 'Queen' in str(type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or rook
                    return False  # it is invalid
                else:  # if it is not enemy queen or rook
                    break  # we consider it valid move depending on queens or rooks
            c = c + 1

        return True

    def is_safe_from_enemy_bishop_or_Queen(self, prev_pos, npx, npy):
        # up left check
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        r = npx
        c = npy
        if ppx + 1 == npx and ppy + 1 == npy:  # if we move down right(the opposite direction)
            r = r - 2  # start from the next square
            c = c - 2
        else:
            r = r - 1  # else just continue
            c = c - 1

        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r - 1
            c = c - 1

        # down right check
        r = npx
        c = npy
        if ppx - 1 == npx and ppy - 1 == npy:  # if we move up left(the opposite direction)
            r = r + 2  # start from the next square
            c = c + 2
        else:
            r = r + 1  # else just continue
            c = c + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r + 1
            c = c + 1

        # up right check
        r = npx
        c = npy
        if ppx + 1 == npx and ppy - 1 == npy:  # if we move down left(the opposite direction)
            r = r - 2  # start from the next square
            c = c + 2
        else:
            r = r - 1  # else just continue
            c = c + 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r - 1
            c = c + 1

        # down left check
        r = npx
        c = npy
        if ppx - 1 == npx and ppy + 1 == npy:  # if we move up right(the opposite direction)
            r = r + 2  # start from the next square
            c = c - 2
        else:
            r = r + 1  # else just continue
            c = c - 1
        while True:
            if r < 0 or r > 7 or c < 0 or c > 7:  # out of board = end of loop
                break
            cur_piece = GlobalVariables.board.matrix[r][c]
            if cur_piece is not None:  # piece found
                if ('Bishop' in str(type(cur_piece)) or 'Queen' in str(
                        type(cur_piece))) and cur_piece.color != self.color:  # if enemy queen or bishop
                    return False  # it is invalid
                else:  # if it is not enemy queen or bishop
                    break  # we consider it valid move depending on queens or bishops
            r = r + 1
            c = c - 1

        return True

    def is_safe_from_enemy_knights(self, npx, npy):
        if 0 <= npx - 2 < 8 and 0 <= npy - 1 < 8 and GlobalVariables.board.matrix[npx - 2][npy - 1] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx - 2][npy - 1])) and GlobalVariables.board.matrix[npx - 2][npy - 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx - 2 < 8 and 0 <= npy + 1 < 8 and GlobalVariables.board.matrix[npx - 2][npy + 1] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx - 2][npy + 1])) and GlobalVariables.board.matrix[npx - 2][npy + 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx - 1 < 8 and 0 <= npy + 2 < 8 and GlobalVariables.board.matrix[npx - 1][npy + 2] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx - 1][npy + 2])) and GlobalVariables.board.matrix[npx - 1][npy + 2].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 1 < 8 and 0 <= npy + 2 < 8 and GlobalVariables.board.matrix[npx + 1][npy + 2] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx + 1][npy + 2])) and GlobalVariables.board.matrix[npx + 1][npy + 2].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 2 < 8 and 0 <= npy + 1 < 8 and GlobalVariables.board.matrix[npx + 2][npy + 1] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx + 2][npy + 1])) and GlobalVariables.board.matrix[npx + 2][npy + 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 2 < 8 and 0 <= npy - 1 < 8 and GlobalVariables.board.matrix[npx + 2][npy - 1] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx + 2][npy - 1])) and GlobalVariables.board.matrix[npx + 2][npy - 1].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx + 1 < 8 and 0 <= npy - 2 < 8 and GlobalVariables.board.matrix[npx + 1][npy - 2] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx + 1][npy - 2])) and GlobalVariables.board.matrix[npx + 1][npy - 2].color != self.color:  # and its enemy knight
                return False

        if 0 <= npx - 1 < 8 and 0 <= npy - 2 < 8 and GlobalVariables.board.matrix[npx - 1][npy - 2] is not None:  # found piece on the board
            if 'Knight' in str(type(GlobalVariables.board.matrix[npx - 1][npy - 2])) and GlobalVariables.board.matrix[npx - 1][npy - 2].color != self.color:  # and its enemy knight
                return False

        return True

    def is_safe_from_enemy_pawn(self, npx, npy):
        direction = 1 if self.color == 'black' else -1

        if 0 <= npy - 1 < 8 and (0 <= npx + direction < 8):  # don't go out of the matrix
            if GlobalVariables.board.matrix[npx + direction][npy - 1] is not None:  # find a piece
                if 'Pawn' in str(type(GlobalVariables.board.matrix[npx + direction][npy - 1])) \
                        and GlobalVariables.board.matrix[npx + direction][npy - 1].color != self.color:  # if it's enemy pawn
                    return False

        if 0 <= npy + 1 < 8 and (0 <= npx + direction < 8):  # don't go out of the matrix
            if GlobalVariables.board.matrix[npx + direction][npy + 1] is not None:  # there is a piece on the right down/up from the new pos
                if 'Pawn' in str(type(GlobalVariables.board.matrix[npx + direction][npy + 1])) \
                        and GlobalVariables.board.matrix[npx + direction][npy + 1].color != self.color:  # if it's enemy pawn
                    return False

        return True

    def is_safe_from_enemy_king(self, npx, npy):
        if 0 <= npx - 1 < 8 and 0 <= npy - 1 < 8:           # out of board check
            if GlobalVariables.board.matrix[npx - 1][npy - 1] is not None:        # top left piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx - 1][npy - 1])) and GlobalVariables.board.matrix[npx - 1][npy - 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx < 8 and 0 <= npy - 1 < 8:               # out of board check
            if GlobalVariables.board.matrix[npx][npy - 1] is not None:            # left center piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx][npy - 1])) and GlobalVariables.board.matrix[npx][npy - 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx + 1 < 8 and 0 <= npy - 1 < 8:           # out of board check
            if GlobalVariables.board.matrix[npx + 1][npy - 1] is not None:        # bot left piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx + 1][npy - 1])) and GlobalVariables.board.matrix[npx + 1][npy - 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx - 1 < 8 and 0 <= npy < 8:               # out of board check
            if GlobalVariables.board.matrix[npx - 1][npy] is not None:            # top center piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx - 1][npy])) and GlobalVariables.board.matrix[npx - 1][npy].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx + 1 < 8 and 0 <= npy < 8:               # out of board check
            if GlobalVariables.board.matrix[npx + 1][npy] is not None:            # bot center piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx + 1][npy])) and GlobalVariables.board.matrix[npx + 1][npy].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx - 1 < 8 and 0 <= npy + 1 < 8:           # out of board check
            if GlobalVariables.board.matrix[npx - 1][npy + 1] is not None:        # top right piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx - 1][npy + 1])) and GlobalVariables.board.matrix[npx - 1][npy + 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx < 8 and 0 <= npy + 1 < 8:               # out of board check
            if GlobalVariables.board.matrix[npx][npy + 1] is not None:            # center right piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx][npy + 1])) and GlobalVariables.board.matrix[npx][npy + 1].color != self.color:  # and it's enemy king
                    return False

        if 0 <= npx + 1 < 8 and 0 <= npy + 1 < 8:           # out of board check
            if GlobalVariables.board.matrix[npx + 1][npy + 1] is not None:        # bot right piece found
                if 'King' in str(type(GlobalVariables.board.matrix[npx + 1][npy + 1])) and GlobalVariables.board.matrix[npx + 1][npy + 1].color != self.color:  # and it's enemy king
                    return False

        return True

    def is_going_into_free_square(self, prev_pos, new_pos):
        npx = new_pos[0]
        npy = new_pos[1]
        if not self.is_safe_from_enemy_king(npx, npy):
            return False

        if not self.is_safe_from_enemy_pawn(npx, npy):
            return False

        if not self.is_safe_from_enemy_knights(npx, npy):
            return False

        if not self.is_safe_from_enemy_bishop_or_Queen(prev_pos, npx, npy):
            return False

        if not self.is_safe_from_enemy_rook_or_Queen(prev_pos, npx, npy):
            return False

        return True

    def is_valid_move(self, prev_pos, new_pos):
        if not Piece.is_valid_move(self, prev_pos, new_pos):
            return False

        if not self.is_going_into_free_square(prev_pos, new_pos):
            return False

        ppx = prev_pos[0]
        ppy = prev_pos[1]
        npx = new_pos[0]
        npy = new_pos[1]
        if 0 < npx > 7 or 0 < npy > 7:  # are we out of the board
            return False  # we leave

        ally = False  # is the new square occupied by an ally
        if not GlobalVariables.board.matrix[npx][npy] is None:
            if GlobalVariables.board.matrix[npx][npy].color == GlobalVariables.board.matrix[ppx][ppy]:
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
                if not self.is_going_into_free_square(prev_pos, (ppx, ppy + 1), GlobalVariables.board.matrix) \
                        or not self.is_going_into_free_square(prev_pos, (ppx, ppy + 2), GlobalVariables.board.matrix):  # king's way is attacked
                    return False
                if GlobalVariables.board.matrix[ppx][ppy + 1] is None and GlobalVariables.board.matrix[ppx][ppy + 2] is None:  # square on the right of the king are empty
                    if self.color == 'white':  # white king castle
                        if isinstance(GlobalVariables.board.matrix[7][7], Rook):  # we have a piece on the right that is a rook
                            if not GlobalVariables.board.matrix[7][7].moved:  # if the rook hasn't moved
                                GlobalVariables.board.matrix[7][7].position = (7, 5)
                                GlobalVariables.board.matrix[7][5] = GlobalVariables.board.matrix[7][7]
                                GlobalVariables.board.matrix[7][7] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
                    else:
                        if isinstance(GlobalVariables.board.matrix[0][7], Rook):  # we have a piece on the right that is a rook
                            if not GlobalVariables.board.matrix[0][7].moved:  # if the rook hasn't moved
                                GlobalVariables.board.matrix[0][7].position = (0, 5)
                                GlobalVariables.board.matrix[0][5] = GlobalVariables.board.matrix[0][7]
                                GlobalVariables.board.matrix[0][7] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
            elif ppy - 2 == npy and ppx == npx:  # we try to castle queen side
                if not self.is_going_into_free_square(prev_pos, (ppx, ppy - 1)) \
                        or not self.is_going_into_free_square(prev_pos, (ppx, ppy - 2)):  # king's way is attacked
                    return False
                if GlobalVariables.board.matrix[ppx][ppy - 1] is None and GlobalVariables.board.matrix[ppx][ppy - 2] is None:  # square on the right of the king are empty
                    if self.color == 'white':  # white king castle
                        if isinstance(GlobalVariables.board.matrix[7][0], Rook):  # we have a piece on the right that is a rook
                            if not GlobalVariables.board.matrix[7][0].moved:  # if the rook hasn't moved
                                GlobalVariables.board.matrix[7][0].position = (7, 3)
                                GlobalVariables.board.matrix[7][3] = GlobalVariables.board.matrix[7][0]
                                GlobalVariables.board.matrix[7][0] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
                    else:
                        if isinstance(GlobalVariables.board.matrix[0][0], Rook):  # we have a piece on the right that is a rook
                            if not GlobalVariables.board.matrix[0][0].moved:  # if the rook hasn't moved
                                GlobalVariables.board.matrix[0][0].position = (0, 3)
                                GlobalVariables.board.matrix[0][3] = GlobalVariables.board.matrix[0][0]
                                GlobalVariables.board.matrix[0][0] = None  # we delete the rook from the bottom right square
                                if self.color == 'white':  # save kings pos
                                    GlobalVariables.w_king_position = new_pos
                                else:
                                    GlobalVariables.b_king_position = new_pos
                                return True
        return False
