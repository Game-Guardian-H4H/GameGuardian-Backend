import sqlite3

from database import connect_to_db

def put_Played_Time(user_id, played_time):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("UPDATE users SET playedTime = ?, WHERE user_id =?",
                    (played_time, user_id))
        row = cur.fetchone()

        # convert row object to dictionary
    except:
        user = {}

    return user