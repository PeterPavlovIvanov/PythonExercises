import pygame

from GlobalVariables import *
from models.Board import Board
from models.pieces.Bishop import Bishop
from models.pieces.King import King
from models.pieces.Knight import Knight
from models.pieces.Pawn import Pawn
from models.pieces.Queen import Queen
from models.pieces.Rook import Rook

white = (255, 255, 255)

def create_board_surface():
    board_surface = pygame.Surface((SQUARE_SIZE * ROWS, SQUARE_SIZE * COLS))
    dark = False
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(r * SQUARE_SIZE, c * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(board_surface, pygame.Color(BLACK_SQUARE_COLOR if dark else WHITE_SQUARE_COLOR), rect)
            dark = not dark
        dark = not dark
    return board_surface


def drag_piece(screen, selected_piece, drag_pos):
    if selected_piece is not None:
        screen.blit(selected_piece.image, (drag_pos[0], drag_pos[1]))


def main():
    screen = pygame.display.set_mode((610, 610))
    board = Board()
    board_surface = create_board_surface()
    clock = pygame.time.Clock()
    selected_piece = None
    square_y = -1
    square_x = -1
    prev_square_x = -1
    prev_square_y = -1
    turn = True
    prev_piece = None
    while True:
        cur_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        cur_x = cur_pos[0] - BOARD_ADJUSTMENT
        cur_y = cur_pos[1] - BOARD_ADJUSTMENT
        for e in events:  # user input
            if e.type == pygame.QUIT:
                return
            elif e.type == pygame.MOUSEBUTTONDOWN:  # left click --> grab a piece in hand
                square_y = int(cur_x / SQUARE_SIZE)
                square_x = int(cur_y / SQUARE_SIZE)
                selected_piece = board.matrix[square_x][square_y]  # duplicates the piece from the board in the hand
                if turn:
                    if selected_piece is not None:
                        if selected_piece.color == 'white':
                            prev_piece = board.matrix[square_x][square_y]  # saves the previous/current state of the piece
                            board.matrix[square_x][square_y] = None  # removes it that so it is only in our hand
                        else:
                            selected_piece = None
                else:
                    if selected_piece is not None:
                        if selected_piece.color == 'black':
                            prev_piece = board.matrix[square_x][square_y]  # saves the previous/current state of the piece
                            board.matrix[square_x][square_y] = None  # removes it that so it is only in our hand
                        else:
                            selected_piece = None
            elif e.type == pygame.MOUSEBUTTONUP:  # release left click --> drop piece back on the board
                if selected_piece is None:
                    continue
                prev_square_x = square_x  # previous position
                prev_square_y = square_y  # previous position
                square_y = int(cur_x / SQUARE_SIZE)  # take new square position for the piece
                square_x = int(cur_y / SQUARE_SIZE)  # take new square position for the piece
                if selected_piece.is_valid_move((prev_square_x, prev_square_y), (square_x, square_y), board.matrix):
                    board.matrix[prev_square_x][prev_square_y] = None
                    selected_piece.new_position((square_x, square_y))  # prepare new piece position
                    board.matrix[square_x][square_y] = selected_piece  # set new piece in the matrix
                    turn = not turn
                else:  # if the move is illegal
                    board.matrix[prev_square_x][prev_square_y] = prev_piece
                    square_x = prev_square_x  # retrieve previous position
                    square_y = prev_square_y  # retrieve previous position

                selected_piece = None  # Remove piece from hand

        screen.fill(BACKGROUND_COLOR)
        draw_letters_on_side(screen)
        screen.blit(board_surface, (BOARD_ADJUSTMENT, BOARD_ADJUSTMENT))
        board.draw_board(screen)

        # always enter dragging but only when selected_piece is not None we act inside
        # selected_piece will become not None when left button is pressed, when released it is again set to None
        drag_piece(screen, selected_piece, (cur_x, cur_y))

        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()


pygame.font.init()


def draw_letters_on_side(screen):
    font = pygame.font.Font(None, 22)
    r = 8
    while r > 0:
        text = font.render(str(9 - r), True, white)
        screen.blit(text, (8, r * SQUARE_SIZE - 15))
        screen.blit(text, (594, r * SQUARE_SIZE - 15))
        text = font.render(chr(r + 96), True, white)
        screen.blit(text, (r * SQUARE_SIZE - 13, 590))
        screen.blit(text, (r * SQUARE_SIZE - 13, 6))
        r = r - 1


if __name__ == '__main__':
    main()
