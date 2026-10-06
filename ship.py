import pygame

class Ship:
    """A class to manage aspects of the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets\Strawb_Spaceship.bmp')