from pathlib import Path

import pygame

from constants import Constants


class LeaderBoard:
    def __init__(self, text_font: str = 'Corbel', text_size: int = 20, frame_color: tuple[int, int, int] = (0, 0, 0,)):
        self.font = pygame.font.SysFont(text_font, text_size)
        self.frame_color = frame_color
        self.leaders = dict()
        self.parse_data('.\\leaderboard.dat')

    def parse_data(self, filedir: str):
        if Path(filedir).exists():
            with open(filedir, 'r') as file:
                line = file.readline().strip()
                while line and len(self.leaders) <= 5:
                    nick, score = line.split()
                    self.leaders[nick] = score

        if len(self.leaders) < 5:
            for _ in range(5 - len(self.leaders)):
                self.leaders['NAN'] = 0

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.frame_color, [0, Constants.WINDOW_HEIGHT-100, 100, 100])

        title = self.font.render('TOP POINTS', True, (255, 255, 255,))

