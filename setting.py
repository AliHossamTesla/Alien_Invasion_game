class Settings:
    """A class to store settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet_direction of 1 represent right; -1 represents left.
        self.alien_points = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

        # Scoring points.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings based on level."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
