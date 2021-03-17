from actor import Actor
import arcade

class Tower(arcade.Sprite):
    
    '''
    Creates a tower sprite
    '''

    def __init__(self, tower='undefined_tower'):

        undefined_tower = {'health':0, 'attack_damage':0, 'cost':0, 'sprite':'towerPlaceHolder', 'coordinates':None}
        villager = {'health':100, 'attack_damage':10, 'cost':10, 'sprite':'villager', 'coordinates':None}
        knight = {'health':200, 'attack_damage':20, 'cost':50, 'sprite':'knight', 'coordinates':None}
        towers = {'villager':villager, 'knight':knight, 'undefined_tower':undefined_tower}

        super().__init__()
        self.health = towers[tower]['health']
        self.damage = towers[tower]['attack_damage']
        self.cost = towers[tower]['cost']
        self.coordinates = None #towers[tower]['coordinates']

    def set_coordinates(self, x, y):
        self.coordinates = (x,y)

Tower()