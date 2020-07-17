import sys 
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """General class for managing the resources and the way the game runs."""

    def __init__(self):
        """Initializing the game and creating its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """Start the main game loop."""
        while True:
            #Waiting for a key or mouse button to be pressed.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        #Screen refresh in each iteration of the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Display the last modified screen.
            pygame.display.flip()

if __name__ == '__main__':
    # Creating a copy of the game and launching it.
    ai = AlienInvasion()
    ai.run_game()
