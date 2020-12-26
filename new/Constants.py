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
    ACTIVE = "ACTIVE"


class GameResult(Enum):
    DRAW = "DRAW"
    PLAYER1_WIN = "PLAYER1_WIN"
    PLAYER2_WIN = "PLAYER2_WIN"

class InsertNewUserResulr(Enum):
    INSERT_NEW_USER_RESULT_INVALID = "INSERT_NEW_USER_RESULT_INVALID"
    INSERT_NEW_USER_RESULT_USER_EXISTS = "INSERT_NEW_USER_RESULT_USER_EXISTS"


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RECORDS_FILE_NAME = "WinsRecords.txt"
RECORDS_FILE_PATH = os.path.join(ROOT_DIR, RECORDS_FILE_NAME)
ROWS = 3
COLS = 3
