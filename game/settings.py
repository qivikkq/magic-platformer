from pathlib import Path

# Окно и частота кадров
WIDTH = 960
HEIGHT = 540
FPS = 60
TITLE = "Magic Platformer"

# Размер одной клетки уровня (в пикселях)
TILE_SIZE = 40

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (20, 40, 45)

# Цвета интерфейса
UI_TEXT_COLOR = (240, 240, 230)
UI_PANEL_COLOR = (35, 35, 55)
UI_BORDER_COLOR = (115, 95, 155)
UI_BUTTON_COLOR = (75, 60, 110)
UI_BUTTON_HOVER_COLOR = (105, 80, 150)
UI_SHADOW_COLOR = (10, 10, 20)

# Пути к шрифтам
BASE_DIR = Path(__file__).resolve().parent.parent
FONT_DIR = BASE_DIR / "assets" / "fonts"

TITLE_FONT_PATH = FONT_DIR / "PressStart2P-Regular.ttf"
TEXT_FONT_PATH = FONT_DIR / "EpilepsySans.ttf"

#Размеры шрифтов
TITLE_FONT_SIZE = 30
TEXT_FONT_SIZE = 28
BUTTON_FONT_SIZE = 22

# Игрок
PLAYER_SIZE = (30, 50)
PLAYER_COLOR = (180, 120, 255)
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_SPEED = -16
MAX_FALL_SPEED = 16
FALL_LIMIT = HEIGHT + 200   # ниже этой линии героиня возрождается