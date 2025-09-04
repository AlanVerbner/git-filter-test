import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path='app.db'):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        with self.get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                           (id INTEGER PRIMARY KEY, username TEXT UNIQUE)''')
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()