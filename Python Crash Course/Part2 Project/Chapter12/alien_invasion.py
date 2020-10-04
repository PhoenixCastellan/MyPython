import sys
from alien_invasion_settings import Settings
import pygame, pygame.display
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_high))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()