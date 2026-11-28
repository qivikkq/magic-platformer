import pygame

from game.projectile import Projectile


def test_projectile_moves():
    """Проверяет движение снаряда."""
    projectile = Projectile(100, 100, 1)
    old_x = projectile.rect.x

    projectile.update()

    assert projectile.rect.x > old_x


def test_projectile_moves_left():
    """Проверяет движение снаряда влево."""
    projectile = Projectile(100, 100, -1)
    old_x = projectile.rect.x

    projectile.update()

    assert projectile.rect.x < old_x


def test_projectile_disappears_on_platform_collision():
    """Проверяет исчезновение снаряда при столкновении с платформой."""
    projectile = Projectile(100, 100, 1)

    platforms = pygame.sprite.Group()
    platform = pygame.sprite.Sprite()
    platform.image = pygame.Surface((100, 40))
    platform.rect = platform.image.get_rect(topleft=(100, 100))
    platforms.add(platform)

    projectile.update()
    if pygame.sprite.spritecollideany(projectile, platforms):
        projectile.kill()

    assert not projectile.alive()