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

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.menu_background = arcade.load_texture(f"{constants.ASSETS_PATH}/menu_background.png")
        self.tower_background = arcade.load_texture(f"{constants.ASSETS_PATH}/tower_background.png")
        self.villager = arcade.load_texture(f"{constants.ASSETS_PATH}/villager.png")
        self.archer = arcade.load_texture(f"{constants.ASSETS_PATH}/archer.png")
        self.knight = arcade.load_texture(f"{constants.ASSETS_PATH}/knight.png")
        self.score = 0

    def draw(self):
        """
        Render the screen.
        """

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, constants.SCREEN_HEIGHT - 140,
                                            500, 140,
                                            self.menu_background)

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 500, arcade.color.WHITE, 18)


        '''draw villager tower'''
        # Draw background for towers in menu
        arcade.draw_lrwh_rectangle_textured(120, constants.SCREEN_HEIGHT - 130,
                                            90, 120,
                                            self.tower_background)

        # Draw tower for build menu
        arcade.draw_lrwh_rectangle_textured(135, constants.SCREEN_HEIGHT - 65,
                                            60, 50,
                                            self.villager)

        # Render name for tower
        arcade.draw_text("Villager", 140, constants.SCREEN_HEIGHT - 90, arcade.color.WHITE, 16)

        # Render price for tower
        arcade.draw_text("10", 155, constants.SCREEN_HEIGHT - 110, arcade.color.WHITE, 16)

        # Render button to press for tower
        arcade.draw_text("Press 1", 140, constants.SCREEN_HEIGHT - 130, arcade.color.WHITE, 16)


        '''draw archer tower'''
        # Draw background for towers in menu
        arcade.draw_lrwh_rectangle_textured(250, constants.SCREEN_HEIGHT - 130,
                                            90, 120,
                                            self.tower_background)

        # Draw tower for build menu
        arcade.draw_lrwh_rectangle_textured(265, constants.SCREEN_HEIGHT - 65,
                                            60, 50,
                                            self.archer)

        # Render name for tower
        arcade.draw_text("Archer", 270, constants.SCREEN_HEIGHT - 90, arcade.color.WHITE, 16)

        # Render price for tower
        arcade.draw_text("15", 285, constants.SCREEN_HEIGHT - 110, arcade.color.WHITE, 16)

        # Render button to press for tower
        arcade.draw_text("Press 2", 270, constants.SCREEN_HEIGHT - 130, arcade.color.WHITE, 16)



        '''draw knight tower'''
        # Draw background for towers in menu
        arcade.draw_lrwh_rectangle_textured(380, constants.SCREEN_HEIGHT - 130,
                                            90, 120,
                                            self.tower_background)

        # Draw tower for build menu
        arcade.draw_lrwh_rectangle_textured(395, constants.SCREEN_HEIGHT - 65,
                                            60, 50,
                                            self.knight)

        # Render name for tower
        arcade.draw_text("Knight", 400, constants.SCREEN_HEIGHT - 90, arcade.color.WHITE, 16)

        # Render price for tower
        arcade.draw_text("20", 415, constants.SCREEN_HEIGHT - 110, arcade.color.WHITE, 16)

        # Render button to press for tower
        arcade.draw_text("Press 3", 400, constants.SCREEN_HEIGHT - 130, arcade.color.WHITE, 16)


    def on_update(self, score):
        #update score
        self.score = score
