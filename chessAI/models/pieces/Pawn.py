import GlobalVariables
from models.pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, prev_pos, new_pos, matrix):
        Piece.__init__(self, prev_pos, new_pos, matrix)
        self.value = 100

    def is_valid_move(self, prev_pos, new_pos, matrix):
        if not Piece.is_valid_move(self, prev_pos, new_pos, matrix):
            return False
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        npx = new_pos[0]
        npy = new_pos[1]

        if ppx == 1 and self.color == 'black' or ppx == 6 and self.color == 'white':  # if pawn hasn't moved
            if (ppx + 2 == npx and ppy == npy and self.color == 'black') \
                    or (ppx - 2 == npx and ppy == npy and self.color == 'white'):  # and tries to double move
                if matrix[npx][npy] is None:  # and there is no one there
                    return True  # we allow the double move

        if (ppx + 1 == npx and ppy == npy and self.color == 'black') \
                or (ppx - 1 == npx and ppy == npy and self.color == 'white'):  # tries to move forward
            if matrix[npx][npy] is None:  # and there is no one there
                return True  # we allow one square move

        if (ppx + 1 == npx and (ppy - 1 == npy or ppy + 1 == npy) and self.color == 'black') \
                or (ppx - 1 == npx and (ppy - 1 == npy or ppy + 1 == npy) and self.color == 'white'):  # tries to capture diagonally
            if matrix[npx][npy] is not None:  # there is some piece there
                if matrix[npx][npy].color != self.color:  # is an enemy
                    return True  # we allow to capture
            elif npx == 2 or npx == 5:  # if there is no piece there we try en passant white captures
                second_to_last = GlobalVariables.history[len(GlobalVariables.history) - 2]
                latest = GlobalVariables.history[len(GlobalVariables.history) - 1]
                if second_to_last is not None:  # there is history
                    if 'Pawn' in str(type(second_to_last)):  # last moved is a pawn
                        if second_to_last.color != self.color:  # it is black
                            if abs(second_to_last.position[0] - latest.position[0]) == 2:  # it double jumped
                                if latest.position[1] == npy:  # it is on the same column
                                    matrix[latest.position[0]][latest.position[1]] = None  # capture pawn
                                    return True

        return False
