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
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.jump()

    def jump(self):
        self.vel_y = JUMP_SPEED
        self.on_ground = False

    def move_and_collide(self, platforms):
        # 1. Двигаем по X и разбираемся со стенами
        self.rect.x += self.vel_x
        for platform in pygame.sprite.spritecollide(self, platforms, False):
            if self.vel_x > 0:
                self.rect.right = platform.rect.left
            elif self.vel_x < 0:
                self.rect.left = platform.rect.right

        # 2. Гравитация и движение по Y
        self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL_SPEED)
        self.rect.y += self.vel_y
        self.on_ground = False
        for platform in pygame.sprite.spritecollide(self, platforms, False):
            if self.vel_y > 0:            # падаем на платформу
                self.rect.bottom = platform.rect.top
                self.on_ground = True
            elif self.vel_y < 0:          # ударились головой
                self.rect.top = platform.rect.bottom
            self.vel_y = 0

    def respawn(self):
        self.rect.topleft = self.start_pos
        self.vel_x = 0
        self.vel_y = 0

    def update(self, platforms):
        self.handle_input()
        self.move_and_collide(platforms)
        if self.rect.top > FALL_LIMIT:
            self.respawn()