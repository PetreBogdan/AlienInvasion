import pygame.image
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class for the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Loading the ship image
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Starting game with a ship at the bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Store de decimal value
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Drawing the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship movement based on the movement flag"""
        # Update the speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Centers Ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)