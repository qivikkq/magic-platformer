import sys
import pygame

from game.settings import WIDTH, HEIGHT, FPS, TITLE, BACKGROUND, WHITE
from game.states import GameState
from game.player import Player
from game.ui.rules_popup import RulesPopup
from game.level import Level
from game.stats import Stats
from game.ui.result_popup import ResultPopup


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

        self.level = Level.load('levels/level1.txt')
        self.platforms = self.level.platforms

        self.stats = Stats()
        self.result_popup = ResultPopup(self.stats)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif self.state == GameState.RULES:
                if self.rules_popup.handle_event(event):
                    self.state = GameState.PLAYING
                    self.stats.start_timer()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.state = GameState.RULES
                elif event.key == pygame.K_2:
                    self.state = GameState.PLAYING
                    self.stats.start_timer()
                elif event.key == pygame.K_3:
                    self.state = GameState.RESULT

            elif self.state == GameState.RESULT:
                if self.result_popup.handle_event(event):
                    pygame.quit()
                    sys.exit()

    def update(self):
        if self.state == GameState.PLAYING:
            self.player.update(self.platforms)

            total_enemies = getattr(self.level, 'total_enemies', 0)
            if total_enemies > 0 and self.stats.all_enemies_dead(total_enemies):
                self.state = GameState.RESULT

    def draw(self):
        self.screen.fill(BACKGROUND)

        if self.state == GameState.RULES:
            self.platforms.draw(self.screen)
            self.rules_popup.draw(self.screen)

        elif self.state == GameState.PLAYING:
            self.platforms.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)

        elif self.state == GameState.RESULT:
            self.platforms.draw(self.screen)
            self.result_popup.draw(self.screen)

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
