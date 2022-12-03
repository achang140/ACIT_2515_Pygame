import pygame, random
from .clean_water import CleanWater

class CleanCondition(pygame.sprite.Group):
    """ Class to generate clean water droplets """
    def __init__(self):
        """ 
        Generate 35 clean water droplets from x range 0 to 500. 
        Add the clean water droplets to a sprite group. 
        """
        super().__init__()
        
        start_x = random.randint(0, 500)
        start_y = 0 
        
        for i in range(35):
            clean_water = CleanWater()
            clean_water.rect.y = start_y
            self.add(clean_water)
            clean_water.rect.x += start_x 
