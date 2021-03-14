import forthequeen.data.constants as constants
import arcade


class TowerPlacer:
    def __init__(self):
        self.num_rows = 7
        self.num_cols = 5
        # self.tower_list = self.fill_list()  # tower_list[x[y]]
        self.tower_dict = self.fill_dict()

    def fill_dict(self):
        _dict = {}
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                _dict[(x, y)] = 0

        return _dict

    def get_sprite_list(self):
        _sprite_list = arcade.sprite_list.SpriteList()
        for value in self.tower_dict.values():
            if value != 0:
                _sprite_list.append(value)
        return _sprite_list

    def place_tower(self, tower: arcade.sprite.Sprite, x, y):
        _tile_size = constants.TILE_SIZE
        m_width = constants.SCREEN_WIDTH / 2
        m_height = constants.SCREEN_HEIGHT / 2

        # how many pixels the screen is off from center
        x_image_deviance = 48
        y_image_deviance = 36

        # This breaks our x and y into a grid
        x_grid = x - ((x - 4) % _tile_size) + x_image_deviance
        y_grid = y - ((y + 8) % _tile_size) + y_image_deviance

        x_image_pos = x_grid - x_image_deviance + _tile_size / 2
        y_image_pos = y_grid - y_image_deviance + _tile_size / 2 - 4

        tower.set_position(x_image_pos, y_image_pos)

        # get x and y relative to top right corner and with our tile size in mind
        x_rel = (x_grid - m_width) / _tile_size
        y_rel = -1 * (y_grid - m_height) / _tile_size

        x_rel = int(x_rel)
        y_rel = int(y_rel)

        if 0 <= x_rel < self.num_cols:
            if 0 <= y_rel < self.num_rows:
                # If there isn't a tower then add a tower
                if self.tower_dict[x_rel, y_rel] == 0:
                    # Add tower to dict
                    self.tower_dict[x_rel, y_rel] = tower
                    print("Tower added at: ", x_rel, y_rel)
                else:
                    print(x_rel, x_grid)

    def add_tower(self, tower, x: int, y: int):
        for key, values in self.tower_dict:
            print(key, values)
        print(self.tower_dict[x, y])
        self.tower_dict[x, y] = tower