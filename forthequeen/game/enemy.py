# from .actor import Actor
import arcade
import random
import data.constants as constants



class Enemy(arcade.Sprite):
    """
    A enemy sprite
    """
    def __init__(self, enemy_name: str = 'enemyPlaceHolder'):


        center_x = random.randint(0, 5)
        center_y = 5

        # enemyPlaceHolder = {'health': 1, 'attack_damage': 0, 'cost': 1, 'coordinates': None}
        skeleton = {'health': 200, 'attack_damage': 20, 'coordinates': [center_x, center_y]}
        ghost = {'health': 100, 'attack_damage': 10, 'coordinates': [center_x, center_y]}
        slime = {'health': 50, 'attack_damage': 15, 'coordinates': [center_x, center_y]}

        enemies = {'skeleton': skeleton, 'ghost': ghost, 'slime': slime}
        enemy = enemies[enemy_name]

        try:
            super().__init__(filename=f"{constants.ASSETS_PATH}/{enemy_name}.png")
        except FileNotFoundError:
            super().__init__(filename=constants.ENEMY_IMAGE)
        
        self.health = enemy['health']
        self.damage = enemy['attack_damage']
        self.cost = 0
    
    def move(self):
        self.change_y = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.remove_from_sprite_lists()
