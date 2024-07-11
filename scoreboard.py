import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize the score keeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 20)

        # Prepare the initial score and high score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Current Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center high score at the top screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into the screen"""
        level_str = "Current Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Place the level bellow the current score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many reminder left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)

            # Decrement width and height by a certain factor or fixed amount
            scale_factor = 0.5  # Example: reduce size to 50%
            original_width = ship.rect.width
            original_height = ship.rect.height
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)

            # Scale the ship image
            ship.image = pygame.transform.scale(ship.image, (new_width, new_height))
            ship.rect = ship.image.get_rect()  # Update rect to the new image size

            # Position the ship
            ship.rect.x = 10 + ship_number * (new_width + 10)
            ship.rect.y = 10

            self.ships.add(ship)

    def show_scoreboard(self):
        """Draw the score, the level and ships on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """To check if the high score has been broken."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
