import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.x = 0
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/planet-2026998_1280.png')
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.center_ship()



        # flag for hold button
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flag."""
        if self.moving_right and self.rect.x <= self.screen_rect.right - 50:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.x >= self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Update rectangle from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        # Start each new ship at the bottom center in this screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position and modify y place.
        self.x = float(self.rect.x)
        self.rect.y -= 10
