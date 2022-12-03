import pygame 

class FinalFlower(pygame.sprite.Sprite):
    """ Class to make a flower with a speech balloon "Thirsty" on the final_screen """
    def __init__(self):
        """ Set the position of the flower on the final_screen """
        super().__init__()
        
        self.image = pygame.image.load("./images/final_flower.png")
        self.rect = self.image.get_rect() 

        # Location of the Flower 
        self.rect.x = 670 
        self.rect.bottom = 400 