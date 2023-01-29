import copy

import pygame

import GlobalVariables
from GlobalVariables import *


class Piece:
    def __init__(self, color: object, position: object, image: object):
        self.color = color
        self.position = position
        self.image = pygame.image.load(image)
        self.moved = False

    def new_position(self, pos):
        self.position = pos

    def is_safe_from_direct_discovered_attack_color(self, matrix, color1, color2):
        # save the beginning of the counters
        start_r_counter = GlobalVariables.w_king_position[0] if color1 == 'white' \
            else GlobalVariables.b_king_position[0]
        start_c_counter = GlobalVariables.w_king_position[1] if color1 == 'white' \
            else GlobalVariables.b_king_position[1]

        # up check
        r = copy.copy(start_r_counter)  # reinit counter
        c = copy.copy(start_c_counter)  # reinit counter
        while True:
            r = r - 1
            if r > 7 or r < 0 or c > 7 or c < 0:  # out of board check
                break
            piece_found = matrix[r][c]
            if piece_found is not None:  # on first found piece
                if ('Rook' in str(type(piece_found)) or 'Queen' in str(type(piece_found)))\
                        and piece_found.color == color2:  # enemy rook or queen found as first piece
                    return False  # illegal move
                else:
                    break

        # down check
        r = copy.copy(start_r_counter)  # reinit counter
        c = copy.copy(start_c_counter)  # reinit counter
        while True:
            r = r + 1
            if r > 7 or r < 0 or c > 7 or c < 0:  # out of board check
                break
            piece_found = matrix[r][c]
            if piece_found is not None:  # on first found piece
                if ('Rook' in str(type(piece_found)) or 'Queen' in str(type(piece_found)))\
                        and piece_found.color == color2:  # enemy rook or queen found as first piece
                    return False  # illegal move
                else:
                    break

        # left check
        r = copy.copy(start_r_counter)  # reinit counter
        c = copy.copy(start_c_counter)  # reinit counter
        while True:
            c = c - 1
            if r > 7 or r < 0 or c > 7 or c < 0:  # out of board check
                break
            piece_found = matrix[r][c]
            if piece_found is not None:  # on first found piece
                if ('Rook' in str(type(piece_found)) or 'Queen' in str(type(piece_found)))\
                        and piece_found.color == color2:  # enemy rook or queen found as first piece
                    return False  # illegal move
                else:
                    break

        # right check
        r = copy.copy(start_r_counter)  # reinit counter
        c = copy.copy(start_c_counter)  # reinit counter
        while True:
            c = c + 1
            if r > 7 or r < 0 or c > 7 or c < 0:  # out of board check
                break
            piece_found = matrix[r][c]
            if piece_found is not None:  # on first found piece
                if ('Rook' in str(type(piece_found)) or 'Queen' in str(type(piece_found)))\
                        and piece_found.color == color2:  # enemy rook or queen found as first piece
                    return False  # illegal move
                else:
                    break

        return True

    def is_safe_from_pawns_color(self, matrix, color1, color2):
        king_pos = GlobalVariables.w_king_position if color1 == 'white' else GlobalVariables.b_king_position
        kpx = king_pos[0]
        kpy = king_pos[1]
        direction = -1 if color1 == 'white' else 1

        # pawn ot the left
        if -1 < kpx + direction < 8 and -1 < kpy - 1 < 8:  # in the board
            if matrix[kpx + direction][kpy - 1] is not None:  # there is a piece
                if 'Pawn' in str(type(matrix[kpx + direction][kpy - 1])) and matrix[kpx + direction][kpy - 1].color == color2:  # enemy pawn found
                    return False

        # pawn on the right
        if -1 < kpx + direction < 8 and -1 < kpy + 1 < 8:  # in the board
            if matrix[kpx + direction][kpy + 1] is not None:  # there is a piece
                if 'Pawn' in str(type(matrix[kpx + direction][kpy + 1])) and matrix[kpx + direction][kpy + 1].color == color2:  # enemy pawn found
                    return False

        return True

    def is_safe_from_pawns(self, matrix):
        if GlobalVariables.turn:  # if it's white's turn
            if not self.is_safe_from_pawns_color(matrix, 'white', 'black'):  # we check white's king safety
                return False
        else:
            if not self.is_safe_from_pawns_color(matrix, 'black', 'white'):  # on black's turn we check black kings safety
                return False

        return True

    def is_safe_from_knights_color(self, matrix, color1, color2):
        king_pos = GlobalVariables.w_king_position if color1 == 'white' else GlobalVariables.b_king_position
        kpx = king_pos[0]
        kpy = king_pos[1]
        # top right
        if -1 < kpx - 2 < 8 and -1 < kpy + 1 < 8:  # in the board
            if matrix[kpx - 2][kpy + 1] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx - 2][kpy + 1])) and matrix[kpx - 2][kpy + 1].color == color2:  # enemy knight found
                    return False

        if -1 < kpx - 1 < 8 and -1 < kpy + 2 < 8:  # in the board
            if matrix[kpx - 1][kpy + 2] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx - 1][kpy + 2])) and matrix[kpx - 1][kpy + 2].color == color2:  # enemy knight found
                    return False

        # bot right
        if -1 < kpx + 1 < 8 and -1 < kpy + 2 < 8:  # in the board
            if matrix[kpx + 1][kpy + 2] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx + 1][kpy + 2])) and matrix[kpx + 1][kpy + 2].color == color2:  # enemy knight found
                    return False

        if -1 < kpx + 2 < 8 and -1 < kpy + 1 < 8:  # in the board
            if matrix[kpx + 2][kpy + 1] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx + 2][kpy + 1])) and matrix[kpx + 2][kpy + 1].color == color2:  # enemy knight found
                    return False

        # bot left
        if -1 < kpx + 2 < 8 and -1 < kpy - 1 < 8:  # in the board
            if matrix[kpx + 2][kpy - 1] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx + 2][kpy - 1])) and matrix[kpx + 2][kpy - 1].color == color2:  # enemy knight found
                    return False

        if -1 < kpx + 1 < 8 and -1 < kpy - 2 < 8:  # in the board
            if matrix[kpx + 1][kpy - 2] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx + 1][kpy - 2])) and matrix[kpx + 1][kpy - 2].color == color2:  # enemy knight found
                    return False

        # top left
        if -1 < kpx - 1 < 8 and -1 < kpy + 2 < 8:  # in the board
            if matrix[kpx - 1][kpy + 2] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx - 1][kpy + 2])) and matrix[kpx - 1][kpy + 2].color == color2:  # enemy knight found
                    return False

        if -1 < kpx - 2 < 8 and -1 < kpy + 1 < 8:  # in the board
            if matrix[kpx - 2][kpy + 1] is not None:  # we have a piece there
                if 'Knight' in str(type(matrix[kpx - 2][kpy + 1])) and matrix[kpx - 2][kpy + 1].color == color2:  # enemy knight found
                    return False

        return True


    def is_safe_from_knights(self, matrix):
        if GlobalVariables.turn:  # if it's white's turn
            if not self.is_safe_from_knights_color(matrix, 'white', 'black'):  # we check white's king safety
                return False
        else:
            if not self.is_safe_from_knights_color(matrix, 'black', 'white'):  # on black's turn we check black kings safety
                return False

        return True

    def is_safe_from_direct_discovered_attack(self, matrix):
        if GlobalVariables.turn:  # if it's white's turn
            if not self.is_safe_from_direct_discovered_attack_color(matrix, 'white', 'black'):  # we check white's king safety
                return False
        elif not self.is_safe_from_direct_discovered_attack_color(matrix, 'black', 'white'):  # on black's turn we check black kings safety
            return False

        return True

    def is_safe_from_diagonal_discovered_attack_color(self, matrix, color1):
        if self.color == color1:  # check white king safety
            # save the beginning of the counters
            start_r_counter = GlobalVariables.w_king_position[0] if color1 == 'white' \
                else GlobalVariables.b_king_position[0]
            start_c_counter = GlobalVariables.w_king_position[1] if color1 == 'white' \
                else GlobalVariables.b_king_position[1]

            r = copy.copy(start_r_counter)  # row counter
            c = copy.copy(start_c_counter)  # col counter
            # down right check
            while True:
                r = r + 1
                c = c + 1
                if r > 7 or c > 7:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if ('Bishop' in piece_full_type or 'Queen' in piece_full_type) \
                            and matrix[r][c].color != color1:  # and is attack our king a.k.a its different color
                        return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

            r = copy.copy(start_r_counter)  # row counter
            c = copy.copy(start_c_counter)  # col counter
            # up left check
            while True:
                r = r - 1
                c = c - 1
                if r < 0 or c < 0:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if ('Bishop' in piece_full_type or 'Queen' in piece_full_type) \
                            and matrix[r][c].color != color1:  # and is attack our king a.k.a its different color
                        return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

            r = copy.copy(start_r_counter)  # row counter
            c = copy.copy(start_c_counter)  # col counter
            # up right check
            while True:
                r = r - 1
                c = c + 1
                if c > 7 or r < 0:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if ('Bishop' in piece_full_type or 'Queen' in piece_full_type) \
                            and matrix[r][c].color != color1:  # and is attack our king a.k.a its different color
                        return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

            r = copy.copy(start_r_counter)  # row counter
            c = copy.copy(start_c_counter)  # col counter
            # down left check
            while True:
                r = r + 1
                c = c - 1
                if c < 0 or r > 7:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if ('Bishop' in piece_full_type or 'Queen' in piece_full_type) \
                            and matrix[r][c].color != color1:  # and is attack our king a.k.a its different color
                        return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

        return True

    def is_safe_from_diagonal_discovered_attack(self, matrix):
        if GlobalVariables.turn:  # if it's white's turn
            if not self.is_safe_from_diagonal_discovered_attack_color(matrix, 'white'):  # we check white's king safety
                return False
        elif not self.is_safe_from_diagonal_discovered_attack_color(matrix, 'black'):  # on black's turn we check black kings safety
            return False

        return True

    def is_valid_move(self, prev_pos, new_pos, matrix):
        if prev_pos[0] > 7 or prev_pos[0] < 0 or prev_pos[1] > 7 \
                or prev_pos[1] < 0 or new_pos[0] > 7 or new_pos[0] < 0 or new_pos[1] > 7 or new_pos[1] < 0:
            return False  # return false when trying to leave the board

        if prev_pos == new_pos:  # if we move the piece at the same spot it is not considered a move
            return False

        if matrix[new_pos[0]][new_pos[1]] is not None:  # if we are trying to capture a piece
            if matrix[new_pos[0]][new_pos[1]].color == self.color:  # it cannot be ours
                return False

        # Temporary set the self on the new_pos
        temp_piece = copy.copy(self)
        temp_piece.position = new_pos
        matrix[prev_pos[0]][prev_pos[1]] = None
        temp_prev_piece_on_new_position = copy.copy(matrix[new_pos[0]][new_pos[1]])
        matrix[new_pos[0]][new_pos[1]] = temp_piece
        # and update the global position if we move a king
        if 'King' in str(type(self)):
            if self.color == 'white':
                GlobalVariables.w_king_position = new_pos
            else:
                GlobalVariables.b_king_position = new_pos

        if 'King' not in str(type(self)):  # if we are not moving the King
            if not self.is_safe_from_diagonal_discovered_attack(matrix):  # check for pins
                matrix[prev_pos[0]][prev_pos[1]] = copy.copy(temp_piece)  # rollback piece in hand
                matrix[new_pos[0]][new_pos[1]] = temp_prev_piece_on_new_position  # rollback piece or None on the new square
                if 'King' in str(type(self)):  # rollback global kings positions if king is grabbed
                    if self.color == 'white':
                        GlobalVariables.w_king_position = prev_pos
                    else:
                        GlobalVariables.b_king_position = prev_pos
                return False

        if 'King' not in str(type(self)):  # if we are not moving the King
            if not self.is_safe_from_direct_discovered_attack(matrix):  # check for pins
                matrix[prev_pos[0]][prev_pos[1]] = copy.copy(temp_piece)  # rollback piece in hand
                matrix[new_pos[0]][new_pos[1]] = temp_prev_piece_on_new_position  # rollback piece or None on the new square
                if 'King' in str(type(self)):  # rollback global kings positions if king is grabbed
                    if self.color == 'white':
                        GlobalVariables.w_king_position = prev_pos
                    else:
                        GlobalVariables.b_king_position = prev_pos
                return False

        if 'King' not in str(type(self)):  # if we are not moving the King
            if not self.is_safe_from_knights(matrix):  # check for attacks from knights
                matrix[prev_pos[0]][prev_pos[1]] = copy.copy(temp_piece)  # rollback piece in hand
                matrix[new_pos[0]][new_pos[1]] = temp_prev_piece_on_new_position  # rollback piece or None on the new square
                if 'King' in str(type(self)):  # rollback global kings positions if king is grabbed
                    if self.color == 'white':
                        GlobalVariables.w_king_position = prev_pos
                    else:
                        GlobalVariables.b_king_position = prev_pos
                return False

        if 'King' not in str(type(self)):  # if we are not moving the King
            if not self.is_safe_from_pawns(matrix):  # check for attacks from pawns
                matrix[prev_pos[0]][prev_pos[1]] = copy.copy(temp_piece)  # rollback piece in hand
                matrix[new_pos[0]][new_pos[1]] = temp_prev_piece_on_new_position  # rollback piece or None on the new square
                if 'King' in str(type(self)):  # rollback global kings positions if king is grabbed
                    if self.color == 'white':
                        GlobalVariables.w_king_position = prev_pos
                    else:
                        GlobalVariables.b_king_position = prev_pos
                return False

        matrix[prev_pos[0]][prev_pos[1]] = copy.copy(temp_piece)  # rollback piece in hand
        matrix[new_pos[0]][new_pos[1]] = temp_prev_piece_on_new_position  # rollback piece or None on the new square
        if 'King' in str(type(self)):  # rollback global kings positions if king is grabbed
            if self.color == 'white':
                GlobalVariables.w_king_position = prev_pos
            else:
                GlobalVariables.b_king_position = prev_pos
        return True

    def is_valid_diagonal_move(self, prev_pos, new_pos, matrix):
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        valid_moves = []
        r = ppx  # row counter
        c = ppy  # col counter

        # down right check
        while True:
            r = r + 1
            c = c + 1
            if r > 7 or c > 7:  # are we out of the board
                break  # we leave
            if matrix[r][c] is None:  # if the current square is empty
                valid_moves.append((r, c))  # it is a valid move
            else:  # if there is a piece ot that square
                if not matrix[r][c].color == self.color:  # if capturable
                    valid_moves.append((r, c))  # it is a valid move
                break  # and in either way we break

        r = ppx  # reset row counter
        c = ppy  # reset col counter
        # up left check
        while True:
            r = r - 1
            c = c - 1
            if r < 0 or c < 0:  # are we out of the board
                break  # we leave
            if matrix[r][c] is None:  # if the current square is empty
                valid_moves.append((r, c))  # it is a valid move
            else:  # if there is a piece ot that square
                if not matrix[r][c].color == self.color:  # if capturable
                    valid_moves.append((r, c))  # it is a valid move
                break  # and in either way we break

        r = ppx  # reset row counter
        c = ppy  # reset col counter
        # up right check
        while True:
            r = r - 1
            c = c + 1
            if c > 7 or r < 0:  # are we out of the board
                break  # we leave
            if matrix[r][c] is None:  # if the current square is empty
                valid_moves.append((r, c))  # it is a valid move
            else:  # if there is a piece ot that square
                if not matrix[r][c].color == self.color:  # if capturable
                    valid_moves.append((r, c))  # it is a valid move
                break  # and in either way we break

        r = ppx  # reset row counter
        c = ppy  # reset col counter
        # down left check
        while True:
            r = r + 1
            c = c - 1
            if c < 0 or r > 7:  # are we out of the board
                break  # we leave
            if matrix[r][c] is None:  # if the current square is empty
                valid_moves.append((r, c))  # it is a valid move
            else:  # if there is a piece ot that square
                if not matrix[r][c].color == self.color:  # if capturable
                    valid_moves.append((r, c))  # it is a valid move
                break  # and in either way we break

        return new_pos in valid_moves

    def is_valid_direct_move(self, prev_pos, new_pos, matrix):
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        valid_moves = []

        # right direct check
        for c in range(ppy + 1, COLS):  # we skip the column that the piece is in
            if matrix[ppx][c] is None:  # if empty square
                valid_moves.append((ppx, c))  # append as valid option
            else:
                if not matrix[ppx][c].color == self.color:  # if piece is available
                    valid_moves.append((ppx, c))  # add if its capturable
                break  # and in either way break

        # left direct check
        for c in reversed(range(ppy)):  # we skip the column that the piece is in
            if matrix[ppx][c] is None:  # if empty square
                valid_moves.append((ppx, c))  # append as valid option
            else:
                if not matrix[ppx][c].color == self.color:  # if piece is available
                    valid_moves.append((ppx, c))  # add if its capturable
                break  # and in either way break

        # up direct check
        for r in reversed(range(ppx)):  # we skip the column that the piece is in
            if matrix[r][ppy] is None:  # if empty square
                valid_moves.append((r, ppy))  # append as valid option
            else:
                if not matrix[r][ppy].color == self.color:  # if piece is available
                    valid_moves.append((r, ppy))  # add if its capturable
                break  # and in either way break

        # down direct check
        for r in range(ppx + 1, ROWS):  # we skip the column that the piece is in
            if matrix[r][ppy] is None:  # if empty square
                valid_moves.append((r, ppy))  # append as valid option
            else:
                if not matrix[r][ppy].color == self.color:  # if piece is available
                    valid_moves.append((r, ppy))  # add if its capturable
                break  # and in either way break

        result = new_pos in valid_moves
        if result and not self.moved:
            self.moved = True

        return result
