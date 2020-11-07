
class GameCaretaker:

    def __init__(self):
        self.memento_list = []
        self.current_memento_index = -1

    # add GameMemento to the memento list
    def add_memento(self,memento):
        if len(self.memento_list) > 0: # not first memento
            # remove all mementos from current index to the end of the list
            self.memento_list = self.memento_list[0:self.current_memento_index+1]

        self.memento_list.append(memento)
        self.current_memento_index += 1

    # perform undo action (return the memento before the current)
    def undo(self):
        if self.current_memento_index > 0:
            self.current_memento_index -= 1
            return self.memento_list[self.current_memento_index]

    # perform redo action (return the memento after the current)
    def redo(self):
        if self.current_memento_index < len(self.memento_list)-1:
            self.current_memento_index += 1
            return self.memento_list[self.current_memento_index]


