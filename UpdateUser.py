from GetUserByID import get_user_by_id
from database import connect_to_db


def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ?, maxTimeAllowed = ?, "
                    "playedTime = ?, WHERE user_id =?",
                     (user["name"], user["email"], user["phone"],
                     user["address"], user["country"],
                     user["user_id"], user["maxTimeAllowed"], user["isPaused"], user["playedTime"]))
        conn.commit()
        #return the user
        updated_user = get_user_by_id(user["user_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user


def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from users WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message