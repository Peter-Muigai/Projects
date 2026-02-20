import pygame

class Player(pygame.sprite.Sprite):
    """A class to manage player assets."""
    def __init__(self, settings, screen):
        """Initialize player attributes."""
        super().__init__()
        self.screen = screen
        self.settings = settings

