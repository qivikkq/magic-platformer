import pygame

from game.settings import WIDTH, HEIGHT, WHITE
from game.ui.popup import Popup

class ResultPopup(Popup):
    def __init__(self, stats):
        kills = stats.kills
        mushrooms = stats.mushrooms
        seconds = int(stats.elapsed_seconds())

        lines = [
            f"Врагов убито: {kills}",
            f"Грибов собрано: {mushrooms}",
            f"Время: {seconds} c",
        ]
        super().__init__("Результат", lines, "Выход")