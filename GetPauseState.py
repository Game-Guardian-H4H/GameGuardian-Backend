import sqlite3

from GetUserByID import get_user_by_id
from database import connect_to_db, create_db_table


def get_Pause_State(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT isPaused FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        user["user_id"] = row["user_id"]

    except:
        conn().rollback()

    finally:
        conn.close()

    return user