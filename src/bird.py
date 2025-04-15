import pygame
import time

class Bird:
    """Class to manage the bird the player controls."""
    def __init__(self, flappy_bird):
        """Initialize the bird."""
        self.game = flappy_bird
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = self.game.settings

        self.clock = self.game.clock

        self.images = []
        self.load_images()

        self.reset_position()
        
        self.last_update_time = time.time()

        self.jumping = False

        self.jump_time = time.time()
        self.velocity = 0
        self.bird_dead = False

        self.y = float(self.rect.y)

        self.angle = 0
    
    def update(self):
        if not self.game.game_over:
            self._change_image()

        if self.game.game_active:
                if self.rect.centerx <= self.screen_rect.centerx:
                    self.rect.right += 3
                self._apply_gravity()
                
        if self.game.game_over:
            if self.rect.top <= self.screen_rect.bottom + 10:
                self.bird_image = self.dead_bird_img
                self._apply_gravity()

                self.angle += 20
                self.angle % 360
                self.bird_image = pygame.transform.rotate(self.dead_bird_img,
                                                           self.angle)
                self.rect = self.bird_image.get_rect(center=self.rect.center)
            else:
                self.game.game_active = False
        
        self.rect.y = self.y

    def _apply_gravity(self):
        current_time = time.time()
        if current_time - self.jump_time > self.settings.jump_duration:
            self.jumping = False

        if self.jumping:
                    self.velocity = self.settings.jump_force
        else:
                    self.velocity += self.settings.gravity
                
        self.y += self.velocity

    def _change_image(self):
        current_time = time.time()
        if current_time - self.last_update_time >= 0.1:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.last_update_time = current_time
            self.bird_image = self.images[self.image_index]

    def draw_bird(self):
        self.screen.blit(self.bird_image, self.rect)

    def load_images(self):
        for img_number in range(1,4):
            img = pygame.image.load(
                f"Images/bird{img_number}.png").convert_alpha()
            self.images.append(img)
        
        self.bird_image = self.images[0]
        self.rect = self.bird_image.get_rect()
        self.image_index = 0

        self.dead_bird_img = pygame.image.load("Images/dead_bird.png")
    
    def bird_jump(self):
        self.jump_time = time.time()
        self.jumping = True

    def reset_position(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y
        self.velocity = 0
        self.angle = 0
        self.rect = self.images[0].get_rect(center=self.rect.center)
        

        