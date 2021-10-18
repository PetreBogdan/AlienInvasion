import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group() # Creates a bullet group
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # Setting a background color
        self.bg_color = (self.settings.bg_color)


    def run_game(self):
        """Start main loop"""
        while True:
            self._check_events() # Refracting the code to be easer to read
            self._update_screen()
            self.ship.update()
            self._update_bullets()

    def _update_bullets(self): # Refracting again
        """Update pos of bullets and get rid of old ones"""
        self.bullets.update()

        # Get rid of bullets when reaching top
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Making one alien first
        alien = Alien(self)
        self.aliens.add(alien)

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event): # Refractoring again
        '''Keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Create a bullet in the bullet group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # Rewrite the screen for every loop in the run_game()
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()



if __name__== '__main__':
    # Creates an instance of a game

    ai = AlienInvasion()
    ai.run_game()
