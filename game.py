import pygame

#FONTS
pygame.font.init()

GAMEOVER_FONT = pygame.font.SysFont('comicsans', 150)
SCORE_FONT = pygame.font.SysFont('comicsans', 50)
SNAKE_FONT = pygame.font.SysFont('comicsans', 120)
TEXT1_FONT = pygame.font.SysFont('comicsans', 70)
TEXT2_FONT = pygame.font.SysFont('comicsans', 40)

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 153, 0)
RED = (204, 0, 0)

class Game:
    def __init__(self, snake):

        self.snake = snake

        self.game_size = 800
        self.window_size = 1000

        self.WIN = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("Snake Game")
        self.FPS = 60

        self.Timer = 0

        self.pressed = False
        self.right_pressed = False
        self.left_pressed = False


    def draw_window(self):
        if self.state == 0:
            self.draw_start_menu()
        elif self.state == 1:
            self.draw_game()
        elif self.state == 2:
            self.draw_gameover_menu()
        pygame.display.update()

    def draw_game(self):
        self.snake.update()
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
        self.draw_score()
        if self.snake.gameover == True:
            self.state = 2
            

    def draw_score(self):
        score_text = SCORE_FONT.render(f"SCORE: {self.snake.score}", 1, RED)
        self.WIN.blit(score_text, (self.window_size//2-score_text.get_width()/2, self.window_size/5))

    def draw_gameover(self):
        draw_text = GAMEOVER_FONT.render("GAME OVER", 1, RED)
        self.WIN.blit(draw_text, (self.window_size//2-draw_text.get_width()/2, self.window_size//2-draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)

    def draw_start_menu(self):
        self.WIN.fill(BLACK)
        draw_text = SNAKE_FONT.render("SNAKE GAME", 1, GREEN)
        self.WIN.blit(draw_text, (self.window_size//2-draw_text.get_width()/2, (self.window_size//2-draw_text.get_height()/2)/1.2))
        if self.seen:
            draw_text2 = TEXT1_FONT.render("To Start Press \'Space\'", 1, WHITE)
            self.WIN.blit(draw_text2, (self.window_size//2-draw_text2.get_width()/2, (self.window_size//2-draw_text2.get_height()/2)/0.8))
        else:
            draw_text2 = TEXT1_FONT.render("To Start Press \'Space\'", 1, RED)
            self.WIN.blit(draw_text2, (self.window_size//2-draw_text2.get_width()/2, (self.window_size//2-draw_text2.get_height()/2)/0.8))   
        draw_text3 = TEXT2_FONT.render("Miłosz Foltyn", 1, RED)
        self.WIN.blit(draw_text3, (self.window_size//2-draw_text3.get_width()/2, (self.window_size//2-draw_text3.get_height()/2)/9))
        pygame.display.update()

    def draw_gameover_menu(self):
        self.WIN.fill(BLACK)
        draw_text = SNAKE_FONT.render("SNAKE GAME", 1, GREEN)
        self.WIN.blit(draw_text, (self.window_size//2-draw_text.get_width()/2, (self.window_size//2-draw_text.get_height()/2)/1.2))
        if self.seen:
            draw_text2 = TEXT1_FONT.render("To Start Press \'Space\'", 1, WHITE)
            self.WIN.blit(draw_text2, (self.window_size//2-draw_text2.get_width()/2, (self.window_size//2-draw_text2.get_height()/2)/0.8))
        draw_text3 = TEXT2_FONT.render("Miłosz Foltyn", 1, RED)
        self.WIN.blit(draw_text3, (self.window_size//2-draw_text3.get_width()/2, (self.window_size//2-draw_text3.get_height()/2)/9))
        score_text = SNAKE_FONT.render(f"{self.snake.score}", 1, RED)
        self.WIN.blit(score_text, (self.window_size//2-score_text.get_width()/2, self.window_size/6))
        pygame.display.update()


    def user_game_input(self):
        self.keys_pressed = pygame.key.get_pressed()

        if self.pressed == False:

            if self.keys_pressed[pygame.K_RIGHT]:
                if not self.right_pressed:
                    self.snake.direction -= 1
                    self.pressed = True
                    self.right_pressed = True
            else:
                self.right_pressed = False

            if self.keys_pressed[pygame.K_LEFT]:
                if not self.left_pressed:
                    self.snake.direction += 1
                    self.pressed = True
                    self.left_pressed = True
            else:
                self.left_pressed = False

            self.snake.direction = self.snake.direction % 4

    def start_menu_input(self):
        self.keys_pressed = pygame.key.get_pressed()
        if self.keys_pressed[pygame.K_SPACE]:
            self.state = 1
            self.snake.restart()
    

    def state_input(self):
        if self.state == 0:
            self.start_menu_input()
        elif self.state == 1:
            self.user_game_input()
        elif self.state == 2:
            self.start_menu_input()

    def main(self):
        clock = pygame.time.Clock()
        run = True
        self.state = 0
        self.seen = True
        while run:
            clock.tick(self.FPS)
            self.state_input()
            self.Timer += 1
            
            if self.Timer % 10 == 0:
                # self.Timer = 0
                self.draw_window()
                self.pressed = False
                print(self.seen)
            if self.Timer % self.FPS*3 == self.FPS/2:
                self.seen = False
                # print(self.seen)
            elif self.Timer % self.FPS*3 == self.FPS:
                self.seen = True
                # print(self.seen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()