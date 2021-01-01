from Constants import *
from FileHandler import FileHandler


class Model:

    def __init__(self):
        self.game_state = GameState.INACTIVE.value
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
        self.game_state = GameState.ACTIVE.value
        self.game_result = ""

    # initialize empty board
    def init_board(self):
        for row in range(ROWS):
            for column in range(COLS):
                self.game_data_grid[row, column] = None

    # return true if no step is available (all board cells have been chosen)
    def is_full(self):

        for key, value in self.game_data_grid.items():
            if value is None:
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

    # perform step of a player
    def move(self, row, col):

        # check if move is legal
        if self.game_data_grid[row, col] is not None:
            return

        # update board
        self.game_data_grid[row, col] = self.turn

        # check end game
        self.update_game_state()
        if self.game_state == GameState.ACTIVE.value:
            # update turn
            self.switch_player()

    # activate steps when a player wins the game
    def activate_win_state(self,player):
        self.game_state = GameState.OVER.value
        if player.name == self.player1.name:
            self.game_result = GameResult.PLAYER1_WIN.value
        else:
            self.game_result = GameResult.PLAYER2_WIN.value

        self.game_board_message = f"{player.name} is the winner !!"
        FileHandler.add_win_to_user(player.name)

    # update the game state by the current state
    def update_game_state(self):
        if self.is_winner(self.player1):
            self.activate_win_state(self.player1)
        elif self.is_winner(self.player2):
            self.activate_win_state(self.player2)
        elif self.is_full():
            self.game_state = GameState.OVER.value
            self.game_result = GameResult.DRAW.value
            self.game_board_message = f"It is a draw"
        else:
            self.game_state = GameState.ACTIVE.value

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

    # return the correct error if the players are not valid.
    # return empty string if the players are valid
    def players_valid(self,player1,player2):
        if self.empty_attribute_exists(player1) or self.empty_attribute_exists(player2):
            return Error.EMPTY_ATTRIBUTE.value
        elif player1.name == player2.name:
            return Error.PLAYERS_SAME_NAME.value
        elif player1.shape == player2.shape and player1.color == player2.color and player1.size == player2.size:
            return Error.PLAYERS_SAME_ATTRIBUTES.value
        else:
            return ""

    # return true if player got an invalid attribute (empty string)
    def empty_attribute_exists(self,player):
        player_attributes = vars(player)
        for val in player_attributes.values():
            if(val == ""):
                return True

        return False


