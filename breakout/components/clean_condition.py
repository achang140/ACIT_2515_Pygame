import pygame
import random
from .clean_water import CleanWater

class CleanCondition(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        start_x = random.randint(0, 500)
        start_y = 0 
        for i in range(10):
            
            clean_water = CleanWater()
            
            clean_water.rect.x += start_x 
            clean_water.rect.y = start_y

            self.add(clean_water)
