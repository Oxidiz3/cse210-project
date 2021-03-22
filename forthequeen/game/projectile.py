import arcade
import data.constants as constants


class Projectile(arcade.Sprite):
    def __init__(self, attack_damage, coordinates):
        super().__init__(attack_damage)
#Still need to work on passing the tower coordinates to the projectile
        self.center_x = x
        self.center_y = y
#Looking into a method within arcade which could make movement easier
    def update(self):
        #Call this to update movement
        self.center_y -= 1