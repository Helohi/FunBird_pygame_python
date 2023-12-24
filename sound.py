import pygame


class Sound:
    @staticmethod
    def play_boing():
        return pygame.mixer.Sound('./assets/boing.wav').play()

    @staticmethod
    def play_point_gain():
        return pygame.mixer.Sound('./assets/point.wav').play()
