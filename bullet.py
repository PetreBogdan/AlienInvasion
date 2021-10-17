import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullet"""
    def __init__(self, ai_game):
        '''Creating a bullet at the current ship position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rectangle at (0, 0) and then set pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position is at a decimal value
        self.y = float(self.rect.y)

    def update(self):
        '''Move the bullet up the screen'''
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draws the bullet'''
        pygame.draw.rect(self.screen, self.color, self.rect)
