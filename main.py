import numpy as np
import matplotlib.pyplot as plt

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
    

    def update(self):
        self.head_next_move = self.move()
        
        for x in range(self.length):
            for y in range(self.length):
                if self.board[x, y] == 1:
                    self.head_pos = [x, y]
                if self.board[x, y] > 0:
                    self.board[x, y] += 1
                if self.board[x, y] > self.snake_length:
                    self.board[x, y] = 0
        self.next_head_pos = [self.head_pos[0]+self.head_next_move[0], self.head_pos[1]+self.head_next_move[1]]
        self.board[self.next_head_pos[0], self.next_head_pos[1]] = 1
        




game = Game(10)
game.update()
game.update()
print(game.board)
