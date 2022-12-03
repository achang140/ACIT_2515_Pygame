import pygame 

class FinalWinFlower(pygame.sprite.Sprite):
    """ Class to make a flower with a speech balloon "Thank you" for the final_win_screen """
    def __init__(self):
        """ Set the position of the flower on the final_win_screen """
        super().__init__()
        
        self.image = pygame.image.load("./images/final_happy_flower.png")
        self.rect = self.image.get_rect() 

        # Location of the Flower 
        self.rect.x = 670 
        self.rect.bottom = 400 