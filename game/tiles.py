from typing import Any

import pygame

from game.settings import TILE_SIZE

class Platform(pygame.sprite.Sprite):
    """Платформа уровня"""

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((120, 120, 120))

        self.rect = self.image.get_rect(topleft = (x, y))
