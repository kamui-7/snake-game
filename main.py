from src import snake
from src import fruit
from src import constants

import pygame
import random

from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_a, K_s, K_d


pygame.init()


win = pygame.display.set_mode((constants.width, constants.height))
snake = snake.Snake()


def gen_fruit():
    x = random.randrange(constants.size, constants.width - constants.size)
    y = random.randrange(constants.size, constants.height - constants.size)

    for cell in snake.body:
        if coor2rect(x, y).colliderect(coor2rect(cell.x, cell.y)):
            gen_fruit()

    return fruit.Fruit(x, y)


def coor2rect(x, y):
    return pygame.Rect(x, y, constants.size, constants.size)


esa = gen_fruit()

clock = pygame.time.Clock()
gameOver = True
while gameOver:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == K_LEFT or event.key == K_a:
                snake.left()

            if event.key == K_RIGHT or event.key == K_d:
                snake.right()

            if event.key == K_UP or event.key == K_w:
                snake.up()

            if event.key == K_DOWN or event.key == K_s:
                snake.down()

    gameOver = snake.gameOver()
    clock.tick(30)

    win.fill(constants.back_color)
    snake.draw(win)
    esa.draw(win)
    eaten = snake.update(esa)

    if eaten:
        esa = gen_fruit()

    pygame.display.flip()
