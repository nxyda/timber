import pygame
import sys

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

# Wczytywanie obrazka
timber_img = pygame.image.load('timber.png').convert_alpha()

# Ustalanie pozycji bloków
timber_rect = timber_img.get_rect()
timber_width, timber_height = timber_rect.size

# Obliczanie pozycji początkowej dla 8 bloków na środku ekranu
start_x = (SCREEN_WIDTH - timber_width) // 2
start_y = (SCREEN_HEIGHT - (8 * timber_height)) // 2

# Pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rysowanie
    screen.fill(WHITE)

    for i in range(8):
        y_position = start_y + i * timber_height
        screen.blit(timber_img, (start_x, y_position))

    pygame.display.update()
    clock.tick(FPS)
