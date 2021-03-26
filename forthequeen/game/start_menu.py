import data.constants as constants
import arcade

class StartMenu:
    def setup(self):
        # Get image for start menu 
        self.start_menu =  arcade.load_texture(f"{constants.ASSETS_PATH}/start_menu.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.start_menu)
