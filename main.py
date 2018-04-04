import configparser

from game.game import Game

config = configparser.ConfigParser()
config.read("config/game.ini")
default = config['Default']

game = Game(windows_size=(default["screen_width"], default["screen_height"]))

game.game_loop()
