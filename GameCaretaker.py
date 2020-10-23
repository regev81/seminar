
class GameCaretaker:

    def __init__(self):
        self.memento_list = []
        self.current_memento_index = -1

    def add_memento(self,memento):
        if(len(self.memento_list) > 0): # not first memento
            # remove all mementos from current index to the end pf the list
            self.memento_list = self.memento_list[0:self.current_memento_index+1]

        self.memento_list.append(memento)
        self.current_memento_index += 1

    def undo(self):
        if (self.current_memento_index > 0):
            self.current_memento_index -= 1
            return self.memento_list[self.current_memento_index]

    def redo(self):
        if (self.current_memento_index < len(self.memento_list)-2):
            self.current_memento_index += 1
            return self.memento_list[self.current_memento_index]


