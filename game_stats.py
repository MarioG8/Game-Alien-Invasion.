class GameStats:
    """In-game statistics monitoring."""

    def __init__(self, ai_game):
        """Initializing the statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Launching the game in an inactive mode.
        self.game_active = False

        # The best score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialization of statistics that may change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        
