import sys
from random import randint
from time import time

import pygame

from bird import Bird
from black_statistics import Statistics
from constants import Constants
from game_states import State, StartMenu, RestartMenu, GameRunning
from hole import Hole
from sound import Sound


def gen_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def start_set():
    """ Game variables to create new game
     Returns: bird, holes, statistics and stopwatch """

    Hole.restart_hole()
    return (Bird((0, 173, 181), (Constants.WINDOW_WIDTH // 4, Constants.WINDOW_HEIGHT // 2,)),
            [Hole()], Statistics(), time())


def start_game():
    def run_state(state: State):
        nonlocal bird, holes, statistics, stopwatch

        match state:
            case State.StartMenu:
                return StartMenu.run(screen, on, statistics, stopwatch, clock, bird, holes)
            case State.RestartMenu:
                return RestartMenu.run(screen, on, statistics, stopwatch, clock, bird, holes)
            case State.GameRunning:
                return GameRunning.run(screen, on, statistics, stopwatch, clock, bird, holes)

    # Main variables
    screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT,))
    clock = pygame.time.Clock()
    state = State.StartMenu
    Sound.start_background_music()

    # Game variables
    bird, holes, statistics, stopwatch = start_set()
    on = True

    while on:
        clock.tick(Constants.FPS)
        prev_state = state
        on, state = run_state(state)

        if prev_state != state and state == State.GameRunning:
            bird, holes, statistics, stopwatch = start_set()


def main():
    pygame.init()
    start_game()

    # Quiting the game
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
