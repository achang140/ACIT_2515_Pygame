import pygame 

class FinalWinFlower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("./images/final_happy_flower.png")
        self.rect = self.image.get_rect() 

        self.rect.x = 670 # Starting X-Position 
        self.rect.bottom = 400