from snake import Snake
from game import Game

if __name__ == "__main__":
    snake = Snake(16)
    game = Game(snake)
    game.main()