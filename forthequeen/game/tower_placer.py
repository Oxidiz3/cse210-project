import forthequeen.data.constants as constants


class TowerPlacer:
    def __init__(self):
        self.num_rows = 5
        self.num_cols = 5
        self.tower_list = self.fill_list()  # tower_list[x,y]

    def fill_list(self):
        _list = []
        for x in range(self.num_cols):
            y_list = []
            for y in range(self.num_rows):
                y_list.append(0)
            _list.append(y_list)
            y_list.clear()

        return _list

    def place_tower(self, tower, x, y):
        _tile_size = constants.TILE_SIZE
        m_width = constants.SCREEN_WIDTH / 2
        m_height = constants.SCREEN_HEIGHT / 2

        print(x - (x % _tile_size), y - (y % _tile_size))

        # if x < m_width and y < m_width:
        #     if x > m_width and y >

        pass