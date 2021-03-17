"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from .scene_manager import SceneManager
from .actor_manager import ActorManager
from .menu import Menu
from .tower_placer import TowerPlacer
from .tower import Tower
import data.constants as constants


class Director(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        # Instantiate the two managers
        self.scene_manager = SceneManager()
        self.actor_manager = ActorManager()
        self.tower_placer = TowerPlacer()
        self.menu = Menu()

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.menu.setup()

        # Create your sprites and sprite lists here
        main_level = arcade.Sprite(filename=constants.LEVEL_IMAGE)

        # add the level and center it
        # Make sure this is always first VVV
        main_level.position = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
        self.scene_manager.current_scene.append(main_level)
        # Add scenes here VVV

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.scene_manager.current_scene.draw()
        self.actor_manager.actors.draw()
        self.tower_placer.get_sprite_list().draw()
        self.menu.draw()
        self.tower_placer.tower_dict


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.ENTER:
            self.scene_manager.change_screen(0)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(button)
        # left click
        if button == 1:
            tower = Tower('villager')
            self.tower_placer.place_tower(tower, x, y)
        # right click
        elif button == 4:
            self.tower_placer.sell_tower(x, y)
        pass