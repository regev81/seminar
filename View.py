import tkinter as tk
from tkinter import *
from Constants import *


class View(tk.Tk):

    def __init__(self,controller):
        super().__init__()
        self.controller = controller

        # create the UI
        main_frame = Frame(self)
        main_frame.pack(padx=10, pady=10)
        self.message = None
        self.game_buttons_grid = []
        self.game_symbols_grid = []
        self.redo_button = None
        self.undo_button = None

        self.create_message_pane(main_frame)
        self.create_grid_pane(main_frame)
        self.create_buttons_pane(main_frame)

    # create the top pane witch holds the message to the user
    def create_message_pane(self,main_frame):

        message_pane = Frame(main_frame)

        self.message = tk.StringVar()
        message_label = Label(message_pane, textvariable=self.message,
                                   background="white", fg="black")
        message_label.pack(fill=tk.X)
        message_pane.pack(side="top")

    # create the center pane witch holds the game board
    def create_grid_pane(self, main_frame):
        grid_frame = Frame(main_frame)
        for row in range(ROWS):
            button_row_arr = []
            symbol_row_arr = []
            for col in range(COLS):
                symbol = StringVar()
                b = Button(grid_frame, textvariable=symbol, font=("Helvetica", 20), height=3, width=6,
                           bg="SystemButtonFace",
                           command=lambda row1=row, col1=col: self.controller.grid_clicked(row1, col1))
                b.config(state="disabled")
                b.grid(row=row, column=col)
                button_row_arr.append(b)
                symbol_row_arr.append(symbol)
            self.game_buttons_grid.append(button_row_arr)
            self.game_symbols_grid.append(symbol_row_arr)

        grid_frame.pack(side="top")

    # create the bottom pane witch holds the new game, undo and redo buttons
    def create_buttons_pane(self,main_frame):
        bottom_frame = Frame(main_frame)
        new_game_button = Button(bottom_frame, text="New Game", command=lambda: self.controller.new_game_clicked())
        self.redo_button = Button(bottom_frame, text="Redo", command=lambda: self.controller.redo_clicked())
        self.redo_button.config(state="disabled")
        self.undo_button = Button(bottom_frame, text="Undo", command=lambda: self.controller.undo_clicked())
        self.undo_button.config(state="disabled")
        new_game_button.pack(side="left", fill=tk.X)
        self.redo_button.pack(side="left", fill=tk.X)
        self.undo_button.pack(side="left", fill=tk.X)
        bottom_frame.pack(side="top")

    def main(self):
        self.mainloop()

    # make all the game buttons clickable
    def enable_grid_buttons(self):
        for row in range(ROWS):
            for col in range(COLS):
               self.game_buttons_grid[row][col].config(state="normal")

    # make all the game buttons un-clickable
    def disable_grid_buttons(self):
        for row in range(ROWS):
            for col in range(COLS):
               self.game_buttons_grid[row][col].config(state="disabled")