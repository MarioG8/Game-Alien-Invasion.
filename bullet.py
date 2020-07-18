import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class intended for the management of missiles launched by a ship."""

    def __init__(self, ai_game):
        """Create a missile object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rectangle at point (0, 0) and then define the appropriate position for it.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The position of the bullet is defined by a floating point value.
        self.y = float(self.rect.y)

    def update(self):
        """Moving the missile around the screen."""
        # Update bullet position.
        self.y -= self.settings.bullet_speed
        # Update the position of the bullet rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Display the missile on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)