import pygame
from game.settings import WIDTH, CAMERA_DEADZONE


class Camera:
    def __init__(self, level_width_px, level_height_px):
        self.offset_x = 0
        self.offset_y = 0
        self.level_w = level_width_px
        self.level_h = level_height_px

    def update(self, target_rect):
        center_x = target_rect.centerx - self.offset_x

        if center_x > WIDTH - CAMERA_DEADZONE:
            self.offset_x = target_rect.centerx - (WIDTH - CAMERA_DEADZONE)
        elif center_x < CAMERA_DEADZONE:
            self.offset_x = target_rect.centerx - CAMERA_DEADZONE

        max_x = max(0, self.level_w - WIDTH)
        self.offset_x = max(0, min(self.offset_x, max_x))

    def apply(self, sprite):
        return sprite.rect.move(-self.offset_x, -self.offset_y)