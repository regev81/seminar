from GameCaretaker import *
from GameMemento import *
from Model import *
from View import *

class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.care_taker = None

    def main(self):
        self.view.main()

    # activated when game button clicked
    def grid_clicked(self,row,col):
        print(f"cell {row},{col} was clicked")

        self.model.move(row, col)
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))
        self.update_grid()
        self.update_message()
        self.update_redo_undo_buttons()


    # activated when redo button clicked
    def redo_clicked(self):
        print("redo_clicked")
        memento = self.care_taker.redo()
        if memento != None:
            self.model.update_grid_by_memento(memento)
        self.update_grid()
        self.update_message()

    # activated when undo button clicked
    def undo_clicked(self):
        print("undo_clicked")
        memento = self.care_taker.undo()
        if memento != None:
            self.model.update_grid_by_memento(memento)
        self.update_grid()
        self.update_message()

    # activated when new game button clicked
    def new_game_clicked(self):
        print("new_game")
        self.view.enable_grid_buttons()
        self.model.new_game()
        self.update_grid()
        self.update_message()
        self.update_redo_undo_buttons()

        # create GameCaretaker and first memento
        self.care_taker = GameCaretaker()
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))

    # update the view game board by the model game grid
    def update_grid(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.model.game_data_grid[row][col] == PLAYER1:
                      self.view.game_symbols_grid[row][col].set(PLAYER1_SYMBOL)
                      self.view.game_buttons_grid[row][col].config(bg=PLAYER1_COLOR)
                      self.view.game_buttons_grid[row][col].config(state="disabled")
                elif self.model.game_data_grid[row][col] == PLAYER2:
                    self.view.game_symbols_grid[row][col].set(PLAYER2_SYMBOL)
                    self.view.game_buttons_grid[row][col].config(bg=PLAYER2_COLOR)
                    self.view.game_buttons_grid[row][col].config(state="disabled")
                else:
                    self.view.game_symbols_grid[row][col].set(EMPTY_SYMBOL)
                    self.view.game_buttons_grid[row][col].config(bg="SystemButtonFace")
                    self.view.game_buttons_grid[row][col].config(state="active")
                    if self.model.game_state != GAME_STATE_ACTIVE:
                        self.view.game_buttons_grid[row][col].config(state="disabled")

    # update the state of the redo and undo buttons by the game state
    def update_redo_undo_buttons(self):
        if self.model.game_state != GAME_STATE_ACTIVE:
            self.view.redo_button.config(state="disabled")
            self.view.undo_button.config(state="disabled")
        else:
            self.view.redo_button.config(state="active")
            self.view.undo_button.config(state="active")

    # update the message to the user by the game state and result
    def update_message(self):
        # game over
        if self.model.game_state == GAME_STATE_OVER:
            if self.model.game_result == GAME_RESULT_DRAW:
                message = "Game over, it is a draw"
            elif self.model.game_result == GAME_RESULT_WIN_PLAYER1:
                message = "PLAYER1 is the winner !!!"
            else:
                message = "PLAYER2 is the winner !!!"
        # game continue
        else:
            message = f"{self.model.turn} turn..."

        self.view.message.set(message)

