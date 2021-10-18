import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Class to represent an Alein'''

    def __init__(self, ai_game):
        '''Starting position and creating an Alien'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading the image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Starting with the Alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the horizontal pos
        self.x = float(self.rect.x)

    def update(self):
        """Move aliens to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
