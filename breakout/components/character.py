import pygame 

class Character(pygame.sprite.Sprite):
    """ Class to make a character sprite on the game_screen """
    def __init__(self):
        """ Set the starting position of the character on the game_screen """
        super().__init__()
        
        self.image = pygame.image.load("./images/character.png")
        self.rect = self.image.get_rect() 

        self.rect.x = 700 / 2 # Starting X-Position 
        self.rect.bottom = 700 # Starting Y-Position 
        
    def move_right(self):
        """ 
        Moves the character to the right by 30 pixels and 
        keeps the character within the screen. 
        """
        self.rect.x += 30
        # Prevent Character from Moving Out of the Screen 
        if self.rect.left > 725: 
            self.rect.x = 720
    
    def move_left(self):
        """
        Moves the character to the left by 30 pixels and 
        keeps the character within the screen.
        """
        self.rect.x -= 30
        # Prevent Character from Moving Out of the Screen 
        if self.rect.left < 0: 
            self.rect.x = 0

    def move_up(self):
        """
        Moves the character to the top by 15 pixels.
        """
        self.rect.y -= 15 

    def move_down(self):
        """
        Moves the character to the bottom by 15 pixels. 
        """
        self.rect.y += 15 
        