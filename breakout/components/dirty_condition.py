import pygame, random
from .dirty_water import DirtyWater

class DirtyCondition(pygame.sprite.Group):
    """ Class to generate dirty water droplets """
    def __init__(self):
        """
        Generate 5 dirty water droplets from x range from 0 to 20. 
        Add the dirty water droplets to a sprite group. 
        """
        super().__init__()
        
        start_x = random.randint(0, 20)
        start_y = 0 
        
        for i in range(5):
            dirty_water = DirtyWater()
            dirty_water.rect.y = start_y
            self.add(dirty_water)
            dirty_water.rect.x += start_x
