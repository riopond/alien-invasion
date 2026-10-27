class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1300
        self.screen_height = 850
        self.bg_colour = (25, 25, 112) # Colours in PyGame are RGB

        # Ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (250, 249, 246)
        self.bullets_allowed = 8