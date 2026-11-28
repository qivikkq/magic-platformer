import pygame

from game.enemy import Enemy, StrongEnemy
from game.settings import ENEMY_SIZE

def make_platform(x, y, w, h):
    platform = pygame.sprite.Sprite()
    platform.rect = pygame.Rect(x, y, w, h)
    return platform


def test_enemy_dies_after_one_hit():
    assert Enemy(0, 0).take_hit() is True


def test_strong_enemy_dies_after_two_hit():
    enemy = StrongEnemy(0, 0)
    assert enemy.take_hit() is False
    assert enemy.take_hit() is True


def test_enemy_stays_on_platform():
    platforms = pygame.sprite.Group(make_platform(0, 100, 100, 20))

    enemy = Enemy(60, 100 - ENEMY_SIZE[1])

    for _ in range(200):
        enemy.update(platforms)

        assert enemy.rect.left >= 0
        assert enemy.rect.right <= 100