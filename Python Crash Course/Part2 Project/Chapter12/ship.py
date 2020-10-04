import pygame
from alien_invasion_settings import Settings


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.settings = ai_settings

        self.image = pygame.image.load(
            "E:\\source\\Workspaces\\seazen\\MyPython\\Python Crash Course\\Part2 Project\\Chapter12\\images\\ship.bmp"
        )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        if self.moving_forward and (self.rect.bottom > self.rect.h):
            self.bottom -= self.settings.ship_speed_factor
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
