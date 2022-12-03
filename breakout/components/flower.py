import pygame 

class Flower(pygame.sprite.Sprite):
    """ Class to make a flower with a search bubble "Water Me" for the game_screen """
    def __init__(self):
        """ Set the position of the flower on the game_screen """
        super().__init__()
        
        self.image = pygame.image.load("./images/flower.png")
        self.rect = self.image.get_rect() 

        # Location of the Flower 
        self.rect.x = 670 
        self.rect.bottom = 400