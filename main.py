import pygame
import sys
from constants import Constants
from random import randint
from bird import Bird
from menu import Menu, MenuEnum
from hole import Hole
from black_statistics import Statistics
from time import time, gmtime
import asyncio


def gen_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def start_set():
    """ Game variables to create new game
     Returns: bird, holes, statistics and stopwatch """

    Hole.restart_hole()
    return (Bird((0, 173, 181), (Constants.WINDOW_WIDTH // 4, Constants.WINDOW_HEIGHT // 2,)),
            [Hole()], Statistics(), time())


async def main():
    def exit_menu():
        nonlocal is_menu, stopwatch, bird, holes, statistics, stopwatch

        if is_menu[1].what_menu == MenuEnum.RESTART:
            bird, holes, statistics, stopwatch = start_set()
        elif is_menu[1].what_menu == MenuEnum.START:
            stopwatch = time()
        is_menu = [False, None]

    pygame.init()

    # Main variables
    screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT,))
    clock = pygame.time.Clock()
    is_menu = (True, Menu(screen))

    # Game variables
    bird, holes, statistics, stopwatch = start_set()
    on = True

    while on:
        clock.tick(Constants.FPS)  # set FPS
        await asyncio.sleep(0)

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if is_menu[0]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        exit_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Menu.is_clicked(pygame.mouse.get_pos()):
                        exit_menu()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.jump()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    bird.jump()

        # Drawing window
        screen.fill((34, 40, 49,))  # Background
        # Draw statistics
        statistics.draw(screen, gmtime(time() - stopwatch), bird.points, clock.get_fps())

        if is_menu[0]:  # Menu
            is_menu[1].draw()
        else:  # Game
            # Draw bird
            if not bird.make_move(screen):
                is_menu = (True, Menu(screen, MenuEnum.RESTART))

            # Draw holes
            last_hole = None
            for i, hole in enumerate(holes):
                if hole.is_valuable and hole.is_needed_to_check(bird):
                    if hole.is_bird_in(bird):
                        hole.is_valuable = False
                        bird.points += Hole.POINT_GIVEN
                    elif bird.position[0] - bird.size < hole.pos[0] + hole.size[0]:
                        pass
                    else:
                        is_menu = (True, Menu(screen, MenuEnum.RESTART))

                if not hole.make_move(screen):
                    del holes[i]
                    continue

                last_hole = hole
            if last_hole and Constants.WINDOW_WIDTH - last_hole.pos[0] >= Hole.SPACE_BETWEEN:
                holes.append(Hole())

        pygame.display.update()  # Update using changes

    # Quiting the game
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    asyncio.run(main())
