import arcade
import arcade.gui
from arcade.gui import UIManager


class MyFlatButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """

    def on_click(self):
        """ Called when user lets off button """
        print("Click flat button. ")


class Menu(arcade.View):

    """
    Main view. Really the only view in this example."""

    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4

        start_button = MyFlatButton(
            "Start Playing",
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(start_button)

        quit_button = MyFlatButton(
            "Quit",
            center_x=self.window.width // 2,
            center_y=y_slot * 1,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(quit_button)