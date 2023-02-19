import sqlite3

from database import connect_to_db


def get_user_by_id(username):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cur.rowcount is not 0:
            row = cur.fetchone()

            # convert row object to dictionary
            user["username"] = row["username"]
            user["maxTimeAllowed"] = row["maxTimeAllowed"]
            user["playedTime"] = row["playedTime"]
            user["isPaused"] = row["isPaused"]
    except:
        return "Failure", 500

    return user
