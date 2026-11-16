from enum import Enum, auto


class GameState(Enum):
    """Три состояния игры."""
    RULES = auto()    # окно с правилами
    PLAYING = auto()  # игра идёт
    RESULT = auto()   # окно итогов