import pygame 
from screens.base_screen import BaseScreen 
from components.text_box import TextBox

class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        # WelcomeScreen Buttons 
        self.start_btn = TextBox((300, 100), "Start", bgcolor = (230, 173, 216)) # Width and Height, Text, Background Color 
        self.instruction_btn = TextBox((300, 100), "Instruction", bgcolor = (173, 188, 230))
        self.start_btn.rect.topleft = (250, 200)
        self.instruction_btn.rect.topleft = (250, 400)      

    def draw(self):
        background_image = pygame.image.load("./images/background_character.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))


        self.window.blit(self.start_btn.image, self.start_btn.rect)
        self.window.blit(self.instruction_btn.image, self.instruction_btn.rect)

    def update(self):
        pass 

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"
            if self.instruction_btn.rect.collidepoint(event.pos):
                self.running = False 
                self.next_screen = "instruction"