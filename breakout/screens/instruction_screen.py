import pygame 
from screen import BaseScreen
from component import TextBox

class InstructionScreen(BaseScreen):
    """ 
    InstructionScreen Class inherits from BaseScreen Class 
    Instruction screen is a help tool that gives the player tips before entering the game for the first time. 
    """
    def __init__(self, window, state):
        """
        Position the "Play Now" button on the instruction_screen 
        """
        super().__init__(window, state)

        self.start_btn = TextBox((150, 80), "Play Now", bgcolor = (251, 191, 119)) # Width and Height, Text, Background Color 
        self.start_btn.rect.topright = (790, 0)
    
    def draw(self):
        """
        Instruction Screen with a page of instruction and a "Start Now" button to begin the game. 
        """
        instruction_image = pygame.image.load("./images/instruction.png")
        instruction = pygame.transform.scale(instruction_image, (800, 700))
        self.window.blit(instruction, (0, 0))
    
        self.window.blit(self.start_btn.image, self.start_btn.rect)

    def manage_event(self, event):
        """ 
        Detects mouse actions. 
        If the user clicks the "Play Now" button, directs to the user_info_screen asking for the username.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "userinfo"
