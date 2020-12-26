from tkinter import *
from tkinter import font
from tkinter.font import Font
from tkinter.ttk import Combobox

from Constants import *
from new.Constants import Size, Shape, Color


class View:

    def __init__(self,controller):
        self.controller = controller
        self.start_page = None
        self.new_game_page = None
        self.game_board_canvas = None
        self.add_user_page = None
        self.game_board_message = None
        self.new_user_page = None
        self.new_user_entry_str = None
        self.new_user_add_error_label_str = None
        self.player1_name_combo = None
        self.player1_shape_combo = None
        self.player1_color_combo = None
        self.player1_size_combo = None
        self.player2_name_combo = None
        self.player2_shape_combo = None
        self.player2_color_combo = None
        self.player2_size_combo = None

    def main(self):
        self.create_start_page()

    def create_start_page(self):
        height = 160
        width = 280
        root = Tk()
        root.geometry(f"{width}x{height}")
        root.resizable(width=False, height=False)
        root.title("Tic Tac Toe Menu")
        root.wm_attributes("-topmost", 1)
        self.start_page = Frame(root)
        self.start_page.pack(pady = 5)

        # buttons
        buttons_text_font = font.Font(family='Helvetica', size=15, weight='bold')
        padding_y = 3

        new_game_but = Button(self.start_page, text="New Game", command=self.controller.new_game_clicked)
        new_game_but['font'] = buttons_text_font
        new_game_but.pack(side="top", fill="x",pady=padding_y)

        add_user_but = Button(self.start_page, text="Add new user", command=self.controller.add_new_user_clicked)
        add_user_but['font'] = buttons_text_font
        add_user_but.pack(side="top", fill="x",pady=padding_y)

        generate_report_but = Button(self.start_page, text="Generate Report", command=self.controller.generate_report_clicked)
        generate_report_but['font'] = buttons_text_font
        generate_report_but.pack(side="top", fill="x",pady=padding_y)

        root.mainloop()

    def create_new_game_page(self):
        height = 520
        width = 380
        root = Toplevel()
        root.geometry(f"{width}x{height}")
        root.resizable(width=False, height=False)
        root.title("New Game")
        root.wm_attributes("-topmost", 1)
        self.new_game_page = Frame(root)
        self.new_game_page.pack()

        # shapes, colors and sizes lists
        shapes = [Shape.CIRCLE.value, Shape.RECTANGLE.value, Shape.TRIANGLE.value]
        colors = [Color.BLUE.value, Color.RED.value, Color.GREEN.value]
        sizes = [Size.SMALL.value, Size.MEDIUM.value, Size.LARGE.value]
        lableframe_title_font = Font(family="Helvetica", size=20, weight="bold")
        lable_font = Font(family="Helvetica", size=15)
        combo_font = Font(family="Helvetica", size=10)
        padx = 5
        pady = 5

        ### first labelframe
        player1_labelframe = LabelFrame(self.new_game_page, text="player 1", font = lableframe_title_font)
        player1_labelframe.pack(fill="both", expand="yes", pady=15)
        # name
        player1_name_label = Label(player1_labelframe, text="Name:",font=lable_font).grid(row=0, column=0,padx=padx, pady=pady)
        self.player1_name_combo = Combobox(player1_labelframe,font=combo_font).grid(row=0, column=1,padx=padx, pady=pady)
        # shape
        player1_shape_label = Label(player1_labelframe, text="Shape:",font=lable_font).grid(row=1, column=0,padx=padx, pady=pady)
        self.player1_shape_combo = Combobox(player1_labelframe, values=shapes,font=combo_font).grid(row=1, column=1,padx=padx, pady=pady)
        # color
        player1_color_label = Label(player1_labelframe, text="Color:",font=lable_font).grid(row=2, column=0,padx=padx, pady=pady)
        self.player1_color_combo = Combobox(player1_labelframe, values=colors,font=combo_font).grid(row=2, column=1,padx=padx, pady=pady)
        # size
        player1_shape_label = Label(player1_labelframe, text="Size:",font=lable_font).grid(row=3, column=0,padx=padx, pady=pady)
        self.player1_shape_combo = Combobox(player1_labelframe, values=sizes,font=combo_font).grid(row=3, column=1,padx=padx, pady=pady)

        ### second labelframe
        player2_labelframe = LabelFrame(self.new_game_page, text="player 2",font = lableframe_title_font)
        player2_labelframe.pack(fill="both", expand="yes",pady=15)
        # name
        player2_name_label = Label(player2_labelframe, text="Name:",font=lable_font).grid(row=0, column=0,padx=padx, pady=pady)
        self.player2_name_combo = Combobox(player2_labelframe,font=combo_font).grid(row=0, column=1,padx=padx, pady=pady)
        # shape
        player2_shape_label = Label(player2_labelframe, text="Shape:",font=lable_font).grid(row=1, column=0,padx=padx, pady=pady)
        self.player2_shape_combo = Combobox(player2_labelframe, values=shapes,font=combo_font).grid(row=1, column=1,padx=padx, pady=pady)
        # color
        player2_color_label = Label(player2_labelframe, text="Color:",font=lable_font).grid(row=2, column=0,padx=padx, pady=pady)
        self.player2_color_combo = Combobox(player2_labelframe, values=colors,font=combo_font).grid(row=2, column=1,padx=padx, pady=pady)
        # size
        player2_shape_label = Label(player2_labelframe, text="Size:",font=lable_font).grid(row=3, column=0,padx=padx, pady=pady)
        self.player2_shape_combo = Combobox(player2_labelframe, values=sizes,font=combo_font).grid(row=3, column=1,padx=padx, pady=pady)

        # start game button
        start_game_but = Button(self.new_game_page, text="Start Game",font = lable_font, command=self.controller.start_game_clicked)
        start_game_but.pack(side=LEFT)

    def create_game_board_page(self, game_data_grid, text_message):
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
        color = the_player.color.value
        div_param = 7
        if the_player.size == Size.LARGE:
            size_param = 1
        elif the_player.size == Size.MEDIUM:
            size_param = 2
        else:
            size_param = 3

        x1 = cell_topleft_x + ((cell_width / div_param) * size_param)
        y1 = cell_topleft_y + ((cell_height / div_param) * size_param)
        x2 = cell_topleft_x + cell_width - ((cell_width / div_param) * size_param)
        y2 = cell_topleft_y + cell_height - ((cell_height / div_param) * size_param)
        if shape == Shape.RECTANGLE:
            self.game_board_canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        elif shape == Shape.CIRCLE:
            self.game_board_canvas.create_oval(x1, y1, x2, y2, fill=color)
        else:
            points = [x1, y2, x2, y2, ((x1 + x2) / 2), y1]
            self.game_board_canvas.create_polygon(points, fill=color)

    def create_new_user_page(self):
        height = 600
        width = 400
        root = Toplevel()
        root.title("New new user")
        self.new_user_page = Frame(root, height=height, width=width)
        self.new_user_page.pack()

        new_user_label = Label(self.new_user_page,text = 'Enter new user name:')
        new_user_label.grid(column=0, row=0)
        self.new_user_entry_str = StringVar()
        new_user_entry = Entry(self.new_user_page, textvariable=self.new_user_entry_str)
        new_user_entry.grid(column=1, row=0)
        add_button = Button(self.new_user_page, text="Add",command=self.controller.insert_new_user_clicked)
        add_button.grid(column=2, row=0)
        self.new_user_add_error_label_str = StringVar()
        new_user_add_error_label = Label(self.new_user_page,textvariable = self.new_user_add_error_label_str)
        new_user_add_error_label.grid(row=1)

    def create_labelframe(self,player):
        # shapes, colors and sizes lists
        shapes = [Shape.CIRCLE.value, Shape.RECTANGLE.value, Shape.TRIANGLE.value]
        colors = [Color.BLUE.value, Color.RED.value, Color.GREEN.value]
        sizes = [Size.SMALL.value, Size.MEDIUM.value, Size.LARGE.value]

        player1_labelframe = LabelFrame(self.new_game_page, text=player)
        player1_labelframe.pack(fill="both", expand="yes")
        # name
        player1_name_label = Label(player1_labelframe, text="Name:").grid(row=0, column=0)
        self.player1_name_combo = Combobox(player1_labelframe).grid(row=0, column=1)
        # shape
        self.player1_shape_label = Label(player1_labelframe, text="Shape:").grid(row=1, column=0)
        self.player1_shape_combo = Combobox(player1_labelframe, values=shapes).grid(row=1, column=1)
        # color
        self.player1_color_label = Label(player1_labelframe, text="Color:").grid(row=2, column=0)
        self.player1_color_combo = Combobox(player1_labelframe, values=colors).grid(row=2, column=1)
        # size
        self.player1_shape_label = Label(player1_labelframe, text="Size:").grid(row=3, column=0)
        self.player1_shape_combo = Combobox(player1_labelframe, values=sizes).grid(row=3, column=1)
