import arcade
from data import constants
from game.projectile import Projectile

class ProjectileManager(arcade.Sprite):
    def __init__(self):
        self.friendlyProjectiles = arcade.SpriteList()
        self.enemyProjectiles = arcade.SpriteList()

        super().__init__(filename=constants.PROJECTILE_IMAGE)

    def createBullet(self, x, y, direction, enemy: bool):
        new_projectile = Projectile(direction, enemy)
        new_projectile.position = (x, y)

        if enemy:
            self.enemyProjectiles.append(new_projectile)
        else:
            self.friendlyProjectiles.append(new_projectile)


