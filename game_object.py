from abc import ABC, abstractmethod

import pygame


class GameObject(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def make_move(self, surface):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass
