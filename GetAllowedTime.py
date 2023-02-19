import sqlite3

from database import connect_to_db

def get_Allowed_Time(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT maxTimeAllowed FROM users WHERE user_id = ?",(user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["maxTimeAllowed"] = row["maxTimeAllowed"]
    except:
        user = {}

    return user