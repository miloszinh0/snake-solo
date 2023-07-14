import pygame
import random
pygame.font.init()
# WIDTH, HEIGHT = 1000, 1000
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snake Game")

# FPS = 8

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 204, 0)
DARK_GREEN = (0, 153, 0)
RED = (204, 0, 0)

GAMEOVER_FONT = pygame.font.SysFont('comicsans', 150)
SCORE_FONT = pygame.font.SysFont('comicsans', 50)



class Snake:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.head = 1
        self.length = 2
        self.apple = -1
        self.board[round(board_size/4)][round(board_size/4)] = self.head
        self.head_pos = [round(board_size/4), round(board_size/4)]
        self.board[round(board_size/4)-1][round(board_size/4)] = 2
        self.board[round(board_size/2)][round(board_size/2)] = -1
        self.apple_pos = [round(board_size/2), round(board_size/2)]
        self.direction = 3
        self.score = 0
        self.apple_eaten = False
        self.gameover = False

    def move(self):
        if self.direction == 1:
            return [-1, 0]
        elif self.direction == 2:
            return [0, 1]
        elif self.direction == 3:
            return [1, 0]
        elif self.direction == 0:
            return [0, -1]

    def random_apple(self):
        x = random.randint(0, self.board_size - 1)
        y = random.randint(0, self.board_size - 1)
        if self.board[x][y] == 0:
            self.board[x][y] = self.apple
            self.apple_pos = [x, y]
        else:
            self.random_apple()

    def update(self):
        self.next_move = self.move()
        self.next_head_pos = [self.head_pos[0] + self.next_move[0], self.head_pos[1] + self.next_move[1]]

        if 0 <= self.next_head_pos[0] < self.board_size and 0 <= self.next_head_pos[1] < self.board_size:
            if self.length > self.board[self.next_head_pos[0]][self.next_head_pos[1]] > 0:
                self.GameOver()
        else:
            self.GameOver()

        if self.next_head_pos == self.apple_pos:
            self.score += 1
            self.length += 1
            self.apple_eaten = True

        for x in range(self.board_size):
            for y in range(self.board_size):
                tile = self.board[x][y]
                if self.board[x][y] not in [0, -1]:
                    self.board[x][y] += 1
                if (x == self.head_pos[0] + self.next_move[0] and y == self.head_pos[1] + self.next_move[1]):
                    self.board[x][y] = 1
                if self.board[x][y] > self.length:
                    self.board[x][y] = 0
            
        self.head_pos = [self.head_pos[0] + self.next_move[0], self.head_pos[1] + self.next_move[1]]

        if self.apple_eaten == True:
            self.random_apple()
            self.apple_eaten = False

    def GameOver(self):
        self.gameover = True
        print("GameOver")

    def restart(self):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.head = 1
        self.length = 2
        self.apple = -1
        self.board[round(board_size/4)][round(board_size/4)] = self.head
        self.head_pos = [round(board_size/4), round(board_size/4)]
        self.board[round(board_size/4)-1][round(board_size/4)] = 2
        self.board[round(board_size/2)][round(board_size/2)] = -1
        self.apple_pos = [round(board_size/2), round(board_size/2)]
        self.direction = 3
        self.score = 0
        self.apple_eaten = False
        self.gameover = False
        
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
        pygame.time.delay(2000)

    def draw_start_menu(self):
        draw_text = GAMEOVER_FONT.render("SNAKE_GAME", 1, RED)
        self.WIN.blit(draw_text, (self.window_size//2-draw_text.get_width()/2, self.window_size//2-draw_text.get_height()/2))
def main():
    snake = Snake(20)
    game = Game(snake)
    game_state = "menu"
    clock = pygame.time.Clock()
    run = True
    Timer = 0
    pressed = False
    right_pressed = False
    left_pressed = False
    while run:
        clock.tick(game.FPS)
        keys_pressed = pygame.key.get_pressed()
        if pressed == False:
            if keys_pressed[pygame.K_RIGHT]:
                if not right_pressed:
                    game.snake.direction -= 1
                    pressed = True
                    right_pressed = True
            else:
                right_pressed = False

            if keys_pressed[pygame.K_LEFT]:
                if not left_pressed:
                    game.snake.direction += 1
                    pressed = True
                    left_pressed = True
            else:
                left_pressed = False
            game.snake.direction = game.snake.direction % 4
        Timer += 1
        if Timer % 7 == 0 and game_state == "game":
            Timer = 0
            game.snake.update()
            game.draw_window()
            pressed = False
            if game.snake.gameover == True:
                game.draw_gameover()
                main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()

if __name__ == "__main__":
    main()
