import pygame 
import random

class CleanWater(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/clean_water.png")
        self.rect = self.image.get_rect() 
        self.rect.x = random.randint(0, 800)

    def update(self):
        self.rect.y += random.randint(0,30) # Drop from Sky 
        if self.rect.bottom == 700:
            self.kill() # Water Drop to the Ground, Dissappear 
