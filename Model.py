import numpy as np

class Model:

    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2
    DRAW = 3
    CONTINUE_GAME = 4
    ROWS = 3
    COLS = 3


    def __init__(self):
        # matrix of int's of the game board
        self.grid = None

        self.turn = None

    # start a new game
    def new_game(self):
        # set the turn
        self.turn = self.PLAYER1
        self.new_game()

    # initialize empty board
    def init_board(self):
        self.grid = np.array(self.ROWS,self.COLS).fill(self.EMPTY)

    # return true if it is a draw
    def is_draw(self):
        for row in enumerate(self.ROWS):
            for col in enumerate(self.COLS):
                if self.grid[row, col] != self.EMPTY:
                    return False
        return True

    # return true if the player is the winner
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

    # update the grid matrix by the move of the
    # return the the player who should be in the cell (PLAYER1/PLAYER2/EMPTY)
    def move(self,row,col):
        if self.grid[row,col] == self.EMPTY:

            # update board
            self.grid[row, col] = self.turn

            # check end game
            game_state = self.check_end_game()
            if(game_state == self.CONTINUE_GAME):
                # update turn
                self.switch_player()

        return self.grid[row,col]


    # check if end of game and return the winner if needed
    def check_end_game(self):
        if self.is_draw():
            return self.DRAW
        elif self.is_winner(self.PLAYER1):
            return self.PLAYER1
        elif self.is_winner(self.PLAYER2):
            return self.PLAYER2

        return self.CONTINUE_GAME


    # switch player
    def switch_player(self):
        if(self.turn == self.PLAYER1):
            self.turn = self.PLAYER2
        else:
            self.turn = self.PLAYER1