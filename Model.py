from Constants import *


class Model:

    def __init__(self):
        self.game_state = GAME_STATE_INACTIVE
        self.turn = None
        self.game_result = None
        self.game_data_grid = None

        # initialize empty board
    def init_board(self):
        self.game_data_grid = []
        for row in range(ROWS):
            row_arr = []
            for col in range(COLS):
                row_arr.append(EMPTY_SYMBOL)
            self.game_data_grid.append(row_arr)

    # return true if no step is available (all board cells have been chosen)
    def is_full(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.game_data_grid[row][col] == EMPTY_SYMBOL:
                    return False
        return True

    # return true if the player is the winner
    def is_winner(self,player):

        player_count = 0

        # check rows
        for row in range(ROWS):
            for col in range(COLS):
                if self.game_data_grid[row][col] == player:
                    player_count += 1
                else:
                    continue
            if player_count == 3:
                return True
            else:
                player_count = 0

        # check cols
        for col in range(COLS):
            for row in range(ROWS):
                if self.game_data_grid[row][col] == player:
                    player_count += 1
                else:
                    continue
            if player_count == 3:
                return True
            else:
                player_count = 0

        # diagonal
        if (self.game_data_grid[0][0] == player and self.game_data_grid[1][1] == player and self.game_data_grid[2][2] == player) or (self.game_data_grid[0][2] == player and self.game_data_grid[1][1] == player and self.game_data_grid[2][0] == player):
            return True

        return False

    def move(self,row,col):

        # update board
        self.game_data_grid[row][col] = self.turn

        # check end game
        self.update_game_state()
        if self.game_state == GAME_STATE_ACTIVE:
            # update turn
            self.switch_player()

    # check if end of game and return the winner if needed
    def update_game_state(self):
        if self.is_winner(PLAYER1):
            self.game_state = GAME_STATE_OVER
            self.game_result = GAME_RESULT_WIN_PLAYER1
        elif self.is_winner(PLAYER2):
            self.game_state = GAME_STATE_OVER
            self.game_result = GAME_RESULT_WIN_PLAYER2
        elif self.is_full():
            self.game_state = GAME_STATE_OVER
            self.game_result = GAME_RESULT_DRAW
        else:
            self.game_state = GAME_STATE_ACTIVE

    def switch_player(self):
        if self.turn == PLAYER1:
            self.turn = PLAYER2
        else:
            self.turn = PLAYER1

    # init new game parameters
    def new_game(self):
        self.init_board()
        self.turn = PLAYER1
        self.game_state = GAME_STATE_ACTIVE
        self.game_result = ""

    # change the game_data_grid by the memento game_data_grid
    def update_grid_by_memento(self,memento):
        for row in range(ROWS):
            for col in range(COLS):
                self.game_data_grid[row][col] = memento.game_data_grid[row][col]

