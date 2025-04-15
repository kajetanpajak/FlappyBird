
class Settings:
    """Class to manage game's settings."""
    def __init__(self):
        """Initialize all settings"""
        self.screen_width = 1012
        self.screen_height = 900

        # BIRB
        self.bird_speed = 3
        self.gravity = 0.5
        self.jump_force = -4.5
        self.jump_duration = 0.2

        # PIPE
        self.pipe_gap = 230
        
        self.pipe_interval = 3
        