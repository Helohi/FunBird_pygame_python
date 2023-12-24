import typing
from random import randint
from constants import Constants
from pygame import Surface, gfxdraw
from game_object import GameObject


class Bird(GameObject):
    def __init__(self, color, position: typing.Iterable = None, size: int = Constants.SIZE_OF_BIRD, width: int = 0):
        self.position = list(position) if position else [randint(10, Constants.WINDOW_WIDTH - 10),
                                                         randint(10, Constants.WINDOW_HEIGHT - 10), ]
        self.size = size
        self.color = color
        self.width = width
        self.speed = 0
        self.points = Constants.Points

    def make_move(self, surface: Surface):
        self.move()
        gfxdraw.filled_circle(surface, *self.position, self.size, self.color)
        return self.is_alive()

    def jump(self):
        self.speed = 15

    def move(self):
        self.position[1] = self.position[1] - self.speed
        self.speed = max(self.speed - 1, Constants.MAX_GRAVITATION)

    def is_alive(self):
        if self.position[1] - self.size > Constants.WINDOW_HEIGHT:
            self.position[1] = -self.size
        elif self.position[1] + self.size < 0:
            self.position[1] = Constants.WINDOW_HEIGHT + self.size
        return True
