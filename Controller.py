from Model import Model
from View import View
from tkinter import messagebox

class Controller:

    # X starts so true
    clicked = True
    count = 0

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self,text):
        print(f"button {text} clicked")

    def b_click(self,b):
        global clicked, count
            if b["text"] == " " and clicked == True:
                b["text"] = "X"
                clicked = False
                count += 1
               # checkifwon()
            elif b["text"] == " " and clicked == False:
                b["text"] = "O"
                clicked = True
                count += 1
               # checkifwon()
            else:
                #messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")