import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from flappy_bird import FlappyBird

if __name__ == "__main__":
    game = FlappyBird()
    game.run_game()