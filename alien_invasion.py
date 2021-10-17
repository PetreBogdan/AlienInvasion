import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """The game class"""

    def __init__(self):
        """Initialize the game"""
        pygame.init() # Returns True for game is initialized
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heigth = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width, self.settings.screen_heigth
        # ))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Setting a background color
        self.bg_color = (self.settings.bg_color)


    def run_game(self):
        """Start main loop"""
        while True:
            self._check_events() # Refracting the code to be easer to read
            self._update_screen()
            self.ship.update()


    def _check_events(self):
        # Watch fr keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event): # Refractoring again
        '''Keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # Exits the game when q was pressed
            sys.exit()

    def _check_keyup_events(self, event): # Refractoring again
        '''Keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Rewrite the screen for every loop in the run_game()
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__== '__main__':
    # Creates an instance of a game

    ai = AlienInvasion()
    ai.run_game()
