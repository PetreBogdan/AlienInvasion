import pygame.image


class Ship:
    """A class for the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Incarca imaginea nava
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #Incepe jocul mereu cu o noua nava in centru jos
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Drawing the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship movement based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
