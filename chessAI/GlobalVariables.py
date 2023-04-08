from random import *
SQUARE_SIZE = 70
ROWS = COLS = 8
BOARD_ADJUSTMENT = 25
PIECE_ADJUSTMENT = 30
BLACK_SQUARE_COLOR = (212, 148, 0)
WHITE_SQUARE_COLOR = (252, 240, 204)
BACKGROUND_COLOR = (128, 89, 0)
EVALUATION_BAR_WIDTH = 15

w_team_value = 0
b_team_value = 0

w_king_position = (7, 4)
b_king_position = (0, 4)
history = []  # each element of the history contains 2 Pieces, the old and the new state of the piece
turn = True  # True - white's turn; False - black's turn
screen = None
board = None
random = Random()
