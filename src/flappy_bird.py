import pygame
import sys
import time
from settings import Settings
from background import Background
from bird import Bird
from pipe import Pipe
from button import Button
from scoreboard import Scoreboard

class FlappyBird:
    """Class to manage game resources and behavior."""
    def __init__(self):
        pygame.init()
        # Create an instance of the game's settings
        self.settings = Settings()
        # Initialize game window
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Flappy Bird")

        # Initialize background
        self.bg = Background(self)
        self.floors = self.bg.floors

        # Initialize clock
        self.clock = pygame.time.Clock()

        self.bird = Bird(self)

        self.last_pipe_time = time.time()

        self.pipes = []
        
        self.game_active = False
        self.game_over = False

        self.play_button = Button(self, "Play")

        self.scoreboard = Scoreboard(self)

        
    def run_game(self):
        """Game loop."""
        while True:
            self._check_events()

            self.bird.update()

            if self.game_active and not self.game_over:
                self._update_pipes()
                self._check_collisions()

            self._update_screen()

            self.clock.tick(60)
            
    def _update_screen(self):
        """Draw all elements of the game on the screen."""
        self.bg.draw_background()   
        
        self._draw_pipes()
    
        self.bird.draw_bird()
        self.scoreboard.draw()
        if not self.game_active or self.bird.bird_dead:
            self.play_button.draw_button()
        
        pygame.display.flip()        

    def _check_events(self):
        """Respond to events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_pressed(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_key_pressed(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bird.bird_jump()
            self._start_game()

    def _update_pipes(self):
        current_time = time.time()
        
        if current_time - self.last_pipe_time > self.settings.pipe_interval:
            self.pipes.append(Pipe(self))
            self.last_pipe_time = current_time

        for pipe in self.pipes:
            pipe.update()
            if not pipe.scored and pipe.x + pipe.up_rect.width < self.bird.rect.left:
                self.scoreboard.increase_score()
                pipe.scored = True

            # Usuwanie rury, jak zniknie z lewej
            if pipe.x < -pipe.up_rect.width:
                self.pipes.remove(pipe)
            
        
    def _draw_pipes(self):
        for pipe in self.pipes:
            pipe.draw()

    def _check_play_button(self, mouse_pos):
        """Start a new game when player presses play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()
            
    def _start_game(self):
        if not self.game_active:
            self.pipes.clear()
            self.game_over = False
            self.game_active = True
            self.bird.reset_position()
            self.play_button.prep_msg("Play again")
            self.scoreboard.reset()

    def _check_collisions(self):
        
        for pipe in self.pipes:
            if self.bird.rect.colliderect(pipe.up_rect) or (
                self.bird.rect.colliderect(pipe.down_rect)
            ):
                self.game_over = True
                self.bird.bird_jump()
                
        for floor in self.floors:
            if self.bird.rect.colliderect(floor.rect):
                self.game_over = True
                self.bird.bird_jump()
  

