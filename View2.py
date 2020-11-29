import tkinter as tk

from Constants import *


class View:

    def __init__(self,controller):
        self.controller = controller
        self.start_page = None
        self.new_game_page = None
        self.game_board_page = None
        self.add_user_page = None

    def main(self):
        self.create_start_page()

    # create the start page menu
    def create_start_page(self):
        height = 400
        width = 300
        root = tk.Tk()
        root.title("Tic Tac Toe Menu")
        self.start_page = tk.Canvas(root, height=height, width=width)
        self.start_page.pack()

        # buttons
        button1 = tk.Button(self.start_page, text="New Game", command=self.controller.new_game_clicked)
        button1.pack()

        root.mainloop()

    # create the new game window (where the players choose their shapes)
    def create_new_game_page(self):
        height = 700
        width = 700
        root = tk.Tk()
        self.new_game_page = tk.Canvas(root, height=height, width=width)
        self.new_game_page.pack()

        # start game button
        button1 = tk.Button(self.new_game_page, text="Start Game", command=self.controller.start_game_clicked)
        button1.pack()

    # create the new board game window
    def create_board_game_page(self,game_data_grid):
        height = 700
        width = 700
        root = tk.Tk()
        self.game_board_page = tk.Canvas(root, height=height, width=width)
        self.game_board_page.pack(fill=tk.BOTH, expand=tk.YES)
        self.game_board_page.delete("all")
        size = 3
        cellwidth = int(self.game_board_page.winfo_width() / size)
        cellheight = int(self.game_board_page.winfo_height() / size)
        for column in range(size):
            for row in range(size):
                x1 = column * cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                cell = self.game_board_page.create_rectangle(x1, y1, x2, y2, fill="white", tags=f"{row},{column}")
                self.game_board_page.tag_bind(cell, '<ButtonPress-1>', self.controller.cell_clicked)
                #squers[row, column] = cell
                player = game_data_grid[row, column]
                if (player != None):
                    self.draw_shape(self.game_board_page, player, x1, y1, cellwidth, cellheight)


    def draw_shape(self,thecanvas, theplayer,cell_topleft_x,cell_topleft_y,cellwidth,cellheight):
        size_param = 1
        shape = theplayer.shape
        color = theplayer.color

        if theplayer.size == SIZE_LARGE:
            size_param = 1
        elif theplayer.size == SIZE_MEDIUM:
            size_param = 2
        else:
            size_param = 3

        x1 = cell_topleft_x + ((cellwidth/7)*size_param)
        y1 = cell_topleft_y + ((cellheight / 7) * size_param)
        x2 = cell_topleft_x + cellwidth - ((cellwidth/7)*size_param)
        y2 = cell_topleft_y + cellheight - ((cellheight/7)*size_param)
        if shape == SHAPE_RECTANGLE :
            thecanvas.create_rectangle(x1, y1, x2, y2, fill=color)
        elif shape == SHAPE_CIRCLE:
            thecanvas.create_oval(x1, y1, x2, y2, fill=color)
        else:
            points = [x1,y2,x2,y2,((x1+x2)/2),y1]
            thecanvas.create_polygon(points, fill=color)