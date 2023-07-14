import pygame
from snake import Snake
pygame.font.init()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 204, 0)
DARK_GREEN = (0, 153, 0)
RED = (204, 0, 0)

#FONTS
GAMEOVER_FONT = pygame.font.SysFont('comicsans', 150)
SCORE_FONT = pygame.font.SysFont('comicsans', 50)

class Game:
    def __init__(self, snake):
        self.snake = snake
        self.game_size = 800
        self.window_size = 1000
        self.WIN = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("Snake Game")

        self.FPS = 60


    def draw_window(self):
        self.WIN.fill(WHITE)
        for x in range(self.snake.board_size):
            for y in range(self.snake.board_size):
                if self.snake.board[x][y] == 0:
                    color = BLACK
                elif self.snake.board[x][y] == 1:
                    color = DARK_GREEN
                elif self.snake.board[x][y] == -1:
                    color = RED
                else:
                    color = GREEN
                rect = pygame.Rect((self.window_size-self.game_size)/2 + x * self.game_size/self.snake.board_size, (self.window_size-self.game_size)/2 + y * self.game_size/self.snake.board_size, self.game_size/self.snake.board_size, self.game_size/self.snake.board_size)
                pygame.draw.rect(self.WIN, color, rect)
        score_text = SCORE_FONT.render(f"SCORE: {self.snake.score}", 1, RED)
        self.WIN.blit(score_text, (self.window_size//2-score_text.get_width()/2, self.window_size/5))
        pygame.display.update()

    def draw_gameover(self):
        draw_text = GAMEOVER_FONT.render("GAME OVER", 1, RED)
        self.WIN.blit(draw_text, (self.window_size//2-draw_text.get_width()/2, self.window_size//2-draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)