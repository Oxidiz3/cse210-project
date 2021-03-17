#from .actor import Actor
import arcade
import data.constants as constants

class Tower(arcade.Sprite):
    
    '''
    A tower sprite
    '''

    def __init__(self, tower_name: str='towerPlaceHolder'):
        
        towerPlaceHolder = {'health':1, 'attack_damage':0, 'cost':1, 'coordinates':None}
        villager = {'health':100, 'attack_damage':10, 'cost':10, 'coordinates':None}
        knight = {'health':200, 'attack_damage':20, 'cost':50, 'coordinates':None}

        towers = {'villager':villager, 'knight':knight, 'towerPlaceHolder':towerPlaceHolder}
        tower = towers[tower_name]

        try:
            super().__init__(f"{constants.ASSETS_PATH}/{tower_name}.png")
        except FileNotFoundError:
            super().__init__(constants.TOWER_IMAGE)
        self.health = tower['health']
        self.damage = tower['attack_damage']
        self.cost = tower['cost']
        self.coordinates = None #tower['coordinates']

    def set_coordinates(self, x, y):
        self.coordinates = (x,y)

#Tower()