import pygame 
from screens.base_screen import BaseScreen
from components.text_box import TextBox

class UserInfo(BaseScreen):
    def __init__(self, window, state):
        super().__init__(window, state)
        self.user_name = "" 

    def draw(self):
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.ask_box.image, self.ask_box.rect)
        self.window.blit(self.name_box.image, self.name_box.rect)

    def update(self):
        self.ask_box = TextBox((100, 100), "Name: ", bgcolor = (255, 253, 246))
        self.name_box = TextBox((200, 100), str(self.user_name), bgcolor = (255, 253, 150))        
        self.ask_box.rect.topright = (460, 100)
        self.name_box.rect.topright = (500, 200)
    

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_name = self.user_name[:-1]
            elif event.key in range(pygame.K_a, pygame.K_z):
                self.user_name += event.unicode
            self.state["username"] = self.user_name 
            
            if len(self.user_name) > 0:  
                if event.key == pygame.K_RETURN:
                    self.running = False
                    self.next_screen = "game"