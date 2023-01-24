from models.pieces.Piece import Piece


class Knight(Piece):
    def is_valid_move(self, prev_pos, new_pos, matrix):
        ppx = prev_pos[0]
        ppy = prev_pos[1]
        npx = new_pos[0]
        npy = new_pos[1]

        if ppx - 2 == npx:
            if ppy - 1 == npy or ppy + 1 == npy:
                return True

        if ppx - 1 == npx:
            if ppy - 2 == npy or ppy + 2 == npy:
                return True

        if ppx + 1 == npx:
            if ppy - 2 == npy or ppy + 2 == npy:
                return True

        if ppx + 2 == npx:
            if ppy - 1 == npy or ppy + 1 == npy:
                return True

        return False
