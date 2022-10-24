import sqlite3
from datetime import datetime as dt

# --- DataBase's ---
user_db = sqlite3.connect('user.db')

user_cur = user_db.cursor()

user_cur.execute('''CREATE TABLE IF NOT EXISTS users(
                name TEXT NOT NULL,
                user_id BIGINT,
                last_move DATETIME);
''')

user_db.commit()


def addUser(user_id, cur, db):
    cur.execute("""UPDATE users SET last_move = ? WHERE user_id = ?""", (dt.now(), user_id))
    db.commit()

