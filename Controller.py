from GameCaretaker import *
from GameMemento import *
from Model import *
from Player import *
from View import *


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.care_taker = None

    def main(self):
        self.view.main()

    def new_game_clicked(self):
        # dont start new game if a previous game is still running
        if self.model.game_state == GameState.ACTIVE.value or self.model.game_state == GameState.CHOOSE_PLAYERS_DETAILS.value:
            return

        self.model.game_state = GameState.CHOOSE_PLAYERS_DETAILS.value
        userswins_from_file = FileHandler.get_all_users_and_wins()
        users_from_file = list(userswins_from_file.keys())
        self.view.create_new_game_page(users_from_file)

    def add_new_user_clicked(self):
        self.view.create_new_user_page()

    def generate_report_clicked(self):
        pass

    def start_game_clicked(self,root):
        # create player 1
        player1_name = self.view.player1_name_combo.get()
        player1_shape = self.view.player1_shape_combo.get()
        player1_color = self.view.player1_color_combo.get()
        player1_size = self.view.player1_size_combo.get()
        player1 = Player(player1_name,player1_shape,player1_color,player1_size)

        # create player 2
        player2_name = self.view.player2_name_combo.get()
        player2_shape = self.view.player2_shape_combo.get()
        player2_color = self.view.player2_color_combo.get()
        player2_size = self.view.player2_size_combo.get()
        player2 = Player(player2_name,player2_shape,player2_color,player2_size)

        # verify players
        players_valid_val = self.model.players_valid(player1,player2)
        if players_valid_val != "":
            self.view.show_error(players_valid_val)
            return

        root.destroy()
        self.model.player1 = player1
        self.model.player2 = player2

        # create GameCaretaker and first memento
        self.care_taker = GameCaretaker()
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))

        self.model.start_new_game()
        self.view.create_game_board_page(self.model.game_data_grid,self.model.game_board_message)

        # create GameCaretaker and first memento
        self.care_taker = GameCaretaker()
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))

    def on_resize(self,event):
        self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)

    def cell_clicked(self,event):
        if self.view.game_board_canvas.find_withtag(CURRENT) and self.model.game_state == GameState.ACTIVE.value:
            tag = self.view.game_board_canvas.itemcget(CURRENT, "tags")
            row_column = re.split(',| ', tag)
            # row_column = tag.split(sep=',')
            row = int(row_column[0])
            column = int(row_column[1])

            self.model.move(row,column)
            self.care_taker.add_memento(GameMemento(self.model.game_data_grid))
            self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)

    # activated when redo button clicked
    def redo_clicked(self):
        if self.model.game_state == GameState.ACTIVE.value:
            memento = self.care_taker.redo()
            if memento is not None:
                self.model.update_grid_by_memento(memento)
            self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)

    # activated when undo button clicked
    def undo_clicked(self):
        if self.model.game_state == GameState.ACTIVE.value:
            memento = self.care_taker.undo()
            if memento is not None:
                self.model.update_grid_by_memento(memento)
            self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)

    # insert new user to the file (if the user name is valid)
    def insert_new_user_clicked(self):
        name_entered = self.view.new_user_entry_str.get()
        if FileHandler.user_name_exists_in_file(name_entered):
            self.view.new_user_add_error_label_str.set(Error.USER_EXISTS.value)
        else:
            FileHandler.add_new_user_to_file(name_entered)
            self.view.new_user_add_error_label_str.set(f"User {name_entered} successfully added to file")