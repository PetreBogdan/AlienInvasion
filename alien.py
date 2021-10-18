import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Class to represent an Alein'''

    def __init__(self, ai_game):
        '''Starting position and creating an Alien'''
        super().__init__()
        self.screen = ai_game

        # Loading the image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Starting with the Alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the horizontal pos
        self.x = float(self.rect.x)