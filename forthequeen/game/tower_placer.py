import data.constants as constants
import arcade


class TowerPlacer:
    def __init__(self):
        self.num_rows = 7
        self.num_cols = 5
        self.score = 50
        self.tower_dict = self.fill_dict()

    def fill_dict(self):
        """
        initialize the dict and fill it with empty items at proper coordinates
        :return dict: tower_dict
        """
        _dict = {}
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                _dict[(x, y)] = 0

        return _dict

    def get_sprite_list(self):
        """
        :return: _sprite_list
        """
        _sprite_list = arcade.sprite_list.SpriteList()
        for value in self.tower_dict.values():
            if value != 0:
                _sprite_list.append(value)
        return _sprite_list

    def get_relative_position(self, x, y):
        """
            Returns the coordinate of our tower grid
        :param x: mouse_x coordinate
        :param y: mouse_y coordinate
        :return: relative_x, relative_y
        """
        _tile_size = constants.TILE_SIZE
        m_width = constants.SCREEN_WIDTH / 2
        m_height = constants.SCREEN_HEIGHT / 2

        # how many pixels the screen is off from center
        x_image_deviance = 44
        y_image_deviance = 36

        # This breaks our x and y into a grid
        x_grid = x - ((x - 4) % _tile_size) + x_image_deviance
        y_grid = y - ((y + 8) % _tile_size) + y_image_deviance

        # get x and y relative to top right corner and with our tile size in mind
        x_rel = (x_grid - m_width) / _tile_size
        y_rel = -1 * (y_grid - m_height) / _tile_size

        x_rel = int(x_rel)
        y_rel = int(y_rel)

        return x_rel, y_rel

    def get_image_pos(self, x, y):
        """
            get where the image should be with given x,y
        :param x: mouse_x
        :param y: mouse_y
        :return x_image_pos, y_image_pos:
        """
        _tile_size = constants.TILE_SIZE

        # This breaks our x and y into a grid
        x_grid = x - ((x - 6) % _tile_size)
        y_grid = y - ((y + 8) % _tile_size)

        x_image_pos = x_grid + _tile_size / 2
        y_image_pos = y_grid + _tile_size / 2 - 4
        return x_image_pos, y_image_pos

    def get_score(self):
        """ :return: self.score """
        return self.score

    def place_tower(self, tower, x, y):
        """
        places tower into the dictionary
        :param tower: tower class
        :param x: x coord of mouse
        :param y: y coord of mouse
        """
        x_rel, y_rel = self.get_relative_position(x, y)
        x_image_pos, y_image_pos = self.get_image_pos(x, y)
        tower.set_position(x_image_pos, y_image_pos)

        if 0 <= x_rel < self.num_cols:
            if 0 <= y_rel < self.num_rows:
                # If there isn't a tower then add a tower
                if self.tower_dict[x_rel, y_rel] == 0:
                    if self.score >= tower.cost:
                        self.score -= tower.cost
                        # Add tower to dict
                        self.tower_dict[x_rel, y_rel] = tower
                        print("Tower added at: ", x_rel, y_rel)
                    else:
                        print("you have no more score to spend")

    def sell_tower(self, x, y):
        """
        sells tower and returns cost to self.score
        :param x: mouse x
        :param y:  mouse y
        """
        x_rel, y_rel = self.get_relative_position(x, y)

        if self.tower_dict[x_rel, y_rel] != 0:
            cost = self.tower_dict[x_rel, y_rel].cost
        else:
            cost = 0 

        if 0 <= x_rel < self.num_cols:
            if 0 <= y_rel < self.num_rows:
                if self.tower_dict[(x_rel, y_rel)] != 0:
                    self.score += cost
                    self.tower_dict[(x_rel, y_rel)] = 0

        print(self.score)