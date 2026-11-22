import sys

import pygame

from game.settings import WIDTH, HEIGHT, FPS, TITLE, BACKGROUND, WHITE
from game.states import GameState
from game.ui.rules_popup import RulesPopup
from game.player import Player


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
        self.player = Player(100, 400)
        # ВРЕМЕННО: тестовые платформы, пока нет Level
        self.platforms = pygame.sprite.Group()
        for x, y, w, h in [(0, 500, 960, 40), (200, 400, 150, 20), (450, 320, 150, 20)]:
            platform = pygame.sprite.Sprite()
            platform.rect = pygame.Rect(x, y, w, h)
            platform.image = pygame.Surface((w, h))
            platform.image.fill((90, 140, 90))
            self.platforms.add(platform)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.state == GameState.RULES:
                if self.rules_popup.handle_event(event):
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

    def update(self):
        # Здесь позже появится логика каждого состояния
        if self.state == GameState.RULES:
            pass
        elif self.state == GameState.PLAYING:
            self.player.update(self.platforms)
        elif self.state == GameState.RESULT:
            pass

    def draw(self):
        self.screen.fill(BACKGROUND)

        # text = self.font.render(self.state.name, True, WHITE)
        # self.screen.blit(text, (20, 20))
        if self.state == GameState.RULES:
            self.rules_popup.draw(self.screen)

        elif self.state == GameState.PLAYING:
            text = self.font.render("PLAYING", True, WHITE)
            self.screen.blit(text, (20, 20))

        elif self.state == GameState.RESULT:
            text = self.font.render("RESULT", True, WHITE)
            self.screen.blit(text, (20, 20))
            
        if self.state == GameState.PLAYING:
            self.platforms.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)
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
