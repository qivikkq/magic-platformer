import sys
from sys import platform

import pygame

from game.settings import WIDTH, HEIGHT, FPS, TITLE, BACKGROUND, WHITE, BASE_DIR, TILE_SIZE
from game.states import GameState
from game.player import Player
from game.level import Level
from game.camera import Camera
from game.ui.rules_popup import RulesPopup

class Game:
    """Главный класс: окно, игровой цикл, смена состояний."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)

        self.running = True
        self.state = GameState.RULES

        self.rules_popup = RulesPopup()

        # Загрузка уровня
        self.level = Level()
        self.level.load(BASE_DIR / "levels" / "level1.txt")

        # Загрузка игрока в точке Р
        self.player = Player(*self.level.player_start)

        self.projectiles = pygame.sprite.Group()

        # Создаём камеру
        self.camera = Camera(self.level.width * TILE_SIZE, self.level.height * TILE_SIZE)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif (self.state == GameState.RULES and self.rules_popup.handle_event(event)):
                self.state = GameState.PLAYING

            # ВРЕМЕННО: цифры 1-3 переключают состояния для проверки.
            # Удалим, когда появятся настоящие кнопки.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.state = GameState.RULES
                elif event.key == pygame.K_2:
                    self.state = GameState.PLAYING
                elif event.key == pygame.K_3:
                    self.state = GameState.RESULT
                elif event.key == pygame.K_SPACE and self.state == GameState.PLAYING:
                    projectile = self.player.shoot()
                    self.projectiles.add(projectile)

    def update(self):
        if self.state == GameState.PLAYING:
            self.player.update(self.level.platforms)
            self.level.enemies.update(self.level.platforms)
            self.projectiles.update(self.level.platforms, self.level.enemies)
            if pygame.sprite.spritecollide(self.player, self.level.enemies, False):
                self.player.respawn()
            self.camera.update(self.player)


    def draw(self):
        self.screen.fill(BACKGROUND)

        if self.state == GameState.RULES:
            self.rules_popup.draw(self.screen)
        elif self.state == GameState.PLAYING:
            for platform in self.level.platforms:
                self.screen.blit(platform.image, self.camera.apply(platform))

            for enemy in self.level.enemies:
                self.screen.blit(enemy.image, self.camera.apply(enemy))

            for projectile in self.projectiles:
                self.screen.blit(projectile.image, self.camera.apply(projectile))

            self.screen.blit(self.player.image, self.camera.apply(self.player))

        text = self.font.render(self.state.name, True, WHITE)
        self.screen.blit(text, (20, 20))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
