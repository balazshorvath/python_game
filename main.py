import configparser

from game.game import Game

config = configparser.ConfigParser()
config.read("config/game.ini")
game = Game(config)

game.game_loop()
