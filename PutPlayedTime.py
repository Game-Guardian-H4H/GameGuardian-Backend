import sqlite3

from database import connect_to_db


def put_played_time():
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("UPDATE users SET playedTime = ?, WHERE username =?",
                    (user['played_time'], user['username']))
        row = cur.fetchone()

        # convert row object to dictionary
    except:
        user = {}

    return user
