from flask import Flask, request, jsonify #added to top of file
#from flask_cors import CORS #added to top of file

from Create_user import insert_user
from GetAllUsers import get_All_Users
from GetUserByID import get_user_by_id
from UpdateUser import update_user, delete_user

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})

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

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run(host='127.0.0.9', port=4455, debug=True) #run app