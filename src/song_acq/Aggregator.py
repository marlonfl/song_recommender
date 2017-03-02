import sqlite3
import os


class Aggregrator(object):
    db_path = "../../data/songs.db"

    def __init__(self):
        # creates empty db if it doesn't exist
        open(self.db_path, 'a').close()

if __name__ == "__main__":
    a = Aggregrator()
