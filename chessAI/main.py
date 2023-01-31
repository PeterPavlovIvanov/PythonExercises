import copy

import pygame

import GlobalVariables
from GlobalVariables import *
from models.Board import Board
from models.pieces.Bishop import Bishop
from models.pieces.King import King
from models.pieces.Knight import Knight
from models.pieces.Pawn import Pawn
from models.pieces.Piece import Piece
from models.pieces.Queen import Queen
from models.pieces.Rook import Rook

white = (255, 255, 255)
black = (0, 0, 0)
selected_square = pygame.image.load('res/possible_movement_7.png')


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


def drag_piece(selected_piece, drag_pos):
    if selected_piece is not None:
        GlobalVariables.screen.blit(selected_piece.image, (drag_pos[0], drag_pos[1]))


def main():
    GlobalVariables.screen = pygame.display.set_mode((630, 610))
    GlobalVariables.board = Board()
    board_surface = create_board_surface()
    count_evaluation()  # count initial evaluation
    draw_evaluation()  # draw evaluation
    clock = pygame.time.Clock()
    selected_piece = None
    square_y = -1
    square_x = -1
    prev_square_x = -1
    prev_square_y = -1
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
                selected_piece = GlobalVariables.board.matrix[square_x][square_y]  # duplicates the piece from the board in the hand
                if GlobalVariables.turn:
                    if selected_piece is not None:
                        if selected_piece.color == 'white':
                            prev_piece = GlobalVariables.board.matrix[square_x][square_y]  # saves the previous/current state of the piece
                            GlobalVariables.board.matrix[square_x][square_y] = None  # removes it that so it is only in our hand
                        else:
                            selected_piece = None
                else:
                    if selected_piece is not None:
                        if selected_piece.color == 'black':
                            prev_piece = GlobalVariables.board.matrix[square_x][square_y]  # saves the previous/current state of the piece
                            GlobalVariables.board.matrix[square_x][square_y] = None  # removes it that so it is only in our hand
                        else:
                            selected_piece = None
            elif e.type == pygame.MOUSEBUTTONUP:  # release left click --> drop piece back on the board
                if selected_piece is None:
                    continue
                prev_square_x = square_x  # previous position
                prev_square_y = square_y  # previous position
                square_y = int(cur_x / SQUARE_SIZE)  # take new square position for the piece
                square_x = int(cur_y / SQUARE_SIZE)  # take new square position for the piece

                if selected_piece.is_valid_move((prev_square_x, prev_square_y), (square_x, square_y)):
                    GlobalVariables.board.matrix[prev_square_x][prev_square_y] = None  # delete old state of piece from board
                    GlobalVariables.history.append(copy.copy(selected_piece))  # save the prev pos of the piece
                    selected_piece.new_position((square_x, square_y))  # prepare new piece position

                    if GlobalVariables.board.matrix[square_x][square_y] is not None:
                        if GlobalVariables.board.matrix[square_x][square_y].color != selected_piece.color:
                            GlobalVariables.board.matrix[square_x][square_y] = selected_piece  # set new piece in the matrix
                    else:
                        GlobalVariables.board.matrix[square_x][square_y] = selected_piece  # set new piece in the matrix

                    GlobalVariables.history.append(selected_piece)  # add the new state of the piece
                    count_evaluation()  # count evaluation
                    GlobalVariables.turn = not GlobalVariables.turn  # change turns
                else:  # if the move is illegal
                    GlobalVariables.board.matrix[prev_square_x][prev_square_y] = prev_piece
                    square_x = prev_square_x  # retrieve previous position
                    square_y = prev_square_y  # retrieve previous position

                selected_piece = None  # Remove piece from hand

        GlobalVariables.screen.fill(BACKGROUND_COLOR)
        draw_letters_on_side()
        GlobalVariables.screen.blit(board_surface, (BOARD_ADJUSTMENT, BOARD_ADJUSTMENT))
        GlobalVariables.board.draw_board()

        # select just moved squares
        draw_selected_squares()
        draw_evaluation()  # draw eva-luation

        # always enter dragging but only when selected_piece is not None we act inside
        # selected_piece will become not None when left button is pressed, when released it is again set to None
        drag_piece(selected_piece, (cur_x, cur_y))

        # display update
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()


pygame.font.init()


def draw_selected_squares():
    if len(GlobalVariables.history) > 1:  # if there is a move made
        new_square_to_select = GlobalVariables.history[len(GlobalVariables.history) - 1]  # latest pos of moved piece
        old_square_to_select = GlobalVariables.history[len(GlobalVariables.history) - 2]  # old pos of moved piece
        GlobalVariables.screen.blit(selected_square, (old_square_to_select.position[1] * SQUARE_SIZE + BOARD_ADJUSTMENT
                                      , old_square_to_select.position[0] * SQUARE_SIZE + BOARD_ADJUSTMENT))
        GlobalVariables.screen.blit(selected_square, (new_square_to_select.position[1] * SQUARE_SIZE + BOARD_ADJUSTMENT
                                      , new_square_to_select.position[0] * SQUARE_SIZE + BOARD_ADJUSTMENT))


def draw_letters_on_side():
    font = pygame.font.Font(None, 22)
    r = 8
    while r > 0:
        text = font.render(str(9 - r), True, white)
        GlobalVariables.screen.blit(text, (8, r * SQUARE_SIZE - 15))
        GlobalVariables.screen.blit(text, (594, r * SQUARE_SIZE - 15))
        text = font.render(chr(r + 96), True, white)
        GlobalVariables.screen.blit(text, (r * SQUARE_SIZE - 13, 590))
        GlobalVariables.screen.blit(text, (r * SQUARE_SIZE - 13, 6))
        r = r - 1


def count_evaluation():
    GlobalVariables.w_team_value = 0
    GlobalVariables.b_team_value = 0
    for r in range(0, 8):
        for c in range(0, 8):
            if GlobalVariables.board.matrix[r][c] is not None:  # we find a piece
                if GlobalVariables.board.matrix[r][c].color == 'white':
                    GlobalVariables.w_team_value = GlobalVariables.w_team_value + GlobalVariables.board.matrix[r][c].value
                else:
                    GlobalVariables.b_team_value = GlobalVariables.b_team_value + GlobalVariables.board.matrix[r][c].value


def draw_evaluation():
    all_value = GlobalVariables.w_team_value + GlobalVariables.b_team_value
    value_piece = 610 / all_value
    pygame.draw.rect(GlobalVariables.screen, black, pygame.Rect(610, 0, 20, value_piece * GlobalVariables.b_team_value))
    pygame.draw.rect(GlobalVariables.screen, white, pygame.Rect(610, value_piece * GlobalVariables.b_team_value, 20, value_piece * GlobalVariables.w_team_value))


if __name__ == '__main__':
    main()
