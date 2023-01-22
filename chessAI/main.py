import pygame

# CONSTANTS
window_size = (610, 610)
ss = 70  # square side
spa = 25  # square position adjustment
background_color = (153, 107, 0)
white_square_color = (255, 245, 219)
black_square_color = (214, 171, 62)
dpap_x = 19  # draw piece adjustment pointer
dpap_y = 4  # draw piece adjustment pointer
black_rook = pygame.image.load("res/pieces/black_rook.png")
black_knight = pygame.image.load("res/pieces/black_knight.png")
black_bishop = pygame.image.load("res/pieces/black_bishop.png")
black_queen = pygame.image.load("res/pieces/black_queen.png")
black_king = pygame.image.load("res/pieces/black_king.png")
black_pawn = pygame.image.load("res/pieces/black_pawn.png")
white_rook = pygame.image.load("res/pieces/white_rook.png")
white_knight = pygame.image.load("res/pieces/white_knight.png")
white_bishop = pygame.image.load("res/pieces/white_bishop.png")
white_queen = pygame.image.load("res/pieces/white_queen.png")
white_king = pygame.image.load("res/pieces/white_king.png")
white_pawn = pygame.image.load("res/pieces/white_pawn.png")


# Initialize screen
pygame.init()
screen = pygame.display.set_mode(window_size)


# draws text
def draw_text(surface, text, pos, font):
    text = str(text)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = pos
    surface.blit(text_surface, text_rect)


# draws a piece
def draw_piece(symbol, pos):
    row = int((pos / 8) - 0.1)
    x_index_ = 8 if pos % 8 == 0 else pos % 8
    x_pos = (x_index_ * ss) + dpap_x - black_rook.get_width()
    y_pos = (row * ss) + dpap_y + (black_rook.get_width() / 2)
    if symbol == 'r':
        screen.blit(black_rook, (x_pos, y_pos))
    elif symbol == 'n':
        screen.blit(black_knight, (x_pos, y_pos))
    elif symbol == 'b':
        screen.blit(black_bishop, (x_pos, y_pos))
    elif symbol == 'q':
        screen.blit(black_queen, (x_pos, y_pos))
    elif symbol == 'k':
        screen.blit(black_king, (x_pos, y_pos))
    elif symbol == 'p':
        screen.blit(black_pawn, (x_pos, y_pos))
    elif symbol == 'R':
        screen.blit(white_rook, (x_pos, y_pos))
    elif symbol == 'N':
        screen.blit(white_knight, (x_pos, y_pos))
    elif symbol == 'B':
        screen.blit(white_bishop, (x_pos, y_pos))
    elif symbol == 'Q':
        screen.blit(white_queen, (x_pos, y_pos))
    elif symbol == 'K':
        screen.blit(white_king, (x_pos, y_pos))
    elif symbol == 'P':
        screen.blit(white_pawn, (x_pos, y_pos))


# converts the damn numbers to letters
def damn_letters(index):
    if index == 1:
        return "a"
    elif index == 2:
        return "b"
    elif index == 3:
        return "c"
    elif index == 4:
        return "d"
    elif index == 5:
        return "e"
    elif index == 6:
        return "f"
    elif index == 7:
        return "g"
    elif index == 8:
        return "h"


# Initialize board
font = pygame.font.Font(pygame.font.get_default_font(), 22)
screen.fill(background_color)
for r in range(0, 8):
    for c in range(0, 8):
        if (r + c) % 2 == 0:
            square_color = white_square_color
        else:
            square_color = black_square_color
        pygame.draw.rect(screen, square_color, pygame.Rect(r * ss + spa, c * ss + spa, ss, ss))


# side letters and numbers
for i in range(97, 105):
    index = i - 96
    draw_text(screen, str(index), (spa + (index * ss - (ss/2)), 2), font)
    draw_text(screen, str(index), (spa + (index * ss - (ss/2)), 666), font)
    draw_text(screen, damn_letters(index), (677, spa + (index * ss - (ss/2)) - 10), font)
    draw_text(screen, damn_letters(index), (12.5, spa + (index * ss - (ss/2)) - 10), font)


# Chess pieces
starting_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
position_counter = 1
for symbol in starting_FEN:
    if symbol.isdigit():
        position_counter = position_counter + int(symbol)
    elif symbol == '/':
        pass
    else:
        draw_piece(symbol, position_counter)
        position_counter = position_counter + 1


pygame.display.flip()  # maybe draws ??
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


if game_over:
    pygame.quit()