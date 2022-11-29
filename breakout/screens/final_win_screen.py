import pygame 
from screens.base_screen import BaseScreen
from breakout.components.happy_character import HappyCharacter
from breakout.components.final_win_flower import FinalWinFlower
# from .game_screen import GameScreen
from components.text_box import TextBox

class FinalWinScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        self.start_btn = TextBox((300, 80), "Play Again", bgcolor = (230, 173, 216)) # Width and Height, Text, Background Color 
        self.start_btn.rect.topleft = (250, 200)

        self.end_btn = TextBox((300, 80), "Exit", bgcolor = (173, 188, 230)) 
        self.end_btn.rect.topleft = (250, 300)

        self.happy_character = HappyCharacter()
        self.final_win_flower = FinalWinFlower()
        # self.game = GameScreen(BaseScreen)

    def draw(self):
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.start_btn.image, self.start_btn.rect)
        self.window.blit(self.end_btn.image, self.end_btn.rect)

        self.window.blit(self.happy_character.image, self.happy_character.rect)
        self.window.blit(self.final_win_flower.image, self.final_win_flower.rect)

        # self.window.blit(self.game.score_board, (0, 0))
   
    def update(self):
        pass 

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"
            if self.end_btn.rect.collidepoint(event.pos):
                self.running = False 
                self.next_screen = False 