import pygame.font 

class Scoreboard:
    """Class designed to represent scoring information."""
    def __init__(self, ai_game):
        """Initialize scoring attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for score information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial scoring images.
        self.prep_score()

    def prep_score(self):
        """Convert a score to a generated image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Score display in the top right corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20

    def show_score(self):
        """Displays scores, level, and ships on the screen."""
        self.screen.blit(self.score_image, self.score_rect)