class GameStats:
    """Tracks statistics for Alien Invasion Game."""

    def __init__(self, ai_game):
        """Initialize statistics about Alien."""
        self.settings = ai_game.settings

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # Score attributes.
        self.score = 0
        self.ships_left = self.settings.ship_limit
        # High score should never be reset.
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0
        self.ships_left = self.settings.ship_limit
        self.level = 1
