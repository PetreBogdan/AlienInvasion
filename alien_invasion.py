import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Clasa jocului"""

    def __init__(self):
        """Initializam jocul"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")

        #Setam o culoare de background
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start main loop"""
        while True:
             # Watch fr keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Rescrie pe ecran pentru fiecare ietarie din loop
            self.screen.fill(self.bg_color)

            #Make the most recently drawn screen visible
            pygame.display.flip()


if __name__== '__main__':
    #Se creeasa o instanta de joc

    ai = AlienInvasion()
    ai.run_game()
