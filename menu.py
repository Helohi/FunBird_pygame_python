import pygame
from constants import Constants


class MenuEnum:
    START = 1
    RESTART = 2


class Menu(MenuEnum):
    _font_size = 48
    _start_button_prop = (Constants.WINDOW_WIDTH // 2 - 100 // 2,
                          Constants.WINDOW_HEIGHT // 2 - _font_size // 2, 100, _font_size)
    _restart_button_prop = ((Constants.WINDOW_WIDTH // 2 - 150 // 2,
                             Constants.WINDOW_HEIGHT // 2 - _font_size // 2, 150, _font_size))

    def __init__(self, surface: pygame.Surface, what_menu: MenuEnum = MenuEnum.START, font_name: str = 'Corbel'):
        self.surface = surface
        self.what_menu = what_menu
        self.font = pygame.font.SysFont(font_name, self._font_size)

    def draw(self):
        if self.what_menu == MenuEnum.START:
            pygame.draw.rect(self.surface, (57, 62, 70), self._start_button_prop)

            self.surface.blit(self.font.render('Start', True, pygame.color.THECOLORS['white']),
                              self._start_button_prop[0:2], )

        elif self.what_menu == MenuEnum.RESTART:
            pygame.draw.rect(self.surface, (57, 62, 70), self._restart_button_prop)

            self.surface.blit(self.font.render('Restart', True, pygame.color.THECOLORS['white']),
                              self._restart_button_prop[0:2], )

    @staticmethod
    def is_clicked(mouse_pos: tuple[int, int], what_menu: MenuEnum):
        match what_menu:
            case MenuEnum.START:
                return MenuEnum.START if (Menu._start_button_prop[0] <=
                                          mouse_pos[0] <= Menu._start_button_prop[0] + Menu._start_button_prop[2] and
                                          Menu._start_button_prop[1] <=
                                          mouse_pos[1] <= Menu._start_button_prop[1] + Menu._start_button_prop[3]) \
                    else False
            case MenuEnum.RESTART:
                return MenuEnum.START if (Menu._restart_button_prop[0] <= mouse_pos[0] <= Menu._restart_button_prop[0] +
                                          Menu._restart_button_prop[2] and Menu._restart_button_prop[1] <= mouse_pos[
                                              1] <= Menu._restart_button_prop[1] + Menu._restart_button_prop[3]) \
                    else False
