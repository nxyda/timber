import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Timber Stacking")
clock = pygame.time.Clock()

timber_left_img = pygame.image.load('timber/timber_left.png').convert_alpha()
timber_right_img = pygame.image.load('timber/timber_right.png').convert_alpha()
timber_img = pygame.image.load('timber/timber.png').convert_alpha()
player_img = pygame.image.load('timber/player.png').convert_alpha()

timber_width, timber_height = timber_img.get_rect().size
timber_left_width = timber_left_img.get_rect().width
timber_right_width = timber_right_img.get_rect().width

player_height = timber_height
player_width = int(player_img.get_rect().width *
                   (player_height / player_img.get_rect().height))
player_img = pygame.transform.scale(player_img, (player_width, player_height))

left_player_x = (SCREEN_WIDTH - timber_width) // 2 - player_width - 60
right_player_x = (SCREEN_WIDTH - timber_width) // 2 + timber_width + 10
player_y = SCREEN_HEIGHT - player_height

player_x = right_player_x

start_y = SCREEN_HEIGHT - timber_height

blocks = []
block_type_3 = "aaa"
for i in range(1000):
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


def move_blocks_down():
    if blocks:
        blocks.pop(0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x = left_player_x
                move_blocks_down()
            elif event.key == pygame.K_RIGHT:
                player_x = right_player_x
                move_blocks_down()

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

    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()
    clock.tick(FPS)
