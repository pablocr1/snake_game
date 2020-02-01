import pygame, random
from pygame import *

pygame.init()
# Define a resolução do jogo
screen = pygame.display.set_mode((600, 600))
# Define o nome da janela
pygame.display.set_caption('Snake Game')

# Direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Posição da cobra
snake = [(200, 200), (210, 200), (220, 200)]
# Define skin da cobra
snake_skin = pygame.Surface((10, 10))
# Cor da cobra
snake_skin.fill((255, 255, 255))

apple_position = (random.randint(0, 590), random.randint(0, 590))
# Define skin da maçã
apple = pygame.Surface((10, 10))
# Cor da maçã
apple.fill((0, 0, 255))

my_direction = LEFT

# Limitar o FPS
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_position)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
