import pygame
from game.settings import (UI_BUTTON_COLOR,
                           UI_BUTTON_HOVER_COLOR,
                           UI_TEXT_COLOR,
                           BUTTON_FONT_SIZE
                           )

class Button:
    def __init__(self, rect, text):
        self.rect = rect
        self.text = text
        self.font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        self.hovered = False

    def draw(self, screen):
        color = UI_BUTTON_HOVER_COLOR if self.hovered else UI_BUTTON_COLOR

        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, UI_TEXT_COLOR, self.rect, 2)

        text_surface = self.font.render(self.text, True, UI_TEXT_COLOR)

        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos))
