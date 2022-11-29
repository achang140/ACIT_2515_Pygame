### For Testing ONLY ### 

import pygame 
from screens.base_screen import BaseScreen
from .game_screen import GameScreen 
from breakout.components.unhappy_character import UnhappyCharacter
from breakout.components.final_flower import FinalFlower
from components.text_box import TextBox


class TestFinalScreen(GameScreen):
    def __init__(self, window):
        super().__init__(window)
        self.start_btn = TextBox((300, 100), "Play Again", bgcolor = (230, 173, 216)) # Width and Height, Text, Background Color 
        self.start_btn.rect.topleft = (250, 200)
        
        self.game = GameScreen(BaseScreen) 
        print(self.game.score)

        self.unhappy_character = UnhappyCharacter()
        self.final_flower = FinalFlower()


    def draw(self):
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.start_btn.image, self.start_btn.rect)

        self.window.blit(self.unhappy_character.image, self.unhappy_character.rect)
        self.window.blit(self.final_flower.image, self.final_flower.rect)


        self.window.blit(self.score_board.image, self.score_board.rect)
        self.window.blit(self.timer.image, self.timer.rect)

    def update(self):
        self.score_board = TextBox((150, 50), "Score: " + str(self.game.score), bgcolor = (255, 192, 77)) # Width and Height, Text, Background Color 
        self.score_board.rect.x = 330 
        self.score_board.rect.y = 60
    
        self.timer = TextBox((150, 50), "Time: " + str(self.game.final_time), bgcolor = (255, 192, 77))
        self.timer.rect.x = 330 
        self.timer.rect.y = 130
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"
