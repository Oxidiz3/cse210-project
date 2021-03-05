import arcade


class SceneManager:
    def __init__(self):
        self.current_scene = arcade.SpriteList()
        self.scenes = []
        self.scene_number = 0
        # 0: main scene, 1: game scene, 2: game over scene

    def add_scene(self, scene):
        self.scenes.append(scene)

    def change_screen(self, screen_number):
        self.scene_number = screen_number
        try:
            self.current_scene = self.scenes[screen_number]
            print("Screen changed to", self.scene_number)
        except IndexError:
            print(f"Scene number: {self.scene_number} doesn't exist try again")