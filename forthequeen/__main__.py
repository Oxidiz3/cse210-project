# program entry point
from game.director import Director
import data.constants as constants
import arcade

def start_game():
    """ Main method """
    game = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    start_game()