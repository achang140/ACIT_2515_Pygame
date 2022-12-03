import pygame, random
from .flower import Flower

class FlowerEnv(pygame.sprite.Group):
    """ Class to add a flower with a search bubble "Water Me" to a sprite group """
    def __init__(self):
        """ Add the flower to a sprite group. This allows the character collide with the flower to achieve the goal """
        super().__init__()
        
        flower = Flower()
        self.add(flower)
