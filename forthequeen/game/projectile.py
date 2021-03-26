from game.actor import Actor


class Projectile(Actor):
    def __init__(self, health, attack_damage, filename):
        super().__init__(health, attack_damage, filename=filename)

        self.center_x = 100
        self.center_y = 10

    def update(self):
        self.center_y -= 1