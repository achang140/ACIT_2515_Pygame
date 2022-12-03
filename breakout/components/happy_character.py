import pygame 

class HappyCharacter(pygame.sprite.Sprite):
    """ Class to make a character sprite for the final_win_screen """
    def __init__(self):
        """ Set the position of the character on the final_win_screen """
        super().__init__()

        self.image = pygame.image.load("./images/final_happy.png")
        self.rect = self.image.get_rect() 

        self.rect.x = 700 / 2 # Starting X-Position 
        self.rect.bottom = 700 # Starting Y-Position 
