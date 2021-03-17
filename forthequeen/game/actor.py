from abc import ABC, abstractmethod
import arcade


class Actor(ABC, arcade.Sprite):
    def __init__(self, health, attack_damage):
        super().__init__()
        self._health = health
        self._attack_damage = attack_damage

    def set_health(self, health):
        self._health = health

    def get_health(self):
        return self._health

    def set_attack_damage(self, attack_damage):
        self._attack_damage = attack_damage

    def get_attack_damage(self):
        return self._attack_damage