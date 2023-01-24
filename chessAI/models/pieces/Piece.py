import pygame


class Piece:
    def __init__(self, color: object, position: object, image: object) -> object:
        self.color = color
        self.position = position
        self.image = pygame.image.load(image)

    def new_position(self, pos):
        self.position = pos

    def is_valid_move(self, prev_pos, new_pos, matrix):
        pass
