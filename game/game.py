"""
Main game loop
"""

import pygame
from pygame.locals import *

from .player import Player, PlayerActions


class Game:
    __enemies = []
    __player = None
    __objects = None

    __window_size = None
    __config = None

    def __init__(self, **kwargs):
        self.__window_size = kwargs.get("windows_size", (800, 600))

    def game_loop(self):
        pygame.init()
        self.__window_size = (800, 600)
        screen = pygame.display.set_mode(self.__window_size)
        clock = pygame.time.Clock()

        background = pygame.Surface(screen.get_size()).convert()
        background.fill((30, 200, 30))

        self.__player = Player(1, 1)
        run = True

        while run:
            delta_time = clock.get_time()
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                elif event.type == KEYDOWN or event.type == KEYUP:
                    if event.key == K_w:
                        self.__player.game_action(PlayerActions.MOVE_UP)
                    elif event.key == K_a:
                        self.__player.game_action(PlayerActions.MOVE_LEFT)
                    elif event.key == K_s:
                        self.__player.game_action(PlayerActions.MOVE_DOWN)
                    elif event.key == K_d:
                        self.__player.game_action(PlayerActions.MOVE_RIGHT)
                    elif event.key == K_SPACE:
                        self.__player.game_action(PlayerActions.USE)
                    elif K_0 <= event.key <= K_9 and event.type == KEYDOWN:
                        self.__player.game_action(PlayerActions.PICK, item_index=event.key - K_0)

            # print(self.__player.position)
            self.move_and_collide(delta_time)
            screen.blit(background, (0, 0))
            self.__player.render(delta_time, screen)
            pygame.display.update()
            clock.tick(60)

    def move_and_collide(self, dt: int):
        if self.__player.moving:

            new_position = self.__player.position + self.__player.direction_vector * (dt / 10)
            if 0 < new_position.x < self.__window_size[0] - 32 and 0 < new_position.y < self.__window_size[1] - 32:
                self.__player.position = new_position
