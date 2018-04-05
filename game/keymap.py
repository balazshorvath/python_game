"""
Keymap
"""
import configparser

from .game_actions import GameActions

"""
    Config should be an .ini file.
    Every config should be inside the "DEFAULT" section.
    The keys should be the exact string representation of the enumerations in GameActions.
    The values should be the scan code of the desired key (I believe pygame events contain keyboard scan codes).
"""


class Keymap:
    controls = None

    def __init__(self, file: str):
        config = configparser.ConfigParser()
        config.read(file)
        config = config["DEFAULT"]
        self.controls = {int(v): k.upper() for k, v in config.items()}

    def map_key(self, key):
        action_string = self.controls.get(key)
        if action_string is not None:
            return GameActions[action_string]
        return None
