from game.actor import Actor
from arcade.sprite import Sprite


class Enemy(Actor):
    def __init__(self, health, attack_damage):
        super().__init__(health, attack_damage)

        self.center_x = 100
        self.center_y = 10

    def update(self):
        self.center_y += 1


# Tower class
# class Tower(Sprite):
#     def __init__(self, health, damage, cost):
#         super().__init__()
#         self.health = 0
#         self.damage = 0
#         self.cost = 0