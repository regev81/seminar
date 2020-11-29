from GameCaretaker import *
from GameMemento import *
from Model import *
from Player import *
from View2 import *

class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.care_taker = None

    def main(self):
        self.view.main()

    def new_game_clicked(self):
        self.view.create_new_game_page()
        self.model.player1 = Player("yakov",SHAPE_CIRCLE,COLOR_RED,SIZE_MEDIUM)
        self.model.player1 = Player("MON", SHAPE_CIRCLE, COLOR_BLACK, SIZE_MEDIUM)

    def start_game_clicked(self):
        self.model.start_new_game()
        self.view.create_board_game_page(self.model.game_data_grid)

    def cell_clicked(self,event):
        if canvas.find_withtag(CURRENT):
            tag = canvas.itemcget(CURRENT, "tags")
            row_column = re.split(',| ', tag)
            #row_column = tag.split(sep=',')
            row = int(row_column[0])
            column = int(row_column[1])
            cells_grid[row,column] = cells_grid[0,0]
            redraw(event)
        print(f"cell {row},{col} was clicked")

        self.model.move(row, col)
        self.care_taker.add_memento(GameMemento(self.model.game_data_grid))
        self.view.create_board_game_page()
        #self.update_grid()
        #self.update_message()
        #self.update_redo_undo_buttons()