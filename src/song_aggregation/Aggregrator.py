import sqlite3 as sql
import os


class Aggregrator(object):
    db_path = "../../data/songs.db"
    cur = None

    def __init__(self):

        # creates empty db if it doesn't exist
        open(self.db_path, 'a').close()
        conn = sql.connect(self.db_path)
        self.cur = conn.cursor()
        self.cur.execute('''CREATE TABLE titles (artist, title)''')
        conn.commit()
        conn.close()

if __name__ == "__main__":
    a = Aggregrator()
