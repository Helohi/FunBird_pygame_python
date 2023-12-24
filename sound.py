import pygame


class Sound:
    @staticmethod
    def play_boing():
        return pygame.mixer.Sound('./assets/boing.wav').play()
