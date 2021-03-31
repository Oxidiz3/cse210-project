"""
If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

from .scene_manager import SceneManager
from .actor_manager import ActorManager
from .menu import Menu
from .tower_placer import TowerPlacer
from .tower import Tower
from .enemy import Enemy
from .projectile_manager import ProjectileManager
# from .add_enemy import AddEnemy
from data import constants


class Director(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)

        # Instantiate the two managers
        self.scene_manager = SceneManager()
        self.actor_manager = ActorManager()
        self.projectile_manager = ProjectileManager()
        self.tower_placer = TowerPlacer()
        self.menu = Menu()

        #self.add_enemy = AddEnemy()
        self.tower = 'villager'

        self.backgroundSong = arcade.Sound(file_name=constants.BACKGROUND_MUSIC, streaming=True)
        self.current_player = None
        self.music = None

        #self.start_time = time.time
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
        self.play_sound()

        # Create your sprites and sprite lists here
        main_level = arcade.Sprite(filename=constants.LEVEL_IMAGE)

        arcade.schedule(self.add_enemy, 1)

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

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.menu.on_update(self.tower_placer.score)
        self.enemy = 'slime'
        self.get_collisions()

    def get_collisions(self):
        enemy_projectiles = self.projectile_manager.enemyProjectiles
        friendly_projectiles = self.projectile_manager.friendlyProjectiles
        for bullet in enemy_projectiles:
            hit_list = arcade.check_for_collision_with_list(bullet, self.tower_placer.get_sprite_list()
                                                            )
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for tower in hit_list:
                _tower = self.tower_placer.tower_dict[tower.position[0], tower.position[1]]
                _tower.take_damage(bullet.damage)

        for projectile in friendly_projectiles:
            hit_list = arcade.check_for_collision_with_list(projectile, self.actor_manager.actors)

            if len(hit_list) > 0:
                projectile.remove_from_sprite_lists()

            for enemy in hit_list:
                _enemy = self.actor_manager
                enemy.take_damage(projectile.damage)



    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.ENTER:
            self.scene_manager.change_screen(0)
        elif key == arcade.key.KEY_1:
            self.tower = 'villager'
        elif key == arcade.key.KEY_2:
            self.tower = 'archer'
        elif key == arcade.key.KEY_3:
            self.tower = 'knight'

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(button)
        # left click
        if button == 1:
            self.tower_placer.place_tower(Tower(self.tower), x, y)
        elif button == 4:
            self.tower_placer.sell_tower(x, y)


    def add_enemy(self, delta_time=None, enemy_id:str='slime'):
        x = random.randint(365, 425)
        y = 170
        self.tower_placer.place_tower(Enemy(enemy_id), x, y, 'enemy')

