from GetUserByID import get_user_by_id
from database import connect_to_db, create_db_table


def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        # create_db_table();
        cur.execute("INSERT INTO users (name, email, phone, address,country) VALUES (?, ?, ?, ?, ?)", (user['name'],
                    user['email'], user['phone'], user['address'],user['country']))
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_user