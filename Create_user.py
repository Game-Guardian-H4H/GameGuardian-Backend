from GetUserByID import get_user_by_id
from database import connect_to_db, create_db_table


def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        create_db_table()
        check_user = get_user_by_id(user["username"])
        if check_user is None:
            return {}
        else:
            cur.execute("INSERT INTO users (username, name, password, email, phone, address, country, maxTimeAllowed) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (user['username'], user['name'], user['password'], user['email'], user['phone'],
                         user['address'], user['country'], user['maxTimeAllowed']))
            conn.commit()
            inserted_user = get_user_by_id(cur.lastrowid)

    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_user
