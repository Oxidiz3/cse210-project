# from .actor import Actor
import arcade
import data.constants as constants
from .projectile import Projectile

class Tower(arcade.Sprite):
    """
    A tower sprite
    """

    def __init__(self, tower_name: str = 'towerPlaceHolder'):

        # towerPlaceHolder = {'health': 1, 'attack_damage': 0, 'cost': 1, 'coordinates': None}
        villager = {'health': 100, 'attack_damage': 10, 'cost': 10, 'coordinates': None}
        knight = {'health': 200, 'attack_damage': 20, 'cost': 20, 'coordinates': None}
        archer = {'health': 50, 'attack_damage': 15, 'cost': 15}

        towers = {'villager': villager, 'knight': knight, 'archer': archer}
        tower = towers[tower_name]

        try:
            super().__init__(filename=f"{constants.ASSETS_PATH}/{tower_name}.png")
        except FileNotFoundError:
            super().__init__(filename=constants.TOWER_IMAGE)
        self.health = tower['health']
        self.damage = tower['attack_damage']
        self.cost = tower['cost']

        # already implemented in the sprites class
        # self.coordinates = None #tower['coordinates']
    # def set_coordinates(self, x, y):
    #     self.coordinates = (x,y)

    def attack(self):
        #call this to initiate an attack
        return Projectile(-10, self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.remove_from_sprite_lists()
