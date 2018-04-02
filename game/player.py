"""
Player
"""
from enum import Enum, unique

from numpy import array

from .game_types import GameObject


@unique
class PlayerActions(Enum):
    MOVE_UP = 0
    MOVE_DOWN = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3


class Player(GameObject):
    position = [0.0, 0.0]
    up, down, right, left = False, False, False, False
    name = "Player"

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def game_action(self, player_action, **kwargs):
        """

        :param player_action: PlayerAction enum
        :param kwargs: arguments for that specific action see PlayerAction
        :return: nothing
        """
        # for k, v in kwargs:
        print("PlayerAction (%s) inputs: " % player_action, kwargs)
        if player_action == PlayerActions.MOVE_UP:
            self.up = not self.up
        elif player_action == PlayerActions.MOVE_DOWN:
            self.down = not self.down
        elif player_action == PlayerActions.MOVE_LEFT:
            self.left = not self.left
        elif player_action == PlayerActions.MOVE_RIGHT:
            self.right = not self.right
        else:
            print("Unknown PlayerAction!")

    def get_direction(self):
        direction = array([0.0, 0.0], "f")
        if self.up:
            direction[1] -= 1.0
        if self.down:
            direction[1] += 1.0
        if self.left:
            direction[0] -= 1.0
        if self.right:
            direction[0] += 1.0
        return direction
