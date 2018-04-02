"""
Game objects
"""


class GameObject:
    def game_action(self, action, **kwargs):
        pass

    def get_direction(self):
        """
        Direction should be a vector (of type tuple) showing the speed of an object and is {unit/seconds}.
        :return:
        """
        pass
