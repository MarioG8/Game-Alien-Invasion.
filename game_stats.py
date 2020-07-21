class GameStats:
    """In-game statistics monitoring."""

    def __init__(self, ai_game):
        """Initializing the statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Initialization of statistics that may change during the game."""
        self.ships_left = self.settings.ship_limit
