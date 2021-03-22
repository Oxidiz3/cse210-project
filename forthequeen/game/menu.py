import random
import arcade
import os
import data.constants as constants
from game.tower_placer import TowerPlacer

class Menu:
    """
    Create the build menu for towers.
    """

    def setup(self):
        """ Initializer """

        self.tower_placer = TowerPlacer()
        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.menu_background = arcade.load_texture(f"{constants.ASSETS_PATH}/menu_background.png")
        self.tower_background = arcade.load_texture(f"{constants.ASSETS_PATH}/tower_background.png")
        self.first_tower = arcade.load_texture(f"{constants.ASSETS_PATH}/villager.png")

    def draw(self):
        """
        Render the screen.
        """

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, constants.SCREEN_HEIGHT - 120,
                                            500, 120,
                                            self.menu_background)

        # Render the text
        arcade.draw_text(f"Score: {self.tower_placer.score}", 10, 500, arcade.color.WHITE, 18)

        # Draw background for towers in menu
        arcade.draw_lrwh_rectangle_textured(120, constants.SCREEN_HEIGHT - 110,
                                            90, 100,
                                            self.tower_background)

        # Draw tower for build menu
        arcade.draw_lrwh_rectangle_textured(135, constants.SCREEN_HEIGHT - 65,
                                            60, 50,
                                            self.first_tower)

        # Render name for tower
        arcade.draw_text("Tower", 140, constants.SCREEN_HEIGHT - 90, arcade.color.WHITE, 16)

        # Render price for tower
        arcade.draw_text("100", 150, constants.SCREEN_HEIGHT - 110, arcade.color.WHITE, 16)