from models.pieces.Bishop import Bishop
from models.pieces.King import King
from models.pieces.Knight import Knight
from models.pieces.Pawn import Pawn
from models.pieces.Queen import Queen
from models.pieces.Rook import Rook
from GlobalVariables import *


class Board:
    def __init__(self):
        r1 = Rook('black', (0, 0), 'res/pieces/black_rook.png')
        n1 = Knight('black', (0, 1), 'res/pieces/black_knight.png')
        b1 = Bishop('black', (0, 2), 'res/pieces/black_bishop.png')
        q = Queen('black', (0, 3), 'res/pieces/black_queen.png')
        k = King('black', (0, 4), 'res/pieces/black_king.png')
        b2 = Bishop('black', (0, 5), 'res/pieces/black_bishop.png')
        n2 = Knight('black', (0, 6), 'res/pieces/black_knight.png')
        r2 = Rook('black', (0, 7), 'res/pieces/black_rook.png')
        p1 = Pawn('black', (1, 0), 'res/pieces/black_pawn.png')
        p2 = Pawn('black', (1, 1), 'res/pieces/black_pawn.png')
        p3 = Pawn('black', (1, 2), 'res/pieces/black_pawn.png')
        p4 = Pawn('black', (1, 3), 'res/pieces/black_pawn.png')
        p5 = Pawn('black', (1, 4), 'res/pieces/black_pawn.png')
        p6 = Pawn('black', (1, 5), 'res/pieces/black_pawn.png')
        p7 = Pawn('black', (1, 6), 'res/pieces/black_pawn.png')
        p8 = Pawn('black', (1, 7), 'res/pieces/black_pawn.png')
        R1 = Rook('white', (7, 0), 'res/pieces/white_rook.png')
        N1 = Knight('white', (7, 1), 'res/pieces/white_knight.png')
        B1 = Bishop('white', (7, 2), 'res/pieces/white_bishop.png')
        Q = Queen('white', (7, 3), 'res/pieces/white_queen.png')
        K = King('white', (7, 4), 'res/pieces/white_king.png')
        B2 = Bishop('white', (7, 5), 'res/pieces/white_bishop.png')
        N2 = Knight('white', (7, 6), 'res/pieces/white_knight.png')
        R2 = Rook('white', (7, 7), 'res/pieces/white_rook.png')
        P1 = Pawn('white', (6, 0), 'res/pieces/white_pawn.png')
        P2 = Pawn('white', (6, 1), 'res/pieces/white_pawn.png')
        P3 = Pawn('white', (6, 2), 'res/pieces/white_pawn.png')
        P4 = Pawn('white', (6, 3), 'res/pieces/white_pawn.png')
        P5 = Pawn('white', (6, 4), 'res/pieces/white_pawn.png')
        P6 = Pawn('white', (6, 5), 'res/pieces/white_pawn.png')
        P7 = Pawn('white', (6, 6), 'res/pieces/white_pawn.png')
        P8 = Pawn('white', (6, 7), 'res/pieces/white_pawn.png')

        self.matrix = \
            [[r1, n1, b1, q, k, b2, n2, r2]
                , [p1, p2, p3, p4, p5, p6, p7, p8]
                , [None, None, None, None, None, None, None, None]
                , [None, None, None, None, None, None, None, None]
                , [None, None, None, None, None, None, None, None]
                , [None, None, None, None, None, None, None, None]
                , [P1, P2, P3, P4, P5, P6, P7, P8]
                , [R1, N1, B1, Q, K, B2, N2, R2]]

    def draw_board(self, screen):
        for r in range(0, ROWS):
            for c in range(0, COLS):
                piece = self.matrix[r][c]
                if not piece is None:
                    screen.blit(piece.image, (PIECE_ADJUSTMENT + piece.position[1] * SQUARE_SIZE
                                              , PIECE_ADJUSTMENT + piece.position[0] * SQUARE_SIZE))
    pass
