from tkinter import *
from Constants import *


class View:

    def __init__(self,controller):
        self.controller = controller
        self.start_page = None
        self.new_game_page = None
        self.game_board_canvas = None
        self.add_user_page = None
        self.game_board_message = None

    def main(self):
        self.create_start_page()

    def create_start_page(self):
        height = 500
        width = 500
        root = Tk()
        root.title("Tic Tac Toe Menu")
        self.start_page = Frame(root, height=height, width=width)
        self.start_page.pack()

        # buttons
        new_game_but = Button(self.start_page, text="New Game", command=self.controller.new_game_clicked)
        new_game_but.pack()

        add_user_but = Button(self.start_page, text="Add User", command=self.controller.add_user_clicked)
        add_user_but.pack()

        generate_report_but = Button(self.start_page, text="Generate Report", command=self.controller.generate_report_clicked)
        generate_report_but.pack()

        root.mainloop()

    def create_new_game_page(self):
        height = 600
        width = 400
        root = Toplevel()
        root.title("New Game")
        self.new_game_page = Frame(root, height=height, width=width)
        self.new_game_page.pack()

        '''
         add gui for new_game_page
        '''

        # start game button
        start_game_but = Button(self.new_game_page, text="Start Game", command=self.controller.start_game_clicked)
        start_game_but.pack()

    def create_game_board_page(self,game_data_grid,text_message):
        root = Toplevel()
        root.title("Game Board")

        # top message label
        self.game_board_message = StringVar()
        message_label = Label(root, textvariable= self.game_board_message)
        message_label.pack(expand=TRUE,fill=BOTH)

        # grid canvas
        #self.game_board_canvas = Canvas(root, height=canvas_height, width=canvas_width)
        self.game_board_canvas = Canvas(root)
        self.game_board_canvas.bind("<Configure>", self.controller.on_resize)
        self.game_board_canvas.pack(expand=TRUE, fill=BOTH)

        # redo undo buttons
        undo_button = Button(root, text="undo",command = self.controller.undo_clicked)
        undo_button.pack(expand=TRUE, fill=BOTH,side = LEFT)
        redo_button = Button(root, text="redo",command = self.controller.redo_clicked)
        redo_button.pack(expand=TRUE, fill=BOTH, side=LEFT)

        self.redraw_game_board(game_data_grid,text_message)

    # redraw the game board by the game data grid
    def redraw_game_board(self, game_data_grid, text_message):
        #self.game_board_canvas.delete("all")

        # update message
        self.game_board_message.set(text_message)

        # get game board page canvas height and width
        canvas_width = self.game_board_canvas.winfo_width()
        canvas_height = self.game_board_canvas.winfo_height()

        # create the grid game board on canvas
        grid_size = 3
        cellwidth = int(canvas_width / grid_size)
        cellheight = int(canvas_height / grid_size)
        for column in range(grid_size):
            for row in range(grid_size):
                x1 = column * cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                cell = self.game_board_canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags=f"{row},{column}")
                self.game_board_canvas.tag_bind(cell, '<ButtonPress-1>', self.controller.cell_clicked)
                player = game_data_grid[row,column]

                # create the shape inside the grid cell if necessary
                if(player != None):
                    self.draw_shape(player,x1,y1,cellwidth,cellheight)

    def draw_shape(self, the_player, cell_topleft_x, cell_topleft_y, cell_width, cell_height):

        shape = the_player.shape
        color = the_player.color

        if the_player.size == SIZE_LARGE:
            size_param = 1
        elif the_player.size == SIZE_MEDIUM:
            size_param = 2
        else:
            size_param = 3

        x1 = cell_topleft_x + ((cell_width / 7) * size_param)
        y1 = cell_topleft_y + ((cell_height / 7) * size_param)
        x2 = cell_topleft_x + cell_width - ((cell_width / 7) * size_param)
        y2 = cell_topleft_y + cell_height - ((cell_height / 7) * size_param)
        if shape == SHAPE_RECTANGLE:
            self.game_board_canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        elif shape == SHAPE_CIRCLE:
            self.game_board_canvas.create_oval(x1, y1, x2, y2, fill=color)
        else:
            points = [x1, y2, x2, y2, ((x1 + x2) / 2), y1]
            self.game_board_canvas.create_polygon(points, fill=color)
