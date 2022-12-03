import pygame, random 

class DirtyWater(pygame.sprite.Sprite):
    """ Class to make a dirty water droplet sprite """
    def __init__(self):
        """ Constructs the necessary components for DirtyWater class """
        super().__init__()
        self.image = pygame.image.load("./images/dirty_water.png")
        self.rect = self.image.get_rect() 
        self.rect.x = random.randint(0, 800)

    def update(self):
        """ 
        Controls the movement of dirty water droplets. 
        Eliminates dirty water droplets that touches the ground. 
        """
        self.rect.y += random.randint(-10, 30) # Drop from Sky 
        if self.rect.bottom > 650:
            self.kill() # Water Drop to the Ground, Dissappear 