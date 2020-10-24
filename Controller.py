from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self,text):
        print(f"button {text} clicked")
