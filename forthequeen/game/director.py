"""
If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from .scene_manager import SceneManager
from .actor_manager import ActorManager
from .menu import Menu
from .start_menu import StartMenu
from .tower_placer import TowerPlacer
from .tower import Tower
from data import constants


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
        self.start_menu = StartMenu()

        self.backgroundSong = arcade.Sound(file_name=constants.BACKGROUND_MUSIC, streaming=True)
        self.current_player = None
        self.music = None

        # If you have sprite lists, you should create them here,
        # and set them to None

    def play_sound(self):
        if self.music:
            self.music.stop(self.current_player)

        self.music = self.backgroundSong
        self.current_player = self.music.play(loop=True)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.menu.setup()
        self.start_menu.setup()
        self.play_sound()

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
        #self.start_menu.draw()

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
            tower = Tower('archer')
            self.tower_placer.place_tower(tower, x, y)
        elif button == 4:
            self.tower_placer.sell_tower(x, y)
