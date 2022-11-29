import pygame
from breakout.screens.welcome_screen import WelcomeScreen
from breakout.screens.game_screen import GameScreen
from breakout.screens.final_win_screen import FinalWinScreen 
from breakout.screens.final_screen import FinalScreen
from breakout.screens.test_final_screen import TestFinalScreen

class Game:
    """Main class for the application"""

    def __init__(self):
        # Window Size 
        display_width = 800 
        display_height = 700
        self.window = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Water in Desert")

    def run(self):
        """Main method, manages interaction between screens"""

        # Available Screens
        screens = {
            "welcome": WelcomeScreen,
            # "instruction": InstructionScreen, 
            "game": GameScreen,
            "finalwin": FinalWinScreen, # To be modified 
            "final": FinalScreen, 
            "testfinal": TestFinalScreen, 
        }

        running = True
        # Start with WelcomeScreen 
        current_screen = "welcome"
        
        while running:
            screen_class = screens.get(current_screen) 
            if not screen_class:
                raise RuntimeError(f"{current_screen} screen not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window)

            # Run the screen
            screen.run()

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen

if __name__ == "__main__":
    stickman = Game()
    stickman.run()
