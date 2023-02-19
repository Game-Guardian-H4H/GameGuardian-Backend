from flask import Flask, request, jsonify

from Create_user import insert_user
from GetAllUsers import get_All_Users
from GetAllowedTime import get_Allowed_Time
from GetPauseState import get_Pause_State
from GetUserByID import get_user_by_id
from UpdateUser import update_user, delete_user
from PutPlayedTime import put_Played_Time
from setPauseState import set_Pause_State

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/getPauseState/<username>', methods=['GET'])
def get_pause_state(username):
    return jsonify(get_Pause_State(username))


@app.route('/api/setPauseState', methods=['POST'])
def set_pause_state():
    user = request.get_json()
    return jsonify(set_Pause_State(user))


app = Flask(__name__)


@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_All_Users())


@app.route('/api/users/<username>', methods=['GET'])
def api_get_user(username):
    return jsonify(get_user_by_id(username))


@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))


@app.route('/api/users/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))


@app.route('/api/users/delete/<username>', methods=['DELETE'])
def api_delete_user(username):
    return jsonify(delete_user(username))


@app.route('/api/users/getAllowedTime/<username>', methods=['GET'])
def api_user_allowed_time(username):
    return jsonify(get_Allowed_Time(username))


@app.route('/api/users/putPlayedTime', methods=['PUT'])
def api_user_played_time():
    user = request.get_json()
    return jsonify(put_Played_Time(user))


if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run()  # run app
