import pygame

from game.settings import WIDTH, HEIGHT


class Camera:
    """Камера, следующая за игроком."""

    def __init__(self, level_width, level_height):
        self.offset_x = 0
        self.offset_y = 0

        self.level_width = level_width
        self.level_height = level_height

    def update(self, target):
        """Обновляет положение камеры относительно игрока."""

        self.offset_x = target.rect.centerx - WIDTH // 2
        self.offset_y = target.rect.centery - HEIGHT // 2

        self.offset_x = max(
            0,
            min(self.offset_x, self.level_width - WIDTH)
        )
        self.offset_y = max(
            0,
            min(self.offset_y, self.level_height - HEIGHT)
        )

    def apply(self, sprite):
        """Возвращает экранные координаты объекта, не меняя его позицию."""

        return sprite.rect.move(-self.offset_x, -self.offset_y)

