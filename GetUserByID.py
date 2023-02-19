import sqlite3

from database import connect_to_db


def get_user_by_id(username):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["username"] = row["username"]
        user["name"] = row["name"]
        user["email"] = row["email"]
        user["phone"] = row["phone"]
        user["address"] = row["address"]
        user["country"] = row["country"]
        user["maxTimeAllowed"] = row["maxTimeAllowed"]
        user["isPaused"] = row["isPaused"]
        user["playedTime"] = row["playedTime"]
    except:
        user = {}

    return user
