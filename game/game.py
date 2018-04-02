"""
Main game loop
"""
from math import acos, pi, sqrt

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
        # config_file = kwargs.get("config")

    #
    # def tick(self, dt):
    #     self.__player.update(dt)

    def game_loop(self):
        self.__window_size = (800, 600)
        self.__player = Player(0, 0, "Player")
        pygame.init()
        screen = pygame.display.set_mode(self.__window_size)
        clock = pygame.time.Clock()

        player_image = pygame.image.load("data/Player.png").convert_alpha()
        player_image = pygame.transform.rotate(player_image, -90)
        background = pygame.Surface(screen.get_size()).convert()
        background.fill((30, 200, 30))

        run = True

        while run:
            delta_time = clock.get_time()
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                elif event.type == KEYDOWN or event.type == KEYUP:
                    if event.key == K_w:
                        self.__player.game_action(PlayerActions.MOVE_UP)
                    if event.key == K_a:
                        self.__player.game_action(PlayerActions.MOVE_LEFT)
                    if event.key == K_s:
                        self.__player.game_action(PlayerActions.MOVE_DOWN)
                    if event.key == K_d:
                        self.__player.game_action(PlayerActions.MOVE_RIGHT)

            direction = self.__player.get_direction()
            self.__player.position = self.__player.position + (direction * (delta_time / 10))
            # Calculate angle between (1.0, 0.0) and player.direction
            # They are both normalized =>
            rot_player = player_image
            if direction[0] != 0.0 or direction[1] != 0.0:
                deg = (acos(direction[0] / sqrt(direction[0] ** 2 + direction[1] ** 2)) * 180) / pi
                if direction[1] > 0.0:
                    deg = -deg
                print(deg)
                rot_player = pygame.transform.rotate(player_image, deg)

            # print(self.__player.position)
            screen.blit(background, (0, 0))
            screen.blit(rot_player, tuple(self.__player.position))  # , special_flags=pygame.BLEND_RGBA_MULT)
            pygame.display.update()
            clock.tick(60)
