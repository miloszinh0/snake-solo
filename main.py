import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

class Game:
    def __init__(self, length):
        self.length = length
        self.board = np.zeros((length, length))
        self.snake_head = 1
        self.snake_length = 2
        self.apple = -1
        self.board[5, 5] = 1
        self.board[5, 6] = 2
        self.direction = 4
        self.points = 0
        self.next_head_pos = [99, 99]
        self.apple_pos = [88,88]
        """ 
         1        
        4 2
         3
        """
    def move(self):
        if self.direction == 1:
            return [-1, 0]
        elif self.direction == 2:
            return [0, 1]
        elif self.direction == 3:
            return [1, 0]
        elif self.direction == 4:
            return [0, -1]
    def random_apple(self):
        x = random.randint(0, self.length)
        y = random.randint(0, self.length)
        if self.board[x, y] == 0:
            self.board[x, y] = self.apple
        else:
            self.random_apple()
        



    def update(self):

        if self.next_head_pos[0] == self.apple_pos[0] and self.next_head_pos[1] == self.apple_pos[1]:
            self.points += 1
            self.random_apple()
        
        self.head_next_move = self.move()
        
        for x in range(self.length):
            for y in range(self.length):
                if self.board[x, y] == 1:
                    self.head_pos = [x, y]
                if self.board[x, y] > 0:
                    self.board[x, y] += 1
                if self.board[x, y] > self.snake_length:
                    self.board[x, y] = 0
                if self.board[x, y] == -1:
                    self.apple_pos = [x, y]
        
        self.next_head_pos = [self.head_pos[0]+self.head_next_move[0], self.head_pos[1]+self.head_next_move[1]]
        for x in self.next_head_pos:
            if not 0 <= x <= self.length-1:
                self.run = False
            else:
                self.board[self.next_head_pos[0], self.next_head_pos[1]] = 1
        return self.board

    def printboard(self):
        print(self.board)

    def GameOver(self):
        print("Game over dziwko")

    def console_anim(self):
        self.run = True
        self.random_apple()
    
        while self.run:
            self.printboard()
            self.update()
            self.plot_anim()
            
    
        self.GameOver()

    def plot_anim(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        fig.clear()
        ax = ax.pcolormesh(self.board)
        plt.show()
        time.sleep(1)
        


game = Game(10)
game.plot_anim()
        
    # def display(self):
    #     self.fig = plt.figure()
    #     ax = self.fig.add_subplot(1, 1, 1, aspect="equal")
    #     ax.set_xlim(0, self.length)
    #     ax.set_ylim(0, self.length)
    #     self.ani = animation.FuncAnimation(self.fig, self.update(),interval=1000)
    #     plt.show()

        

# class Displayer:
#     def __init__(self, game):
#         self.fig = plt.figure()
#         self.fig.suptitle('SNAKE GAME', y=0.9, fontsize=50)
#         self.game = game
#         self.board = self.game.board
#         self.ani = None

#     @staticmethod
#     def __animate(i, ax, game):
#         cells = list()

#         for rows in game.board:
#             for cell in rows:
#                 if cell > 0:
#                     cells.append(1)
#                 elif cell < 0:
#                     cells.append(2)
#                 else:
#                     cells.append(0)

#         ax.clear()
#         data = np.rot90(np.array(cells).reshape(game.length, game.length))
#         c = ax.pcolormesh(data, shading='flat')

#         game.update()
    
#     def display_board(self):
#         self.fig.clear()
#         self.fig.canvas.manager.full_screen_toggle()
#         ax = self.fig.add_subplot(1, 1, 1, aspect="equal")
#         ax.set_xlim(0, self.game.length)
#         ax.set_ylim(0, self.game.length)
#         self.fig.suptitle("")

#         self.ani = animation.FuncAnimation(self.fig, Displayer.__animate, fargs=(ax, self.board),
#                                       interval=100)

#         # slider_axes = plt.axes([0.95, 0.3, 0.03, 0.4])
#         # slider = Slider(slider_axes, 'interval', 1, 1000, orientation='vertical', valinit=100)
#         # slider.on_changed(self.__set_anim_speed)

#         # exit_axes = plt.axes([0.95, 0.9, 0.03, 0.05])
#         # exit_button = Button(exit_axes, 'X')
#         # exit_button.on_clicked(self.__exit)
#         plt.show()


# game = Game(10)
# displayer = Displayer(game)
# displayer.display_board()