from new.Constants import *


class FileHandler:

    @staticmethod
    def get_all_users_and_wins():
        users_wins = {}
        f = open(RECORDS_FILE_PATH, "r")
        while True:
            name = f.readline().rstrip()
            wins = f.readline().rstrip()
            if wins:
                users_wins[name] = int(wins)
            else:
                break  # end of file

        return users_wins
