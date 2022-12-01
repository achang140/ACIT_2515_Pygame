import pygame, webbrowser 
from screens.base_screen import BaseScreen
from breakout.components.happy_character import HappyCharacter
from breakout.components.final_win_flower import FinalWinFlower
from components.text_box import TextBox
from subprocess import Popen 

class FinalWinScreen(BaseScreen):
    """ 
    Final Screen to Winners 
    Inherit from BaseScreen 
    
    """
    def __init__(self, window,state):
        """_Constructor """
        super().__init__(window,state)
        self.start_btn = TextBox((300, 80), "Play Again", bgcolor = (230, 173, 216)) # Width and Height, Text, Background Color 
        self.start_btn.rect.topleft = (250, 200)

        self.end_btn = TextBox((300, 80), "Exit", bgcolor = (173, 188, 230)) 
        self.end_btn.rect.topleft = (250, 300)

        self.score_board = TextBox((150, 50), "Score: " + str(self.state["final_score"]), bgcolor = (255, 192, 77)) # Width and Height, Text, Background Color 
        self.score_board.rect.x = 330 
        self.score_board.rect.y = 60
    
        self.timer = TextBox((150, 50), "Time: " + str(self.state["final_time"]), bgcolor = (255, 192, 77))
        self.timer.rect.x = 330 
        self.timer.rect.y = 130

        self.happy_character = HappyCharacter()
        self.final_win_flower = FinalWinFlower()
        # self.game = GameScreen(BaseScreen)

    def draw(self):
        """ 
        Draw 2 buttons (Start and Exit), 2 images (Character and Flower), 
        final score, and final time onto the screen 
        """
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.start_btn.image, self.start_btn.rect)
        self.window.blit(self.end_btn.image, self.end_btn.rect)

        self.window.blit(self.happy_character.image, self.happy_character.rect)
        self.window.blit(self.final_win_flower.image, self.final_win_flower.rect)

        self.window.blit(self.score_board.image, self.score_board.rect)
        self.window.blit(self.timer.image, self.timer.rect)

        # self.window.blit(self.game.score_board, (0, 0))
   
    def update(self):
        pass 

    def manage_event(self, event):
        """ 
        Detect mouse action, click on start to 
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.write_to_json()
                self.running = False
                self.next_screen = "userinfo"
            if self.end_btn.rect.collidepoint(event.pos):
                self.write_to_json()
                Popen("python app.py")
                webbrowser.open("http://127.0.0.1:5000")
                self.running = False 
                self.next_screen = False 