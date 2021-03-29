from pathlib import Path

DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "For the Queen"

TILE_SIZE = 16
LEVEL_IMAGE = DIRROOT.joinpath("assets/levelMap.png")
TOWER_IMAGE = DIRROOT.joinpath("assets/towerPlaceHolder.png")
ASSETS_PATH = DIRROOT.joinpath('assets')
ENEMY_IMAGE = DIRROOT.joinpath("assets/towerPlaceHolder.png")


# VILLAGER_TOWER = Tower(100, 200, "imagepath")