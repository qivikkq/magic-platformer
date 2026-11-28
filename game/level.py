from pathlib import Path

import pygame

from game.settings import TILE_SIZE, ENEMY_SIZE
from game.tiles import Platform
from game.enemy import Enemy, StrongEnemy


class Level:
    """Загрузка карты и создание объектов уровня."""

    ALLOWED_SYMBOLS = {"#", ".", "P", "E", "S"}

    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_start = None
        self.width = 0
        self.height = 0

    def load(self, path):
        """Загружает карту из текстового файла."""

        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(f"Файл уровня не найден: {path}")

        rows = [
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        if not rows:
            raise ValueError("Карта уровня пустая")

        self.width = len(rows[0])
        self.height = len(rows)

        if any(len(row) != self.width for row in rows):
            raise ValueError("Все строки карты должны иметь одинаковую длину")

        unknown_symbols = {
            symbol
            for row in rows
            for symbol in row
            if symbol not in self.ALLOWED_SYMBOLS
        }

        if unknown_symbols:
            raise ValueError(
                f"Неизвестные символы на карте: {unknown_symbols}"
            )

        player_positions = [
            (column, row)
            for row, line in enumerate(rows)
            for column, symbol in enumerate(line)
            if symbol == "P"
        ]

        if len(player_positions) != 1:
            raise ValueError("На карте должна быть ровно одна точка появления игрока")

        self.platforms.empty()
        self.enemies.empty()

        for row, line in enumerate(rows):
            for column, symbol in enumerate(line):
                x = column * TILE_SIZE
                y = row * TILE_SIZE

                if symbol == "#":
                    self.platforms.add(Platform(x, y))

                elif symbol == "E":
                    enemy_y = y + TILE_SIZE - ENEMY_SIZE[1]
                    self.enemies.add(Enemy(x, enemy_y))

                elif symbol == "S":
                    enemy_y = y + TILE_SIZE - ENEMY_SIZE[1]
                    self.enemies.add(StrongEnemy(x, enemy_y))

        column, row = player_positions[0]
        self.player_start = (
            column * TILE_SIZE,
            row * TILE_SIZE
        )