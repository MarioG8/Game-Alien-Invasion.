import sys 
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # Creation of a copy of the game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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

        self._check_bullet_alien_collision()

    
    def _check_bullet_alien_collision(self):
        """Collision reaction between missile and foreign."""
        # Removal of all projectiles and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        
        if not self.aliens:
            # Get rid of existing missiles and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

        

    def _update_aliens(self):
        """Checking if the alien fleet is at the edge,
        and then updating the position of all aliens in the fleet."""

        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji między obcym i statkiem.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()


    def _ship_hit(self):
        """Alien hitting a ship."""
        # Zmniejszenie wartości przechowywanej w ships_left.
        self.stats.ships_left -= 1

        # Removal of aliens and bullets lists.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Pause ..
        sleep(0.5)


    
    def _create_fleet(self):
        """Build a complete alien fleet."""
        # Create an alien and determine the number of aliens that will fit in the row.
        # The distance between each alien is equal to the width of the alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine how many rows of aliens will fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
        (3 * alien_height)- ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Formation of a complete alien fleet.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            # Creating an alien and placing it in a row.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)


    def _check_fleet_edges(self):
        """The appropriate reaction when an alien reaches the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Moving the entire fleet down and changing direction in which it is moving."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



    def _update_screen(self):
        """Updating images and going to a new screen"""
            #Screen refresh in each iteration of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Display the last modified screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Creating a copy of the game and launching it.
    ai = AlienInvasion()
    ai.run_game()
