from game.actor import Actor


class Enemy(Actor):
    def __init__(self, health, attack_damage, filename):
        super().__init__(health, attack_damage, filename=filename)

        self.center_x = 100
        self.center_y = 10

    def _move(self):
        self.center_y += 1
