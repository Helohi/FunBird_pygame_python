import pygame
import time
from constants import Constants


class Statistics:
    def __init__(self, pos: tuple[int, int] = (0, 0,), frame_size: tuple[int, int] = (210, 60,),
                 frame_color: tuple[int, int, int] = (0, 0, 0,), text_size: int = 20,
                 text_color: (0, 0, 0,) = (255, 255, 255,), text_font: str = 'Corbel'):
        self.pos = pos
        self.frame_size = frame_size
        self.frame_color = frame_color
        self.text_size = text_size
        self.text_color = text_color
        self.text_font = text_font

        self.font = pygame.font.SysFont(self.text_font, self.text_size)

    def draw(self, surface: pygame.Surface, time_: time.struct_time, points: int, fps: float):
        pygame.draw.rect(surface, self.frame_color, [*self.pos, *self.frame_size])

        points_gained = self.font.render(f'Point(s): {points}', True, self.text_color)
        time_text = self.font.render(f'Time in a game: {time.strftime("%M:%S", time_)}', True, self.text_color)
        fps_text = self.font.render(f'FPS: {int(fps)}', True, self.text_color)

        points_gained_big = pygame.font.SysFont(self.text_font, 500).render(f'{points}', False, (57, 62, 70))

        surface.blit(points_gained, self.pos)
        surface.blit(time_text, (self.pos[0], self.pos[1] + self.text_size))
        surface.blit(fps_text, (self.pos[0], self.pos[1] + self.text_size * 2))
        surface.blit(points_gained_big, (Constants.WINDOW_WIDTH//2, Constants.WINDOW_HEIGHT//9))
