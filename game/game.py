"""
Main game loop
"""

import pygame
from pygame.locals import *

from game.game_objects import GameObject, Item
from .keymap import GameActions, Keymap
from .player import Player


class Game:
    __keymap: Keymap
    __player: Player = None
    __objects = []

    __window_size: tuple = None
    __config = None

    def __init__(self, config):
        default = config["DEFAULT"]
        self.__window_size = (default.getint("screen_width"), default.getint("screen_height"))
        self.__keymap = Keymap(default["keymap_config"])
        pygame.init()

    def game_loop(self):
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
                    action: GameActions = self.__keymap.map_key(event.key)
                    if action is None:
                        continue
                    # Should only happen once per keypress
                    if GameActions.PLAYER_ITEM_SELECT_0.value <= action.value <= GameActions.PLAYER_ITEM_SELECT_9.value \
                            and event.type == KEYDOWN:
                        self.__player.game_action(action)
                    else:
                        self.__player.game_action(action)

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
            collides_with = self.find_objects(self.__player.image.get_width(), self.__player.image.get_height(),
                                              self.__player.position.x, self.__player.position.y)
            for o in collides_with:
                if isinstance(o, Item):
                    self.__player.new_item(o)
                    # this might cause problems, if the object matches others, cuz this removes the first match
                    self.__objects.remove(o)

    def spawn(self, game_object: GameObject):
        # game_object.index_id = len(self.__objects)
        self.__objects.append(game_object)

    def find_objects(self, a: float, b: float, x: float, y: float, collide_only: bool = False):
        """

        :param collide_only: if you only care about collision, use this flag
        :param a: size of the area in the "x" direction
        :param b: size of the area in the "x" direction
        :param x: x position of the top left corner of the area
        :param y: y position of the top left corner of the area
        :return: list of objects that are considered inside the area
        """
        result = []
        for o in self.__objects:
            if x - o.image.get_width() < o.position.x < x + a and y - o.image.get_height() < o.position.y < y + b:
                result.append(o)
                if collide_only:
                    return True
        return result
