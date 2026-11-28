import pygame

from game.settings import PROJECTILE_SPEED


class Projectile(pygame.sprite.Sprite):
    """Золотой магический снаряд."""

    def __init__(self, x, y, direction):
        super().__init__()

        self.direction = direction
        self.speed = PROJECTILE_SPEED * direction
        self.animation_frame = 0

        # Создаём два кадра анимации заранее
        self.frames = [
            self._render(0),
            self._render(1)
        ]

        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    def _render(self, frame):
        """Создаёт кадр золотого шара с магическим шлейфом."""
        image = pygame.Surface((32, 32), pygame.SRCALPHA)

        # Частицы позади шара
        trail_x = 7 if self.direction > 0 else 25

        pygame.draw.rect(
            image, (190, 110, 20),
            (trail_x, 14 + frame, 4, 4)
        )
        pygame.draw.rect(
            image, (255, 190, 55),
            (trail_x + (2 if self.direction < 0 else -2), 9, 3, 3)
        )

        # Золотое свечение
        pygame.draw.circle(
            image, (255, 180, 35, 90), (16, 16), 13
        )

        # Основной шар
        pygame.draw.circle(
            image, (190, 105, 20), (16, 16), 10
        )
        pygame.draw.circle(
            image, (255, 190, 55), (16, 16), 8
        )
        pygame.draw.circle(
            image, (255, 235, 155), (16, 16), 5
        )

        # Яркое магическое ядро
        pygame.draw.rect(
            image, (255, 255, 225), (13, 13, 6, 6)
        )

        # Маленькие искры
        pygame.draw.rect(
            image, (255, 220, 100), (5, 5 + frame, 3, 3)
        )

        return image

    def update(self):
        """Движение и анимация снаряда."""
        self.rect.x += self.speed

        self.animation_frame += 1
        self.image = self.frames[(self.animation_frame // 5) % 2]