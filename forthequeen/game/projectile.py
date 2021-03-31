import arcade
import data.constants as constants
from game.actor import Actor

class Projectile(arcade.Sprite):
    def __init__(self, direction, enemy):
        self.direction = direction
        self.enemy = enemy
        self.change_y = self.direction
        self.damage = 15

        super().__init__(filename=constants.PROJECTILE_IMAGE)