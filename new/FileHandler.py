from new.Constants import *


class FileHandler:

    @staticmethod
    def get_all_users_and_wins():
        users_wins = {}
        f = open(RECORDS_FILE_PATH, "r")
        while True:
            name = f.readline().strip()
            wins = f.readline().strip()
            if wins:
                users_wins[name] = int(wins)
            else:
                break  # end of file

        f.close()
        return users_wins

    @staticmethod
    def add_new_user_to_file(user_name):
        f = open(RECORDS_FILE_PATH, "a")
        f.write(f"\n{user_name}\n{0}")
        f.close()

    @staticmethod
    def add_win_to_user(user_name):
        lines = []
        f = open(RECORDS_FILE_PATH, "r")
        while True:
            name = f.readline().strip()
            wins = f.readline().strip()
            if wins:
                new_wins = int(wins)
                if name == user_name:
                    new_wins = new_wins +1
                lines.append(f"{name}")
                lines.append(f"{new_wins}")
            else:
                break  # end of file
        f.close()

        f = open(RECORDS_FILE_PATH, "w")
        f.write('\n'.join(lines))

    @staticmethod
    def user_name_exists_in_file(user_name):
        f = open(RECORDS_FILE_PATH, "r")
        while True:
            name = f.readline().strip()
            wins = f.readline().strip()
            if wins:
                if name == user_name:
                    f.close()
                    return True
            else:
                break  # end of file

        f.close()
        return False