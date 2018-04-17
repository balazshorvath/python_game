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



class Obstacle:
    position: tuple
    size: tuple
    image_transition_time: int
    collide: bool
    images = []
    __next_transition: int
    __current_image: int

    def __init__(self, **kwargs):
        self.position = kwargs.get("position", (0, 0))
        self.size = kwargs.get("size", (10, 10))
        self.images = kwargs.get("images")
        self.image_transition_time = kwargs.get("image_transition_time")
        self.collide = kwargs.get("collide")

    def update(self, dt):
        self.__next_transition -= dt
        if self.__next_transition <= 0:
            self.__current_image += 1
            if self.__current_image >= len(self.images):
                self.__current_image = 0

    def collides(self, obstacle):
        if not self.collide:
            return False

        if self.position[0] - obstacle.size[0] >= obstacle.position[0] <= self.position[0] + self.size[0] \
                and self.position[1] - obstacle.size[1] >= obstacle.position[1] <= self.position[1] + self.size[1]:
            # we collide on the x axis
            return True
