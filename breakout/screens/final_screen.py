import pygame 
from screens.base_screen import BaseScreen
from .game_screen import GameScreen
from components.text_box import TextBox

class FinalScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        self.start_btn = TextBox((300, 100), "Play Again", bgcolor = (230, 173, 216)) # Width and Height, Text, Background Color 
        self.start_btn.rect.topleft = (250, 200)
        self.game = GameScreen(BaseScreen)

    def draw(self):
        self.window.blit(self.start_btn.image, self.start_btn.rect)
        # self.window.blit(self.game.score_board, (0, 0))
   
    def update(self):
        pass 

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"
