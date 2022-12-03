import pygame, webbrowser
from subprocess import Popen 
from screen import BaseScreen
from component import TextBox
from breakout.components import UnhappyCharacter, FinalFlower

class FinalScreen(BaseScreen):
    """ 
    FinalScreen Class inherits from BaseScreen Class 
    Final Screen to players who did not successful water the flower (Character touches the dirty water before colliding with the flower) 
    Position the buttons on the final_screen. 
    """
    def __init__(self, window, state):
        """ 
        Constructs necessary components for the final screen. 
        Background with an unhappy character and a thirsty flower. 
        Includes 2 buttons (start and exit), total score, and total time. 
        """
        super().__init__(window, state)
        self.play_again_btn = TextBox((300, 80), "Play Again", bgcolor = (255, 192, 203)) # Width and Height, Text, Background Color 
        self.play_again_btn.rect.topleft = (250, 200)

        self.end_btn = TextBox((300, 80), "Exit & See Flask Result", bgcolor = (238, 130, 238)) 
        self.end_btn.rect.topleft = (250, 300)

        self.score_board = TextBox((150, 50), "Score: " + str(self.state["final_score"]), bgcolor = (255, 192, 77)) # Width and Height, Text, Background Color 
        self.score_board.rect.x = 330 
        self.score_board.rect.y = 60
    
        self.timer = TextBox((150, 50), "Time: " + str(self.state["final_time"]), bgcolor = (255, 192, 77))
        self.timer.rect.x = 330 
        self.timer.rect.y = 130

        self.unhappy_character = UnhappyCharacter()
        self.final_flower = FinalFlower()

    def draw(self):
        """ 
        Final screen has a desert background with an unhappy character and a thirsty flower. 
        Draw 2 buttons (Start and Exit), 2 images (Character and Flower), 
        final score, and final time onto the final screen. 
        """
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.play_again_btn.image, self.play_again_btn.rect)
        self.window.blit(self.end_btn.image, self.end_btn.rect)

        self.window.blit(self.unhappy_character.image, self.unhappy_character.rect)
        self.window.blit(self.final_flower.image, self.final_flower.rect)

        self.window.blit(self.score_board.image, self.score_board.rect)
        self.window.blit(self.timer.image, self.timer.rect)
   
    def update(self):
        pass 

    def manage_event(self, event):
        """ 
        Detects mouse actions. 
        If the user clicks the "Play Again" button, redirect to the user_info_screen asking for the username.
        If the user clicks the "Exit" button, exit the pygame window and go directly to the Flask browser.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_again_btn.rect.collidepoint(event.pos):
                self.write_to_json()
                self.running = False
                self.next_screen = "userinfo"
            if self.end_btn.rect.collidepoint(event.pos):
                self.write_to_json()
                Popen("python app.py")
                webbrowser.open("http://127.0.0.1:5000")
                self.running = False 
                self.next_screen = False 