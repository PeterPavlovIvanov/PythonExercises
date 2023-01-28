import pygame

import GlobalVariables
from GlobalVariables import *


class Piece:
    def __init__(self, color: object, position: object, image: object):
        self.color = color
        self.position = position
        self.image = pygame.image.load(image)
        self.moved = False
        self.dj = False  # did the pawn double jump, the last turn

    def new_position(self, pos):
        self.position = pos

    def is_safe_from_diagonal_discovered_attack(self, matrix):
        if self.color == 'white':  # check white king safety
            r = GlobalVariables.w_king_position[0]  # row counter
            c = GlobalVariables.w_king_position[1]  # col counter
            # down right check
            while True:
                r = r + 1
                c = c + 1
                if r > 7 or c > 7:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if 'Bishop' in piece_full_type or 'Queen' in piece_full_type:  # if we meet a queen or a bishop
                        if matrix[r][c].color == 'black':  # and is attack our king
                            return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

            r = GlobalVariables.w_king_position[0]  # reset row counter
            c = GlobalVariables.w_king_position[1]  # reset col counter
            # up left check
            while True:
                r = r - 1
                c = c - 1
                if r < 0 or c < 0:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if 'Bishop' in piece_full_type or 'Queen' in piece_full_type:  # if we meet a queen or a bishop
                        if matrix[r][c].color == 'black':  # and is attack our king
                            return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

            r = GlobalVariables.w_king_position[0]  # reset row counter
            c = GlobalVariables.w_king_position[1]  # reset col counter
            # up right check
            while True:
                r = r - 1
                c = c + 1
                if c > 7 or r < 0:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if 'Bishop' in piece_full_type or 'Queen' in piece_full_type:  # if we meet a queen or a bishop
                        if matrix[r][c].color == 'black':  # and is attack our king
                            return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

            r = GlobalVariables.w_king_position[0]  # reset row counter
            c = GlobalVariables.w_king_position[1]  # reset col counter
            # down left check
            while True:
                r = r + 1
                c = c - 1
                if c < 0 or r > 7:  # are we out of the board
                    break  # we leave
                if matrix[r][c] is not None:  # we found a piece
                    piece_full_type = str(type(matrix[r][c]))
                    if 'Bishop' in piece_full_type or 'Queen' in piece_full_type:  # if we meet a queen or a bishop
                        if matrix[r][c].color == 'black':  # and is attack our king
                            return False  # it's invalid move
                    else:  # if it is not Bishop or Queen
                        break  # there won't be danger for our king

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

        #if not self.is_safe_from_diagonal_discovered_attack(matrix):
        #    return False

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
