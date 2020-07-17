class Settings:
    """Class intended for storing all settings."""

    def __init__(self):
        """Initializing game settings."""
        #Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #Spacecraft settings speed.
        self.ship_speed = 1.5
        