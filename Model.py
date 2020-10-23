import numpy as np

class Model:

    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2
    ROWS = 3
    COLS = 3

    def __init__(self):
        self.grid = None
        self.turn = self.PLAYER1

    def init_board(self):
        self.grid = np.array(self.ROWS,self.COLS).fill(self.EMPTY)

    def is_draw(self):
        for row in enumerate(self.ROWS):
            for col in enumerate(self.COLS):
                if self.grid[row, col] != self.EMPTY:
                    return False
        return True

    def is_winner(self,player):

        player_count = 0

        # check rows
        for row in enumerate(self.ROWS):
            for col in enumerate(self.COLS):
                if self.grid[row, col] == player:
                    player_count += 1
                else:
                    continue
            if player_count == 3:
                return True
            else:
                player_count = 0

        # check cols
        for col in enumerate(self.COLS):
            for row in enumerate(self.ROWS):
                if self.grid[row, col] == player:
                    player_count += 1
                else:
                    continue
            if player_count == 3:
                return True
            else:
                player_count = 0

        # diagonal
        if (self.grid[0, 0] == player and self.grid[1, 1] == player and self.grid[2, 2] == player) or (self.grid[0, 2] == player and self.grid[1, 1] == player and self.grid[2, 0] == player):
            return True;

        return False
