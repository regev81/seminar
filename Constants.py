import os
from enum import Enum


class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class Shape(Enum):
    RECTANGLE = "RECTANGLE"
    CIRCLE = "CIRCLE"
    TRIANGLE = "TRIANGLE"


class Size(Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"


class GameState(Enum):
    INACTIVE = "INACTIVE"
    OVER = "OVER"
    CHOOSE_PLAYERS_DETAILS = "PREGAME"
    ACTIVE = "ACTIVE"


class GameResult(Enum):
    DRAW = "DRAW"
    PLAYER1_WIN = "PLAYER1_WIN"
    PLAYER2_WIN = "PLAYER2_WIN"

class Error(Enum):
    PLAYERS_SAME_NAME = "Choose different name for each player"
    PLAYERS_SAME_ATTRIBUTES = "Change Shape/Color/Size, The 2 players must have al least 1 different attribute"
    EMPTY_ATTRIBUTE = "Some attributes are missing"
    USER_EXISTS = "User Exists in file"



ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RECORDS_FILE_NAME = "WinsRecords.txt"
RECORDS_FILE_PATH = os.path.join(ROOT_DIR, RECORDS_FILE_NAME)
ROWS = 3
COLS = 3
