from pathlib import Path
from game.enemy import Enemy

DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "For the Queen"

# Images
TILE_SIZE = 16
LEVEL_IMAGE = DIRROOT.joinpath("assets/levelMap.png")
TOWER_IMAGE = DIRROOT.joinpath("assets/towerPlaceHolder.png")
ASSETS_PATH = DIRROOT.joinpath('assets')

# Sounds
BACKGROUND_MUSIC = DIRROOT.joinpath("assets/HeroicDemise.wav")

# Enemies
SKELETON = Enemy(100, 25, filename="")
BAT = Enemy(50, 15, filename="")
SLIME = Enemy(25, 15, filename="")
