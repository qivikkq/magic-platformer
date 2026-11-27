import pygame

from game.settings import TILE_SIZE, UI_BORDER_COLOR

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(UI_BORDER_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))