import pygame, random
from .dirty_water import DirtyWater

class DirtyCondition(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        start_x = random.randint(0, 20)
        start_y = 0 
        
        for i in range(5):
            dirty_water = DirtyWater()
            
            dirty_water.rect.y = start_y

            self.add(dirty_water)

            dirty_water.rect.x += start_x
