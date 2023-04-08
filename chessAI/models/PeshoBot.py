import GlobalVariables
from models.pieces.Piece import Piece


class PeshoBot:
    def __init__(self, color):
        self.coloredPieces = [None, None, None, None, None, None, None, None,
                              None, None, None, None, None, None, None, None]  # Initialize Pieces of the bot
        self.next_move = None
        self.pieceToMove = None
        self.color = color
        i = 0
        for r in range(0, 8):
            for c in range(0, 8):
                if GlobalVariables.board.matrix[r][c] is not None:  # if we find a piece
                    if GlobalVariables.board.matrix[r][c].color == self.color:  # of the given color
                        self.coloredPieces[i] = GlobalVariables.board.matrix[r][c]  # we save it
                        i = i + 1

    def SyncBoard(self):  # in the case of the bot moving their piece, we must upadte it in self.coloredPieces, otherwise this method will delete the moved piece
        syncArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # array of the positions in self.coloredPieces that we found
        for r in range(0, 8):
            for c in range(0, 8):
                curr_piece = GlobalVariables.board.matrix[r][c]
                if curr_piece is not None:  # if we find a piece
                    if curr_piece.color == self.color:  # of the given color
                        for i in range(0, 16):  # search from the bot's pieces
                            our_curr_piece = self.coloredPieces[i]
                            if our_curr_piece is not None:  # if the find a piece
                                if our_curr_piece.position == curr_piece.position:  # at the same position
                                    syncArray[i] = 1
                                    self.coloredPieces[i] = curr_piece  # we save it's state

        for i in range(0, 16):  # go trough the syncArray
            if syncArray[i] == 0:  # if we have piece that is not found
                self.coloredPieces[i] = None  # it must have been captured, we delete it

    def GenerateRandomMove(self):
        madeAMove = False
        while not madeAMove:
            number = GlobalVariables.random.randint(0, 15)  # random number
            while self.coloredPieces[number] is None:  # until we find a random number
                number = GlobalVariables.random.randint(0, 15)  # we regenerate

            self.pieceToMove = self.coloredPieces[number]
            valid_moves = []

            for x in range(0, 8):
                for y in range(0, 8):
                    if self.pieceToMove.is_valid_move(self.pieceToMove.position, (x, y)):
                        if x != self.coloredPieces[number].position[0] or y != self.coloredPieces[number].position[1]:
                            valid_moves.append((x, y))
                    else:
                        GlobalVariables.board.matrix[self.pieceToMove.position[0]][self.pieceToMove.position[1]] = self.pieceToMove

            if len(valid_moves) > 0:
                madeAMove = True

        self.next_move = valid_moves[GlobalVariables.random.randint(0, len(valid_moves) - 1)]

    pass