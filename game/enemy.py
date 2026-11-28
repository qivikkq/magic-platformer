import pygame

from game.settings import (ENEMY_SIZE, ENEMY_COLOR, ENEMY_SPEED, ENEMY_HP,
                           STRONG_ENEMY_COLOR, STRONG_ENEMY_HP, STRONG_ENEMY_SPEED)

class Enemy(pygame.sprite.Sprite):
    """Обычный враг: ходит по платформе туда-сюда, гибнет от одного попадания"""

    def __init__(self, x, y, hp=ENEMY_HP, speed=ENEMY_SPEED, color=ENEMY_COLOR):
        super().__init__()

        self.image = pygame.Surface(ENEMY_SIZE)
        self.image.fill(color)

        self.rect = self.image.get_rect(topleft=(x, y))

        self.hp = hp
        self.speed = speed
        self.direction = 1


    def take_hit(self, damage=1):
        """Получить удар. Возвращает True, если враг погиб"""

        self.hp -= damage

        if self.hp <= 0:
            self.kill()
            return True

        return False


    def _has_ground(self, rect, platforms):
        """Проверка: есть ли платформа под передним краем врага"""

        x = rect.right - 1 if self.direction > 0 else rect.left
        probe = pygame.Rect(x, rect.bottom, 1, 1)
        return any(p.rect.colliderect(probe) for p in platforms)


    def update(self, platforms):
        next_rect = self.rect.move(self.speed * self.direction, 0)
        hits_wall = any(p.rect.colliderect(next_rect) for p in platforms)

        if hits_wall or not self._has_ground(next_rect, platforms):
            self.direction *= -1
        else:
            self.rect = next_rect


class StrongEnemy(Enemy):
    """Сильный враг: быстрее и выдерживает два попадания"""

    def __init__(self, x, y):
        super().__init__(x, y, hp=STRONG_ENEMY_HP, speed=STRONG_ENEMY_SPEED, color=STRONG_ENEMY_COLOR)