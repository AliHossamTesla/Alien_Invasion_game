class GameStats:
    """Tracks statistics for Alien Invasion Game."""

    def __init__(self, ai_game):
        """Initialize statistics about Alien."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # Score attributes.

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0
        self.ships_left = self.settings.ship_limit

