import pygame


class Button:
    def __init__(self, rect, text):
        self.rect = rect
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            return False


    