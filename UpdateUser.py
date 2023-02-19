from GetUserByID import get_user_by_id
from database import connect_to_db


def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET name = ?, password = ?, email = ?, phone = ?, address = ?, country = ?, maxTimeAllowed "
            "= ?, ""playedTime = ?, WHERE username =?",
            (user["name"], user["password"], user["email"], user["phone"],
             user["address"], user["country"],
             user["username"], user["maxTimeAllowed"], user["isPaused"], user["playedTime"]))
        conn.commit()
        # return the user
        updated_user = get_user_by_id(user["username"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user


def delete_user(username):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from users WHERE username = ?", (username,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message
