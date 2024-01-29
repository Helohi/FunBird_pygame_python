import pygame


class Sound:
    @staticmethod
    def play_boing():
        sound = pygame.mixer.Sound('./assets/boing.wav')
        sound.set_volume(1)
        return sound.play()

    @staticmethod
    def play_point_gain():
        sound = pygame.mixer.Sound('./assets/point.wav')
        sound.set_volume(1)
        return sound.play()

    @staticmethod
    def start_background_music():
        pygame.mixer.music.load('./assets/newMusic.wav')
        pygame.mixer_music.queue('./assets/GameMusic.wav', loops=1)
        pygame.mixer.music.set_volume(0.1)
        return pygame.mixer.music.play(-1)
