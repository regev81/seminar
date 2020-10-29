import tkinter as tk

class View(tk.Tk):

    def __init__(self,controller):
        super().__init__()
        self.controller = controller

        self.title = "Tic Tac Toe"

        self._create_main_frame()

        self._create_example_button()


    def main(self):
        self.mainloop()

    def _create_main_frame(self):
        self.main_frm = tk.Frame(self)
        self.main_frm.pack()

    def _create_example_button(self):
        text = 'example'
        btn = tk.Button(self.main_frm, text=text, command=(
            lambda button=text: self.controller.on_button_click(button)
        ))
        btn.pack()
