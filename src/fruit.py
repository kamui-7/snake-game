import pygame
from . import constants

speed = constants.speed


class Fruit():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, constants.size, constants.size)

    def draw(self, win):
        pygame.draw.rect(win, constants.fruit_color, self.rect)
