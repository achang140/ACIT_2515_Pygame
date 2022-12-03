import pygame 
from screen import BaseScreen 
from component import TextBox

class WelcomeScreen(BaseScreen):
    """
    WelcomeScreen Class inherits from BaseScreen Class 
    Welcome Screen with a "Start" button and an "Instruction" button 
    """
    def __init__(self, window, state):
        """ 
        Constructs necessary components for the welcome screen. 
        Style and position a "Start" button and an "Instruction" button 
        """
        super().__init__(window, state)

        self.start_btn = TextBox((300, 80), "Start", bgcolor = (230, 173, 216)) # Width and Height, Text, Background Color 
        self.start_btn.rect.topleft = (250, 200)

        self.instruction_btn = TextBox((300, 80), "Instruction", bgcolor = (173, 188, 230))
        self.instruction_btn.rect.topleft = (250, 300) 

    def draw(self):
        """ 
        Desert background with "Start" and "Instruction" buttons 
        """
        background_image = pygame.image.load("./images/background_character.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.start_btn.image, self.start_btn.rect)
        self.window.blit(self.instruction_btn.image, self.instruction_btn.rect)

    def update(self):
        pass

    def manage_event(self, event):
        """ 
        Detects mouse actions. 
        If the user clicks the "Start" button, directs to userinfo screen before starting the game. 
        If the user click the "Instruction" button, directs to the instruction page. 
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "userinfo"
            if self.instruction_btn.rect.collidepoint(event.pos):
                self.running = False 
                self.next_screen = "instruction"