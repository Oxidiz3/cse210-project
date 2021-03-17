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
PADDLE_IMAGE = DIRROOT.joinpath("images/paddle-0.png")
BRICK_IMAGE = DIRROOT.joinpath("images/brick-0.png")