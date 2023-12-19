from enum import Enum
from time import gmtime, time
from typing import List
from random import choice

import pygame.event
from pygame.time import Clock

from bird import Bird
from black_statistics import Statistics
from constants import Constants
from hole import Hole, HoleType
from menu import Menu, MenuEnum


class State(Enum):
    StartMenu = 1
    RestartMenu = 2
    GameRunning = 3


class StartMenu:
    @staticmethod
    def run(screen: pygame.Surface, on: bool, statistics: Statistics, stopwatch, clock: Clock, bird: Bird,
            *args, **kwargs) -> (bool, State,):
        next_state = State.StartMenu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_s:
                    next_state = State.GameRunning
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Menu.is_clicked(pygame.mouse.get_pos(), MenuEnum.START):
                    next_state = State.GameRunning

        # Draw window
        screen.fill(Constants.BACKGROUND_COLOR)
        # Draw statistics
        statistics.draw(screen, gmtime(time() - stopwatch), bird.points, clock.get_fps())

        Menu(screen, MenuEnum.START).draw()
        pygame.display.update()
        return on, next_state


class RestartMenu:
    @staticmethod
    def run(screen: pygame.Surface, on: bool, statistics: Statistics, stopwatch, clock: Clock, bird: Bird,
            *args, **kwargs) -> (bool, State,):
        next_state = State.RestartMenu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_s:
                    next_state = State.GameRunning
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Menu.is_clicked(pygame.mouse.get_pos(), MenuEnum.RESTART):
                    next_state = State.GameRunning

        # Draw window
        screen.fill(Constants.BACKGROUND_COLOR)
        # Draw statistics
        statistics.draw(screen, gmtime(time() - stopwatch), bird.points, clock.get_fps())

        Menu(screen, MenuEnum.RESTART).draw()
        pygame.display.update()
        return on, next_state


class GameRunning:
    Hole_TYPE_CHANCE = [HoleType.Static] * 90 + [HoleType.Dynamic] * 10

    @staticmethod
    def run(screen: pygame.Surface, on: bool, statistics: Statistics, stopwatch, clock: Clock, bird: Bird,
            holes: List[Hole], *args, **kwargs) -> (bool, State,):
        next_state = State.GameRunning

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bird.jump()

        # Drawing
        screen.fill(Constants.BACKGROUND_COLOR)
        statistics.draw(screen, gmtime(time() - stopwatch), bird.points, clock.get_fps())

        # Draw bird
        if not bird.make_move(screen):
            next_state = State.RestartMenu

        # Draw holes
        last_hole = None
        for i, hole in enumerate(holes):
            if hole.is_valuable and hole.is_needed_to_check(bird):
                if hole.is_bird_in(bird):
                    hole.is_valuable = False
                    hole.color = (0, 173, 181)
                    bird.points += Hole.POINT_GIVEN
                elif bird.position[0] - bird.size < hole.pos[0] + hole.size[0]:
                    pass
                else:
                    next_state = State.RestartMenu

            if not hole.make_move(screen):
                del holes[i]
                continue
            last_hole = hole

        if last_hole and Constants.WINDOW_WIDTH - last_hole.pos[0] >= Hole.SPACE_BETWEEN:
            holes.append(Hole(hole_type=choice(GameRunning.Hole_TYPE_CHANCE)))

        pygame.display.update()

        return on, next_state
