class Settings:
    """Class intended for storing all settings."""

    def __init__(self):
        """Initializing game settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Spacecraft settings speed.
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullets settings.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien related settings.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # Easy game speed change.
        self.speedup_scale = 1.25

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing settings that change during the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0 

        # A fleet_direction value of 1 is right and -1 is left.
        self.fleet_direction = 1

        # Punctation.
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale