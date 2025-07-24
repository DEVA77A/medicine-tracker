
from model.db_connection import get_connection

class UserDAO:
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def login(self, username, password):
        self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        return self.cur.fetchone()

    def register(self, username, password):
        try:
            self.cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except:
            return False
