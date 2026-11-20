import pygame
from game.ui.button import Button


class Popup:
    def __init__(self, title, text_lines, button_text):
        self.title = title
        self.text_lines = text_lines

        self.title_font = pygame.font.Font(None, 48)
        self.text_font = pygame.font.Font(None, 32)

        self.rect = pygame.Rect(0, 0, 600, 420)

        self.button = Button(
            pygame.Rect(0, 0, 200, 55),
            button_text
        )

    def draw(self, screen):
        # Затемняем игровой экран
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        # Рисуем окно
        self.rect.center = screen.get_rect().center
        pygame.draw.rect(screen, (240, 240, 240), self.rect)
        pygame.draw.rect(screen, (30, 30, 30), self.rect, 3)

        # Рисуем заголовок
        title_surface = self.title_font.render(
            self.title, True, (30, 30, 30)
        )
        title_rect = title_surface.get_rect(
            center=(self.rect.centerx, self.rect.y + 55)
        )
        screen.blit(title_surface, title_rect)

        # Рисуем строки текста
        y = self.rect.y + 120

        for line in self.text_lines:
            text_surface = self.text_font.render(
                line, True, (30, 30, 30)
            )
            text_rect = text_surface.get_rect(
                center=(self.rect.centerx, y)
            )
            screen.blit(text_surface, text_rect)
            y += 40

        # Размещаем и рисуем кнопку
        self.button.rect.center = (
            self.rect.centerx,
            self.rect.bottom - 55
        )
        self.button.draw(screen)

    def handle_event(self, event):
        if self.button.is_clicked(event):
            return True

        return False
