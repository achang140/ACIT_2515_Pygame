import pygame
import random
from .flower import Flower

class FlowerEnv(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        flower = Flower()
        self.add(flower)
