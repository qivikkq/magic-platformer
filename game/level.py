import os

import pygame

from game.settings import TILE_SIZE
from game.tiles import Platform

ALLOWED_CHARS = {"#", "P", "E", "M", "."}

class Level:
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.width = 0
        self.height = 0
        self.player_start = (0, 0)
        self.enemy_spawns = []
        self.mushroom_spawns = []

    @classmethod
    def load(cls, path):
        if not os.path.exists(path):
            raise ValueError(f"Файл карты не найден: {path}")

        with open(path, "r", encoding="utf-8") as f:
            raw_lines = [line.rstrip("\n") for line in f if line.strip() != ""]

        if not raw_lines:
            raise ValueError("Карта пуста.")

        lengths = {len(line) for line in raw_lines}
        if len(lengths) != 1:
            raise ValueError(
                f"Все строки карты должны быть одной длины. Найдено: {sorted(lengths)}"
            )

        bad_chars = set()
        for line in raw_lines:
            bad_chars |= set(line) - ALLOWED_CHARS
        if bad_chars:
            raise ValueError(
                f"В карте встречены недопустимые символы: {sorted(bad_chars)}. "
                f"Разрешены только: {sorted(ALLOWED_CHARS)}"
            )

        level = cls()
        level.height = len(raw_lines)
        level.width = lengths.pop()

        players = 0
        for row_idx, line in enumerate(raw_lines):
            for col_idx, ch in enumerate(line):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                if ch == "#":
                    level.platforms.add(Platform(x, y))
                elif ch == "P":
                    players += 1
                    level.player_start = (x, y)
                elif ch == "E":
                    level.enemy_spawns.append((x, y))
                elif ch == "M":
                    level.mushroom_spawns.append((x, y))

        if players != 1:
            raise ValueError(
                f"На карте должна быть ровно одна стартовая точка P. Найдено: {players}"
            )
        if not level.enemy_spawns:
            raise ValueError("На карте должен быть хотя бы один враг E.")

        return level

    def draw(self, screen):
        self.platforms.draw(screen)