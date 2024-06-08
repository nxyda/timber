import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Stałe
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Kolory
WHITE = (255, 255, 255)

# Ustawienia ekranu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Timber Stacking")
clock = pygame.time.Clock()

# Wczytywanie obrazków
timber_left_img = pygame.image.load('timber/timber_left.png').convert_alpha()
timber_right_img = pygame.image.load('timber/timber_right.png').convert_alpha()
timber_img = pygame.image.load('timber/timber.png').convert_alpha()
player_img = pygame.image.load(
    'timber/player.png').convert_alpha()  # Wczytanie obrazka gracza

# Ustalanie pozycji bloków
timber_width, timber_height = timber_img.get_rect().size
timber_left_width = timber_left_img.get_rect().width
timber_right_width = timber_right_img.get_rect().width

# Skalowanie obrazu gracza do wysokości drewna
player_height = timber_height
player_width = int(player_img.get_rect().width *
                   (player_height / player_img.get_rect().height))
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Pozycja gracza
player_x = (
    SCREEN_WIDTH - player_width
) // 2 + timber_width + 10  # Umieszczenie gracza po prawej stronie drzewa
player_y = SCREEN_HEIGHT - player_height  # Umieszczenie na samym dole ekranu

# Obliczanie pozycji początkowej dla 8 bloków zaczynając od dołu ekranu
start_y = SCREEN_HEIGHT - timber_height

# Generowanie bloków
blocks = []
block_type_3 = "aaa"
for i in range(20):
    block_type = random.choice(['left', 'right'])
    block_type_2 = random.choice(['left', 'right'])
    if block_type != block_type_3:
        blocks.append("aaa")
    if block_type_2 != block_type:
        blocks.append(block_type)
        blocks.append("aaa")
        blocks.append(block_type_2)
    else:
        blocks.append(block_type)
        blocks.append(block_type_2)

    block_type_3 = block_type_2

# Pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rysowanie
    screen.fill(WHITE)

    for i, block_type in enumerate(blocks):
        y_position = start_y - i * timber_height
        if block_type == 'left':
            x_position = (SCREEN_WIDTH - timber_left_width) // 2 - 57
            screen.blit(timber_left_img, (x_position, y_position))
        elif block_type == 'right':
            x_position = (SCREEN_WIDTH - timber_right_width) // 2
            screen.blit(timber_right_img, (x_position, y_position))
        else:
            x_position = (SCREEN_WIDTH - timber_width) // 2 - 28
            screen.blit(timber_img, (x_position, y_position))

    # Rysowanie gracza
    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()
    clock.tick(FPS)
