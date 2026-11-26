import pygame

from game.settings import ENEMY_SIZE, ENEMY_COLOR, ENEMY_SPEED, ENEMY_HP

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