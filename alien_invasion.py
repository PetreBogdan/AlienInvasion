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
            self._update_aliens()


    def _update_bullets(self): # Refracting again
        """Update pos of bullets and get rid of old ones"""
        self.bullets.update()

        # Get rid of bullets when reaching top
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_alien_bullet_collision()


    def _check_alien_bullet_collision(self):
        # Check for any bullets that have hit aliens
        # If so then get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and creates a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Creating one alien and find the number of aliens in a row
        # Spapcing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_heigth = alien.rect.size
        aviable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = aviable_space_x // (2 * alien_width) + 1

        # Determine the number of rows

        ship_heigth = self.ship.rect.height
        aviable_space_y = (self.settings.screen_heigth - (3 * alien_heigth) -
                           ship_heigth)
        number_rows = aviable_space_y // (2 * alien_heigth)

        # Creating the full fleet
        for row_number in range(number_rows):
            # Create the first row of aliens
            for alien_number in range(number_aliens_x):
                # Place aliens
                self._create_alien(alien_number, row_number)




    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_heigth = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the position of all aliens in the fleet and check direction"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """If reaching the edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


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
