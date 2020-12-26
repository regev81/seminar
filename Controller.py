from FileHandler import FileHandler
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
        self.view.create_new_game_page()

        # create GameCaretaker and first memento
        self.care_taker = GameCaretaker()
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))

        # for testing
        self.model.player1 = Player("tal",Shape.TRIANGLE,Color.RED,Size.MEDIUM)
        self.model.player2 = Player("talya", Shape.CIRCLE,Color.BLUE,Size.LARGE)

    def add_new_user_clicked(self):
        self.view.create_new_user_page()

    def generate_report_clicked(self):
        pass

    def start_game_clicked(self):
        self.model.start_new_game()
        self.view.create_game_board_page(self.model.game_data_grid,self.model.game_board_message)

        # create GameCaretaker and first memento
        self.care_taker = GameCaretaker()
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))

    def on_resize(self,event):
        self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)
        print(f"resize occurred")

    def cell_clicked(self,event):
        if self.view.game_board_canvas.find_withtag(CURRENT) and self.model.game_state.value == GameState.ACTIVE.value:
            tag = self.view.game_board_canvas.itemcget(CURRENT, "tags")
            row_column = re.split(',| ', tag)
            # row_column = tag.split(sep=',')
            row = int(row_column[0])
            column = int(row_column[1])

            self.model.move(row,column)
            self.care_taker.add_memento(GameMemento(self.model.game_data_grid))
            self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)
            print(f"cell {row},{column} was clicked")

    # activated when redo button clicked
    def redo_clicked(self):
        print("redo_clicked")
        if(self.model.game_state.value == GameState.ACTIVE.value):
            memento = self.care_taker.redo()
            if memento != None:
                self.model.update_grid_by_memento(memento)
            self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)

    # activated when undo button clicked
    def undo_clicked(self):
        print("undo_clicked")
        if (self.model.game_state.value == GameState.ACTIVE.value):
            memento = self.care_taker.undo()
            if memento != None:
                self.model.update_grid_by_memento(memento)
            self.view.redraw_game_board(self.model.game_data_grid,self.model.game_board_message)

    def insert_new_user_clicked(self):
        name_entered = self.view.new_user_entry_str.get()
        insert_user_result = self.model.check_new_user_name(name_entered)
        message = None
        if insert_user_result == InsertNewUserResulr.INSERT_NEW_USER_RESULT_INVALID:
            message = f"Invalid name !!"
        elif insert_user_result == InsertNewUserResulr.INSERT_NEW_USER_RESULT_USER_EXISTS:
            message = f"User {name_entered} exists, choose a different name"
        else:
            message = f"User {name_entered} was added successfully"
            FileHandler.add_new_user_to_file(name_entered)

        self.view.new_user_add_error_label_str.set(message)

