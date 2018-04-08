"""
GameObjects:
    Item
    GameObject
"""
from pygame import Surface
from pygame.math import Vector2

from game.game import Game


class GameObject:
    reference_vector: Vector2 = Vector2(1.0, 0.0)

    index_id: int

    position: Vector2
    direction_angle: float = 0.0
    direction_vector: Vector2 = reference_vector
    moving: bool = False

    image: Surface = None

    def __init__(self, index_id: int, x: float, y: float):
        self.index_id = index_id
        self.position = Vector2(x, y)

    def render(self, dt: int, screen: Surface):
        pass

    def update(self, dt: int):
        pass


class Item(GameObject):
    icon: Surface = None

    def use(self, game: Game, user: GameObject):
        pass
