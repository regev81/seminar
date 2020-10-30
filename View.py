
from tkinter import *


class View(Tk):

    clicked = True
    count = 0

    def __init__(self,controller):
        super().__init__()
        self.controller = controller

        self.title = "Tic Tac Toe"

        self._create_main_frame()

        self._create_buttons()


    def main(self):
        #self._create_main_frame()
        #self._create_example_button()
        self.mainloop()

    def _create_main_frame(self):
        self.main_frm = Frame(self)
        self.main_frm.pack()

    def _create_buttons(self):
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count

        b1 = Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.b_click(b1))
        b2 = Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b2))
        b3 = Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b3))
        b4 = Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b4))
        b5 = Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b5))
        b6= Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b6))
        b7= Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b7))
        b8= Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b8))
        b9= Button(self.main_frm, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.controller.on_button_click(b9))

        # Grid our buttons to the screen
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)


