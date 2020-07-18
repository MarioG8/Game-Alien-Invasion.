import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """General class for managing the resources and the way the game runs."""

    def __init__(self):
        """Initializing the game and creating its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        #Waiting for a key or mouse button to be pressed.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reaction to pressing a key."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self, event):
        """Reaction to key release."""       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """Create a new missile and add it to the missile group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update missiles and remove missiles not visible on screen."""
        # Updating the position of the missiles.
        self.bullets.update()

        # Removal of bullets that are off-screen.
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)


    def _update_screen(self):
        """Updating images and going to a new screen"""
            #Screen refresh in each iteration of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Display the last modified screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Creating a copy of the game and launching it.
    ai = AlienInvasion()
    ai.run_game()
