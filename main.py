import pygame
import random
from game import Game
from snake import Snake

def main():
    snake = Snake(15)
    game = Game(snake)
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
        if Timer % 10 == 0:
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
