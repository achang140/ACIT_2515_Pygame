import pygame 

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("./images/character.png")
        self.rect = self.image.get_rect() 

        self.rect.x = 700 / 2 # Starting X-Position 
        self.rect.bottom = 700 # Starting Y-Position 
        
        # A Rectangle Around the Container
        # self.rect_rectangle = pygame.Rect(350, 530, 80, 60) # First 2: Position, Last 2: Size of Rectangle  

    def move_right(self):
        self.rect.x += 30
        # Prevent Character from Moving Out of the Screen 
        print(self.rect.x)
        if self.rect.left > 725: 
            self.rect.x = 720
    
    def move_left(self):
        self.rect.x -= 30
        # Prevent Character from Moving Out of the Screen 
        if self.rect.left < 0: 
            self.rect.x = 0
