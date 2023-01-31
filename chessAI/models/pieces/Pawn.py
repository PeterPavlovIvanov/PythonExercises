import pygame

import GlobalVariables
from models.pieces.Bishop import Bishop
from models.pieces.Knight import Knight
from models.pieces.Piece import Piece
from models.pieces.Queen import Queen
from models.pieces.Rook import Rook


class Pawn(Piece):
    def __init__(self, color, new_pos, image):
        Piece.__init__(self, color, new_pos, image)
        self.value = 100

    def ask_promotion(self, npx, npy):
        if npx == 0 or npx == 7:
            promotion_chosen = False
            pos_x = 0 if self.color == 'white' else 7
            knight = Knight(self.color, (pos_x, npy), 'res/pieces/promotion/' + str(self.color) + '_knight.png')
            bishop = Knight(self.color, (pos_x, npy), 'res/pieces/promotion/' + str(self.color) + '_bishop.png')
            queen = Knight(self.color, (pos_x, npy), 'res/pieces/promotion/' + str(self.color) + '_queen.png')
            rook = Knight(self.color, (pos_x, npy), 'res/pieces/promotion/' + str(self.color) + '_rook.png')
            while not promotion_chosen:
                pygame.draw.rect(GlobalVariables.screen, (255, 204, 102), pygame.Rect(255, 292.5, 105, 30))
                GlobalVariables.screen.blit(knight.image, (255, 292.5))
                GlobalVariables.screen.blit(bishop.image, (280, 292.5))
                GlobalVariables.screen.blit(rook.image, (305, 292.5))
                GlobalVariables.screen.blit(queen.image, (330, 292.5))

                pygame.display.flip()
                events = pygame.event.get()
                for e in events:  # user input
                    if e.type == pygame.QUIT:
                        return
                    elif e.type == pygame.MOUSEBUTTONDOWN:
                        cur_pos = pygame.mouse.get_pos()
                        cur_x = cur_pos[0] - GlobalVariables.BOARD_ADJUSTMENT
                        cur_y = cur_pos[1] - GlobalVariables.BOARD_ADJUSTMENT
                        print(f'{cur_x};{cur_y}')
                        if 229 <= cur_x <= 335 and 268 <= cur_y <= 297:
                            if cur_x <= 255.5:
                                GlobalVariables.board.matrix[npx][npy] = Knight(self.color, (npx, npy), f'res/pieces/{self.color}_knight.png')
                            elif cur_x <= 282:
                                GlobalVariables.board.matrix[npx][npy] = Bishop(self.color, (npx, npy), f'res/pieces/{self.color}_bishop.png')
                            elif cur_x <= 308.5:
                                GlobalVariables.board.matrix[npx][npy] = Rook(self.color, (npx, npy), f'res/pieces/{self.color}_rook.png')
                            elif cur_x <= 335:
                                GlobalVariables.board.matrix[npx][npy] = Queen(self.color, (npx, npy), f'res/pieces/{self.color}_queen.png')
                            promotion_chosen = True
                            #229;
                            #268
                            #335;
                            #297

    def is_valid_move(self, prev_pos, new_pos):
        if not Piece.is_valid_move(self, prev_pos, new_pos):
            return False
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        npx = new_pos[0]
        npy = new_pos[1]

        if ppx == 1 and self.color == 'black' or ppx == 6 and self.color == 'white':  # if pawn hasn't moved
            if (ppx + 2 == npx and ppy == npy and self.color == 'black') \
                    or (ppx - 2 == npx and ppy == npy and self.color == 'white'):  # and tries to double move
                if GlobalVariables.board.matrix[npx][npy] is None:  # and there is no one there
                    return True  # we allow the double move

        if (ppx + 1 == npx and ppy == npy and self.color == 'black') \
                or (ppx - 1 == npx and ppy == npy and self.color == 'white'):  # tries to move forward
            if GlobalVariables.board.matrix[npx][npy] is None:  # and there is no one there
                self.ask_promotion(npx, npy)
                return True  # we allow one square move

        if (ppx + 1 == npx and (ppy - 1 == npy or ppy + 1 == npy) and self.color == 'black') \
                or (ppx - 1 == npx and (ppy - 1 == npy or ppy + 1 == npy) and self.color == 'white'):  # tries to capture diagonally
            if GlobalVariables.board.matrix[npx][npy] is not None:  # there is some piece there
                if GlobalVariables.board.matrix[npx][npy].color != self.color:  # is an enemy
                    self.ask_promotion(npx, npy)
                    return True  # we allow to capture
            elif (npx == 5 and self.color == 'black') or (npx == 2 and self.color == 'white'):  # if there is no piece there we try en passant white captures
                second_to_last = GlobalVariables.history[len(GlobalVariables.history) - 2]
                latest = GlobalVariables.history[len(GlobalVariables.history) - 1]
                if second_to_last is not None:  # there is history
                    if 'Pawn' in str(type(second_to_last)):  # last moved is a pawn
                        if second_to_last.color != self.color:  # it is black
                            if abs(second_to_last.position[0] - latest.position[0]) == 2:  # it double jumped
                                if latest.position[1] == npy:  # it is on the same column
                                    GlobalVariables.board.matrix[latest.position[0]][latest.position[1]] = None  # capture pawn
                                    return True

        return False
