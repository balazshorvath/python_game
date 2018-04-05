"""
Player
"""
import pygame
from pygame.math import Vector2

from .keymap import GameActions


class Player:
    reference_vector: Vector2 = pygame.math.Vector2(1.0, 0.0)
    position: Vector2
    direction_angle: float = 0.0
    direction_vector: Vector2 = reference_vector

    moving: bool = False
    attacking: int = 0
    image: pygame.Surface
    image_attack: pygame.Surface
    image_target: pygame.Surface
    image_items = []

    current_item: int = 0
    up, down, right, left = False, False, False, False

    def __init__(self, x: float, y: float):
        self.position = Vector2(x, y)
        # Player images rotated to look at "0 degrees"
        self.image = pygame.image.load("data/Player.png").convert_alpha()
        self.image_attack = pygame.image.load("data/PlayerAttack.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)
        self.image_attack = pygame.transform.rotate(self.image_attack, -90)
        # Target red rect
        self.image_target = pygame.Surface((32, 32))
        self.image_target.fill((240, 30, 30))
        self.image_target.set_alpha(50)
        # Items
        for i in range(0, 10):
            self.image_items.append(self.get_item_slot_image())
        self.image_items[0].blit(pygame.image.load("data/Sword.png").convert_alpha(), (0, 0))
        self.image_items[self.current_item].set_alpha(200)

    def game_action(self, player_action: GameActions, **kwargs):
        """

        :param player_action: PlayerAction enum
        :param kwargs: arguments for that specific action see PlayerAction
        :return: nothing
        """
        # for k, v in kwargs:
        print("PlayerAction (%s) inputs: " % player_action, kwargs)
        if player_action == GameActions.PLAYER_MOVE_UP:
            self.up = not self.up
        elif player_action == GameActions.PLAYER_MOVE_DOWN:
            self.down = not self.down
        elif player_action == GameActions.PLAYER_MOVE_LEFT:
            self.left = not self.left
        elif player_action == GameActions.PLAYER_MOVE_RIGHT:
            self.right = not self.right
        elif player_action == GameActions.PLAYER_USE:
            self.attacking = 200
        elif GameActions.PLAYER_ITEM_SELECT_0.value <= player_action.value <= GameActions.PLAYER_ITEM_SELECT_9.value:
            self.current_item = player_action.value - GameActions.PLAYER_ITEM_SELECT_0.value
            for i in self.image_items:
                i.set_alpha(50)
            self.image_items[self.current_item].set_alpha(200)
        else:
            print("Unknown PlayerAction!")

        new_direction = 0.0
        count = 0
        if self.right:
            if self.up:
                new_direction += 360
            count += 1
        if self.down:
            new_direction += 90
            count += 1
        if self.left:
            new_direction += 180
            count += 1
        if self.up:
            new_direction += 270
            count += 1

        if count > 0:
            self.direction_angle = new_direction / count
            if self.direction_angle > 180:
                self.direction_angle -= 360

            self.direction_vector = self.reference_vector.rotate(self.direction_angle)
            print("Dir: %.2f" % self.direction_angle)
            self.moving = True
        else:
            self.moving = False

    def get_image(self):
        return self.image

    def render(self, dt: int, screen: pygame.Surface):
        self.attacking -= dt
        if self.attacking > 0:
            current_image = self.image_attack
        else:
            self.attacking = 0
            current_image = self.image
        current_image = pygame.transform.rotate(current_image, -self.direction_angle)
        screen.blit(current_image, self.position)
        screen.blit(self.image_target, self.position + self.direction_vector * 32)
        position_x = 32
        position_y = screen.get_height() - 40
        for item in self.image_items:
            screen.blit(item, (position_x, position_y))
            position_x += 40

    @staticmethod
    def get_item_slot_image():
        slot_image = pygame.Surface((32, 32))
        slot_image.fill(color=(50, 50, 50))
        slot_image.fill(color=(94, 94, 94), rect=(1, 1, 30, 30))
        slot_image.set_alpha(50)
        return slot_image
