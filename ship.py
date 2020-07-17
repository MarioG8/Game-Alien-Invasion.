import pygame

class Ship:
    """Class for managing a spacecraft."""
    
    def __init__(self, ai_game):
        """Spacecraft initialization and its initial position.""" 
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Loading the spacecraft image and retrieving its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Options that indicate the movement of the ship.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the option that indicates its movement."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Displaying the spacecraft in its current position"""
        self.screen.blit(self.image, self.rect)