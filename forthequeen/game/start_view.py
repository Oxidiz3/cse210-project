from .director import Director
import data.constants as constants
import arcade

class StartView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture(f"{constants.ASSETS_PATH}/start_menu.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_key_press(self, key, key_modifiers):
        """ If the user presses the space bar, re-start the game. """
        game_view = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        game_view.setup()
        self.window.show_view(game_view)