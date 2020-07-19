import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represents a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and define its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Read the alien image and define its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Place a new alien near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact horizontal alien position.?!
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
        