from constants import Constants
from random import randint, choice
from game_object import GameObject
from pygame import draw
from bird import Bird
from enum import Enum


class HoleType(Enum):
    Static = 1
    Dynamic = 2


class Hole(GameObject):
    NEXT_HEIGHT = 300
    SPACE_BETWEEN = 500
    POINT_GIVEN = 1
    speed = 5

    def __init__(self, hole_type: HoleType = HoleType.Static):
        self.color = (238, 238, 238)
        self.size = 20, Hole.NEXT_HEIGHT
        self.pos = [Constants.WINDOW_WIDTH, randint(0, Constants.WINDOW_HEIGHT - int(self.size[1]))]  # x, y
        self.is_valuable = True
        self.hole_type = hole_type
        self.ver_speed = choice((Hole.speed//2, -Hole.speed//2))

        Hole.NEXT_HEIGHT = max(Hole.NEXT_HEIGHT * 0.98, Constants.SIZE_OF_BIRD * 3)

    def make_move(self, surface):
        self.move()
        draw.rect(surface, self.color, [*self.pos, *self.size])

        return self.is_alive()

    def move(self):
        self.pos[0] -= Hole.speed
        Hole.speed = min(100 * 1000, int((Hole.speed + 0.01) * 1000)) / 1000

        if self.hole_type == HoleType.Dynamic:
            self.pos[1] += self.ver_speed
            if self.pos[1] <= 0 or self.pos[1] + self.size[1] >= Constants.WINDOW_HEIGHT:
                self.ver_speed = -self.ver_speed

    def is_alive(self):
        if self.pos[0] < 0:
            return False
        return True

    def is_bird_in(self, bird: Bird):
        if (self.pos[1] <= bird.position[1] + bird.size <= self.pos[1] + self.size[1]
                or self.pos[1] <= bird.position[1] - bird.size <= self.pos[1] + self.size[1]):
            return True
        return False

    def is_needed_to_check(self, bird: Bird):
        if self.pos[0] + self.size[0] < bird.position[0] + bird.size:
            return True
        return False

    @staticmethod
    def restart_hole():
        Hole.NEXT_HEIGHT = 300
        Hole.SPACE_BETWEEN = 500
        Hole.JUMPS_GIVEN = 2
        Hole.speed = 5
