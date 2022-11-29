import pygame 
from screens.base_screen import BaseScreen



class ReadyScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        pygame.time.set_timer()