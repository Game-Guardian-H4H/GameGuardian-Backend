import sqlite3

from database import connect_to_db

def set_Pause_State(user_id, state):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("UPDATE users SET state = ?, WHERE user_id =?",
                    (user_id, state))
        row = cur.fetchone()

        # convert row object to dictionary
    except:
        user = {}

    return user