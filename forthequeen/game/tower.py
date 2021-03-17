#from .actor import Actor
import arcade
import data.constants as constants

class Tower(arcade.Sprite):
    
    '''
    A tower sprite
    '''

    def __init__(self, tower_name: str='towerPlaceHolder'):
        assets_path = constants.ASSETS_PATH
        towerPlaceHolder = {'health':1, 'attack_damage':0, 'cost':1, 'coordinates':None}
        villager = {'health':100, 'attack_damage':10, 'cost':10, 'coordinates':None}
        knight = {'health':200, 'attack_damage':20, 'cost':50, 'coordinates':None}

        towers = {'villager':villager, 'knight':knight, 'towerPlaceHolder':towerPlaceHolder}
        tower = towers[tower_name]

        super().__init__(f"{assets_path}/{tower_name}.png")
        self.health = tower['health']
        self.damage = tower['attack_damage']
        self.cost = tower['cost']
        self.coordinates = None #tower['coordinates']

    def set_coordinates(self, x, y):
        self.coordinates = (x,y)

#Tower()