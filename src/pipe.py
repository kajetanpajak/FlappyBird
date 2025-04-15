import pygame
from random import randint

class Pipe:
    """Class to create a single pipe obstacle."""
    def __init__(self, flappy_bird):
        self.game = flappy_bird
        self.screen = self.game.screen
        self.settings = self.game.settings

        self.pipe_up_img = pygame.image.load(
            'Images/pipe_up.png'
            ).convert_alpha()
        self.pipe_down_img = pygame.image.load(
            'Images/pipe_down.png'
            ).convert_alpha()
        
        self.up_rect = self.pipe_up_img.get_rect()
        
        self.down_rect = self.pipe_down_img.get_rect()
        
        self.gap = self.settings.pipe_gap

        self._initialize_location()

        self.scored = False

    def _initialize_location(self):
        self.x = float(self.settings.screen_width)
        
        self.down_rect.bottom = randint(220, 450)
        self.up_rect.y = self.down_rect.bottom + self.gap

    def update(self):
        self.x -= self.settings.bird_speed
        
        self.down_rect.x = self.x
        self.up_rect.x = self.x
    
    def draw(self):
        self.screen.blit(self.pipe_down_img, self.down_rect)
        self.screen.blit(self.pipe_up_img, self.up_rect)