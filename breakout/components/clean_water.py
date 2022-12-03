import pygame, random

class CleanWater(pygame.sprite.Sprite):
    """ Class to make a clean water droplet sprite """
    def __init__(self):
        """ Constructs the necessary components for CleanWater class """
        super().__init__()
        self.image = pygame.image.load("./images/clean_water.png")
        self.rect = self.image.get_rect() 
        self.rect.x = random.randint(0, 800)

    def update(self):
        """ 
        Controls the movement of clean water droplets. 
        Eliminates clean water droplets that touches the ground. 
        """
        self.rect.y += random.randint(-5,20) # Drop from Sky 
        if self.rect.bottom == 700:
            self.kill() # Water Drop to the Ground, Dissappear 
