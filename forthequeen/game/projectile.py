import arcade
import data.constants as constants

class Projectile(arcade.Sprite):
    def __init__(self, attack_damage, coordinates):
        super().__init__(attack_damage)
#Still need to work on passing the tower coordinates to the projectile
        self.center_x = x
        self.center_y = y
#Looking into a method within arcade which could make movement easier
from game.actor import Actor


class Projectile(Actor):
    def __init__(self, health, attack_damage, filename):
        super().__init__(health, attack_damage, filename=filename)

        self.center_x = 100
        self.center_y = 10

    