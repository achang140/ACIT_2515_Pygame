import pygame
from breakout.screens import WelcomeScreen, InstructionScreen, UserInfo, GameScreen, FinalScreen, FinalWinScreen

class Game:
    """Main class for the application"""

    def __init__(self):
        # Window Size 
        display_width = 800 
        display_height = 700
        self.window = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Catch Raindrops and Rescue the Flower in the Desert")

    def run(self):
        """Main method, manages interaction between screens"""

        # Available Screens
        screens = {
            "welcome": WelcomeScreen,
            "instruction": InstructionScreen, 
            "userinfo": UserInfo, 
            "game": GameScreen,
            "finalwin": FinalWinScreen,
            "final": FinalScreen, 
        }

        running = True
        # Start with WelcomeScreen 
        current_screen = "welcome"
        state = {}
        while running:
            screen_class = screens.get(current_screen) 
            if not screen_class:
                raise RuntimeError(f"{current_screen} screen not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window, state)

            # Run the screen
            screen.run()

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen
            state = screen.state 

if __name__ == "__main__":
    stickman = Game()
    stickman.run()
