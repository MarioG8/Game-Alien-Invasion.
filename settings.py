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
        
        #Bullets settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3