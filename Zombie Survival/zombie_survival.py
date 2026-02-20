import sys
import pygame

from settings import Settings
from player import Player

class ZombieSurvival:
    """Overall class to manage all assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake Game")
        self.player = Player(self.settings, self.screen)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse movements."""
        # Watch the keyboard and mouse movement.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the player to the right
                    self.player.rect.x += 1


    def _update_screen(self):
        """Update the screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = ZombieSurvival()
    ai.run_game()
