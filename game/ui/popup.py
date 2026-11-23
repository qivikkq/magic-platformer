import pygame

from game.ui.button import Button
from game.settings import (
    WIDTH,
    HEIGHT,
    UI_TEXT_COLOR,
    UI_PANEL_COLOR,
    UI_BORDER_COLOR,
    UI_SHADOW_COLOR,
    TITLE_FONT_PATH,
    TEXT_FONT_PATH,
    TITLE_FONT_SIZE,
    TEXT_FONT_SIZE
)


class Popup:
    def __init__(self, title, text_lines, button_text):
        self.title = title
        self.text_lines = text_lines

        # Настраиваем шрифты
        self.title_font = pygame.font.Font(
            str(TITLE_FONT_PATH), TITLE_FONT_SIZE
        )
        self.text_font = pygame.font.Font(
            str(TEXT_FONT_PATH), TEXT_FONT_SIZE
        )

        # Создаём окно по центру экрана
        self.rect = pygame.Rect(0, 0, 760, 420)
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        # Создаём кнопку
        button_rect = pygame.Rect(0, 0, 220, 60)
        button_rect.center = (
            self.rect.centerx,
            self.rect.bottom - 55
        )

        self.button = Button(button_rect, button_text)

    def draw(self, screen):
        # Затемняем игровой экран
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))

        # Рисуем тень окна
        shadow_rect = self.rect.move(8, 8)
        pygame.draw.rect(screen, UI_SHADOW_COLOR, shadow_rect)

        # Рисуем основное окно и его границу
        pygame.draw.rect(screen, UI_PANEL_COLOR, self.rect)
        pygame.draw.rect(screen, UI_BORDER_COLOR, self.rect, 3)

        # Рисуем заголовок
        title_surface = self.title_font.render(
            self.title, True, UI_TEXT_COLOR
        )
        title_rect = title_surface.get_rect(
            center=(self.rect.centerx, self.rect.y + 65)
        )
        screen.blit(title_surface, title_rect)

        # Рисуем основной текст
        y = self.rect.y + 145

        for line in self.text_lines:
            text_surface = self.text_font.render(
                line, True, UI_TEXT_COLOR
            )
            text_rect = text_surface.get_rect(
                center=(self.rect.centerx, y)
            )
            screen.blit(text_surface, text_rect)
            y += 38

        # Обновляем состояние кнопки и рисуем её
        self.button.update(pygame.mouse.get_pos())
        self.button.draw(screen)

    def handle_event(self, event):
        return self.button.is_clicked(event)