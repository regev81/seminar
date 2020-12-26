from new.Constants import *
from new.FileHandler import FileHandler


class Model:

    def __init__(self):
        self.game_state = GameState.INACTIVE
        self.turn = None
        self.game_result = None
        self.game_data_grid = {}
        self.player1 = None
        self.player2 = None
        self.game_board_message = None

    # start a new game
    def start_new_game(self):
        self.init_board()
        self.turn = self.player1
        self.game_board_message = f"{self.turn.name} turn..."
        self.game_state = GameState.ACTIVE
        self.game_result = ""

    # initialize empty board
    def init_board(self):
        for row in range(ROWS):
            for column in range(COLS):
                self.game_data_grid[row, column] = None

    # return true if no step is available (all board cells have been chosen)
    def is_full(self):

        for key,  value in self.game_data_grid.items():
            for col in range(COLS):
                if value:
                    return False
        return True

    # return true if the player is the winner
    def is_winner(self, player):
        player_count = 0
        # check rows
        for row in range(ROWS):
            for col in range(COLS):
                if self.game_data_grid[row, col] == player:
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
                if self.game_data_grid[row, col] == player:
                    player_count += 1
                else:
                    continue
            if player_count == 3:
                return True
            else:
                player_count = 0

        # diagonal
        if (self.game_data_grid[0, 0] == player and self.game_data_grid[1,1] == player and self.game_data_grid[2,
            2] == player) or (
                self.game_data_grid[0, 2] == player and self.game_data_grid[1, 1] == player and self.game_data_grid[2,
            0] == player):
            return True

        return False

    def move(self, row, col):

        # check if move is legal
        if self.game_data_grid[row, col] is not None:
            return

        # update board
        self.game_data_grid[row, col] = self.turn

        # check end game
        self.update_game_state()
        if self.game_state == GameState.ACTIVE:
            # update turn
            self.switch_player()

    def update_game_state(self):
        if self.is_winner(self.player1):
            self.game_state = GameState.OVER
            self.game_result = GameResult.PLAYER1_WIN
            self.game_board_message = f"{self.player1.name} is the winner !!"
        elif self.is_winner(self.player2):
            self.game_state = GameState.OVER
            self.game_result = GameResult.PLAYER2_WIN
            self.game_board_message = f"{self.player2.name} is the winner !!"
        elif self.is_full():
            self.game_state = GameState.OVER
            self.game_result = GameResult.DRAW
            self.game_board_message = f"It is a draw"
        else:
            self.game_state = GameState.ACTIVE

    def switch_player(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1
        self.game_board_message = f"{self.turn.name} turn..."

    # change the game_data_grid by the memento game_data_grid
    def update_grid_by_memento(self,memento):
        for key, value in memento.game_data_grid.items():
            self.game_data_grid[key] = value

    def check_new_user_name(self,user_name):
        if FileHandler.user_name_exists_in_file(user_name):
            return InsertNewUserResulr.INSERT_NEW_USER_RESULT_USER_EXISTS
        else:
            return InsertNewUserResulr.INSERT_NEW_USER_RESULT_INVALID

