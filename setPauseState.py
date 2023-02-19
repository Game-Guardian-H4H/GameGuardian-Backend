import sqlite3

from database import connect_to_db


def set_pause_state():
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("UPDATE users SET state = ?, WHERE username =?",
                    (user["username"], user["state"]))
        row = cur.fetchone()

        # convert row object to dictionary
    except:
        user = {}

    return user
