import random

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

        # defining next move / snake head position
        self.next_move = self.move()
        self.next_head_pos = [self.head_pos[0] + self.next_move[0], self.head_pos[1] + self.next_move[1]]
        
        # checking if move is allowed/ if not it is gameover
        if 0 <= self.next_head_pos[0] < self.board_size and 0 <= self.next_head_pos[1] < self.board_size:
            if self.board[self.next_head_pos[0]][self.next_head_pos[1]] > 0:
                self.GameOver()
        else:
            self.GameOver()
        
        # checking if apple has been taken
        if self.next_head_pos == self.apple_pos:
            self.score += 1
            self.length += 1
            self.apple_eaten = True

        # updating every tile of the board
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] not in [0, -1]:
                    self.board[x][y] += 1
                if (x == self.head_pos[0] + self.next_move[0] and y == self.head_pos[1] + self.next_move[1]):
                    self.board[x][y] = 1
                if self.board[x][y] > self.length:
                    self.board[x][y] = 0

        # spawning new_apple
        if self.apple_eaten == True:
            self.random_apple()
            self.apple_eaten = False

    def GameOver(self):
        self.gameover = True

    def restart(self):
        Snake = Snake(self.board_size)