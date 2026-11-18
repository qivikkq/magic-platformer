import pygame

from game.settings import (
    PLAYER_SIZE, PLAYER_COLOR, PLAYER_SPEED,
    GRAVITY, JUMP_SPEED, MAX_FALL_SPEED, FALL_LIMIT,
)


class Player(pygame.sprite.Sprite):
    """Героиня: движение, гравитация, прыжок, столкновения с платформами."""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.start_pos = (x, y)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.facing = "right"   # куда смотрит: "right" или "left"

    def shoot(self):
        """Заготовка. Заполнит Настя."""
        pass

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -PLAYER_SPEED
            self.facing = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = PLAYER_SPEED
            self.facing = "right"

    def update(self, platforms):
        self.handle_input()
        self.rect.x += self.vel_x