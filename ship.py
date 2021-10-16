import pygame.image


class Ship:
    """O clasa pentru o nava"""

    def __init__(self, ai_game):
        """Initializam nava si pozitia de start"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Incarca imaginea nava
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #Incepe jocul mereu cu o noua nava in centru jos
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Deseneaza nava"""
        self.screen.blit(self.image, self.rect)
