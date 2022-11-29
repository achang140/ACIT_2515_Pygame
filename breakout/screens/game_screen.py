import pygame 
from screens.base_screen import BaseScreen
from components.text_box import TextBox
from breakout.components.character import Character
# from breakout.components.happy_character import HappyCharacter
from breakout.components.clean_condition import CleanCondition
from breakout.components.dirty_condition import DirtyCondition
from breakout.components.snow_condition import SnowCondition
from breakout.components.flower_env import FlowerEnv


class GameScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        self.score = 0 

        self.character = Character() 
        # self.happy_character = HappyCharacter()
        self.clean_condition = CleanCondition()
        self.dirty_condition = DirtyCondition()
        self.snow_condition = SnowCondition()
        self.flower_env = FlowerEnv()
    
    def draw(self):
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.score_board.image, self.score_board.rect)

        self.window.blit(self.character.image, self.character.rect)
        self.flower_env.draw(self.window)

        self.clean_condition.draw(self.window)
        self.dirty_condition.draw(self.window)
        self.snow_condition.draw(self.window)

        # Change Character to Happy if self.score > 0 
        # if self.score > 0: 
        #     self.window.blit(self.happy_character.image, self.happy_character.rect)

        # Check Rectangle Around the Container 
        # pygame.draw.rect(self.window, (0, 0, 0), self.character.rect_rectangle, 2)

    def update(self):
        self.clean_condition.update() 
        self.dirty_condition.update()
        self.snow_condition.update() 
        
        self.score_board = TextBox((150, 100), self.score, bgcolor = (255, 255, 220)) # Width and Height, Text, Background Color 
        self.score_board.rect.topright = (800, 0)

        if pygame.sprite.spritecollide(self.character, self.clean_condition, dokill = True):
            self.score += 1 
            print(self.score)
        
        if pygame.sprite.spritecollide(self.character, self.snow_condition, dokill = True):
            self.score += 0.5 
            print(self.score)

        if pygame.sprite.spritecollide(self.character, self.dirty_condition, dokill = True):
            pygame.time.wait(150)
            self.running = False 
            self.next_screen = "final" 

        if pygame.sprite.spritecollide(self.character, self.flower_env, dokill = False):
            self.running = False
            self.next_screen = "finalwin"

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.character.move_right()
            if event.key == pygame.K_LEFT:
                self.character.move_left()
            if event.key == pygame.K_UP:
                self.character.move_up()
            if event.key == pygame.K_DOWN:
                self.character.move_down()