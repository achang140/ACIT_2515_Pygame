import pygame, random 
from .snow import Snow

class SnowCondition(pygame.sprite.Group):
    """ Class to generate snow """
    def __init__(self):
        """ 
        Generates 20 snow sprites from x range 0 to 20. 
        Add the snow sprites to a sprite group. 
        """
        super().__init__()

        start_x = random.randint(0, 20)
        start_y = 0 
        
        for i in range(20):
            snow = Snow()
            snow.rect.y = start_y
            self.add(snow)
            snow.rect.x += start_x