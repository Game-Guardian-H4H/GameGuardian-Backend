import sqlite3

from database import connect_to_db


def get_all_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            user = {"username": i["username"], "name": i["name"], "email": i["email"], "phone": i["phone"],
                    "address": i["address"], "country": i["country"], "maxTimeAllowed": i["maxTimeAllowed"]}
            users.append(user)

    except:
        users = []

    return users


