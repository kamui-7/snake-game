from dataclasses import dataclass
import pygame
from . import constants

speed = constants.speed


@dataclass
class Coor():

    x: int
    y: int


class Snake():

    def __init__(self):
        self.body = [Coor(20, 20)]
        self.dx = speed
        self.dy = 0

    def draw(self, win):
        for cell in self.body:
            pygame.draw.rect(win, constants.snake_color,
                             (cell.x, cell.y, constants.size, constants.size))

    def update(self, fruit):
        head = Coor(self.body[0].x + self.dx, self.body[0].y + self.dy)
        self.body.insert(0, head)
        if self.eat(fruit):
            return True
        else:
            self.body.pop()

    def eat(self, fruit):
        rect = pygame.Rect(
            self.body[0].x, self.body[0].y, constants.size, constants.size)
        if rect.colliderect(fruit.rect):
            return True

    def up(self):
        self.dx = 0
        self.dy = -speed

    def right(self):
        self.dx = speed
        self.dy = 0

    def left(self):
        self.dx = -speed
        self.dy = 0

    def down(self):
        self.dx = 0
        self.dy = speed

    def gameOver(self):

        for cell in self.body:
            if cell.x > constants.width - constants.size or cell.x < 0 or \
                    cell.y > constants.height - constants.size or cell.y < 0:
                return False

        if len(self.body) == 1:
            return True

        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return False

        return True
