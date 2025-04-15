import pygame



class Background:
    """Class to manage background textures and animation."""
    def __init__(self, flappy_bird):

        self.game = flappy_bird
        self.screen = flappy_bird.screen
        self.settings = flappy_bird.settings

        self.background_img = pygame.image.load("Images/chuj.png")
        self.background_rect = self.background_img.get_rect()

        self.init_floor()



    def draw_background(self):
        self.screen.blit(self.background_img, self.background_rect)
        self.screen.blit(self.background_img,self.background_rect.topright)
        if not self.game.game_over:
            self._animate_floor()
        self.floors.draw(self.screen)


    def init_floor(self):
        self.floors = pygame.sprite.Group()
        floor = Floor()
        current_x = 0
        for floor_number in range(4):
            new_floor = Floor()
            new_floor.rect.left = current_x
            new_floor.rect.bottom = self.settings.screen_height
            self.floors.add(new_floor)
            current_x += floor.rect.width

    def _animate_floor(self):
        for floor in self.floors:
            floor.rect.left -= self.settings.bird_speed
            if floor.rect.right < -5:
                floor.rect.left = self.settings.screen_width
            

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/floor2.bmp")
        self.rect = self.image.get_rect()