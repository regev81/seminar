from Constants import *


class GameMemento:

    def __init__(self, game_data_grid):
        self.game_data_grid = self.copy_game_board(game_data_grid)

    # copy the game_data_grid and create a new game_data_grid for the memento
    def copy_game_board(self, game_data_grid):
        grid = []
        for row in range(ROWS):
            row_arr = []
            for col in range(COLS):
                row_arr.append(game_data_grid[row][col])
            grid.append(row_arr)

        return grid


