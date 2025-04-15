import pygame

class Scoreboard:
    def __init__(self, flappy_bird):
        self.game = flappy_bird
        self.screen = self.game.screen
        self.settings = self.game.settings
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(None, 72)

        self.score = 0
        self.high_score = 0

    def reset(self):
        self.score = 0

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self):
        score_surf = self.font.render(str(self.score), True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(self.settings.screen_width // 2, 50))
        self.screen.blit(score_surf, score_rect)

        if self.game.game_over:
            hs_surf = self.font.render(f"High Score: {self.high_score}", True, (255, 255, 0))
            hs_rect = hs_surf.get_rect(center=(self.settings.screen_width // 2, 120))
            self.screen.blit(hs_surf, hs_rect)
