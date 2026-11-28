import pygame

from game.settings import PROJECTILE_SPEED


class Projectile(pygame.sprite.Sprite):
    """Золотой магический снаряд."""

    def __init__(self, x, y, direction):
        super().__init__()

        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

        self.direction = direction
        self.speed = PROJECTILE_SPEED * direction
        self.animation_frame = 0

        self.draw()

    def draw(self):
        """Отрисовка золотого шара с магическим шлейфом."""
        self.image.fill((0, 0, 0, 0))

        frame = self.animation_frame % 2

        # Частицы позади шара
        trail_x = 25 if self.direction > 0 else 7

        pygame.draw.rect(
            self.image, (190, 110, 20),
            (trail_x, 14 + frame, 4, 4)
        )
        pygame.draw.rect(
            self.image, (255, 190, 55),
            (trail_x + (2 if self.direction < 0 else -2), 9, 3, 3)
        )

        # Золотое свечение
        pygame.draw.circle(
            self.image, (255, 180, 35, 90), (16, 16), 13
        )

        # Основной шар
        pygame.draw.circle(
            self.image, (190, 105, 20), (16, 16), 10
        )
        pygame.draw.circle(
            self.image, (255, 190, 55), (16, 16), 8
        )
        pygame.draw.circle(
            self.image, (255, 235, 155), (16, 16), 5
        )

        # Яркое магическое ядро
        pygame.draw.rect(
            self.image, (255, 255, 225), (13, 13, 6, 6)
        )

        # Маленькие искры
        pygame.draw.rect(
            self.image, (255, 220, 100), (5, 5 + frame, 3, 3)
        )

    def update(self, platforms, enemies):
        self.rect.x += self.speed
        self.animation_frame += 1
        self.draw()

        if pygame.sprite.spritecollideany(self, platforms):
            self.kill()
            return

        hit_enemies = pygame.sprite.spritecollide(
            self, enemies, False
        )

        if hit_enemies:
            hit_enemies[0].take_hit()
            self.kill()