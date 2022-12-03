import pygame, math
from screen import BaseScreen
from breakout.components import Character, CleanCondition, DirtyCondition, SnowCondition, FlowerEnv
from component import TextBox

class GameScreen(BaseScreen):
    """ 
    GameScreen Class inherits from BaseScreen Class 
    Game Screen with a character that interacts with the four sprite groups (clean water, dirty water, snow, and flower). 
    """
    def __init__(self, window, state):
        """ 
        Constructs necessary components for the game. 
        Tracks scores and times for each player.
        """
        super().__init__(window, state)
        self.score = 0 
        self.time = pygame.time.get_ticks()
        self.final_time = 0 

        self.character = Character() 
        self.clean_condition = CleanCondition()
        self.dirty_condition = DirtyCondition()
        self.snow_condition = SnowCondition()
        self.flower_env = FlowerEnv()
    
    def draw(self):
        """ 
        Desert background with movable characters, controlled by the player using the arrow keys on the keyboard. 
        Draw sprite groups (clean water droplets, dirty water droplets, snow) and a flower onto the game screen. 
        """
        background_image = pygame.image.load("./images/background.png")
        background = pygame.transform.scale(background_image, (800, 700))
        self.window.blit(background, (0, 0))

        self.window.blit(self.score_board.image, self.score_board.rect)
        self.window.blit(self.timer.image, self.timer.rect)

        self.window.blit(self.character.image, self.character.rect)
        self.flower_env.draw(self.window)

        self.clean_condition.draw(self.window)
        self.dirty_condition.draw(self.window)
        self.snow_condition.draw(self.window)

    def update(self):
        """ 
        Update score and time on the game screen. 
        If the character touches a clean water drop, the score is increased by 2.
        If the character touches a snowflake, the score is increased by 1. 
        If the character touches a dirty water drop, the game is over and goes to the final_screen. 
        If the character touches the flower, the game ends and goes to the final_win_screen. 
        """
        current_time = pygame.time.get_ticks()
        
        self.clean_condition.update() 
        self.dirty_condition.update()
        self.snow_condition.update() 
        
        self.score_board = TextBox((150, 100), self.score, bgcolor = (255, 255, 220)) # Width and Height, Text, Background Color 
        self.score_board.rect.topright = (800, 0)

        seconds = math.floor((current_time - self.time) / 1000) 
        self.timer = TextBox((150, 100), seconds, bgcolor = (255, 255, 220))

        if pygame.sprite.spritecollide(self.character, self.clean_condition, dokill = True):
            self.score += 2
        
        if pygame.sprite.spritecollide(self.character, self.snow_condition, dokill = True):
            self.score += 1 

        if pygame.sprite.spritecollide(self.character, self.dirty_condition, dokill = True):
            # Append total score to self.state 
            self.state["final_score"] = self.score
            # Append total time to self.state 
            self.final_time += seconds 
            self.state["final_time"] = self.final_time 

            pygame.time.wait(150)
            self.running = False 
            self.next_screen = "final"

        if pygame.sprite.spritecollide(self.character, self.flower_env, dokill = False):
            # Append total score to self.state 
            self.state["final_score"] = self.score
            # Append total time to self.state 
            self.final_time += seconds 
            self.state["final_time"] = self.final_time

            self.running = False
            self.next_screen = "finalwin"
        
    def manage_event(self, event):
        """ 
        Detects keyboard actions. 
        Click the right arrow key, the character moves to the right. 
        Click the left arrow key, the character moves to the left. 
        Click the up arrow key, the character moves to the top. 
        Click the down arrow key, the character moves to the bottom. 
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.character.move_right()
            if event.key == pygame.K_LEFT:
                self.character.move_left()
            if event.key == pygame.K_UP:
                self.character.move_up()
            if event.key == pygame.K_DOWN:
                self.character.move_down()
