import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class for managing a spacecraft."""
    
    def __init__(self, ai_game):
        """Spacecraft initialization and its initial position.""" 
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Loading the spacecraft image and retrieving its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # The ship's horizontal position is stored as a floating point number.
        self.x = float(self.rect.x)

        #Options that indicate the movement of the ship.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the option that indicates its movement."""
        #Update the X coordinate value of the ship, not its rectangle.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Updating the rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Displaying the spacecraft in its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Puts the ship in the center of the bottom edge of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)