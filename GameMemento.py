from Constants import *


class GameMemento:

    def __init__(self, game_data_grid):
        self.game_data_grid = self.copy_game_board(game_data_grid)

    # copy the game_data_grid and create a new game_data_grid for the memento
    def copy_game_board(self, game_data_grid):
        data_grid = {}
        for key, value in game_data_grid.items():
            data_grid[key] = value
        return data_grid


