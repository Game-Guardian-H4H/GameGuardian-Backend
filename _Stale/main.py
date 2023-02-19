from flask import Flask, request, jsonify

from Create_user import insert_user
from GetAllUsers import get_all_users
from GetAllowedTime import get_allowed_time
from GetPauseState import get_pause_state
from GetUserByID import get_user_by_id
from UpdateUser import update_user, delete_user
from PutPlayedTime import put_played_time
from setPauseState import set_pause_state

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/getPauseState/<username>', methods=['GET'])
def get_pause_state(username):
    return jsonify(get_pause_state(username))


@app.route('/api/setPauseState', methods=['POST'])
def set_pause_state():
    user = request.get_json()
    return jsonify(set_pause_state(user))


app = Flask(__name__)


@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_all_users())


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
    return jsonify(get_allowed_time(username))


@app.route('/api/users/putPlayedTime', methods=['PUT'])
def api_user_played_time():
    user = request.get_json()
    return jsonify(put_played_time(user))


if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run()  # run app
