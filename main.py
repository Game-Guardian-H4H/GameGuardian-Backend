from flask import Flask, request, jsonify #added to top of file

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

@app.route('/api/getPauseState/<user_id>', methods=['GET'])
def getPauseState(user_id):
    return jsonify(get_Pause_State())

@app.route('/api/setPauseState/<user_id, state>', methods=['POST'])
def setPauseState(user_id):
    return jsonify(set_Pause_State())

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_All_Users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

@app.route('/api/users/update',  methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

@app.route('/api/users/getAllowedTime/<user_id>',  methods = ['GET'])
def api_user_allowed_time(user_id):
    return jsonify(get_Allowed_Time(user_id))

@app.route('/api/users/putPlayedTime/<user_id, played_time>',  methods = ['PUT'])
def api_user_played_time(user_id, played_time):
    return jsonify(put_Played_Time(user_id, played_time))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run(ssl_context=('/Users/abhishekpatil/certificates/server.crt', '/Users/abhishekpatil/certificates/server.key')) #run app