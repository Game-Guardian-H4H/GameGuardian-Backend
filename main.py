from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS, cross_origin

from Create_user import insert_user
from GetAllUsers import get_All_Users
from GetUserByID import get_user_by_id
from UpdateUser import update_user, delete_user

app = Flask(__name__)
# enable CORS
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def helloworld():
    return 'Hello, World!'

@app.route('/api/pausegame', methods=['GET'])
def pausegame():
    print("pausegame")
    return 'noooo!'

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

# if __name__ == "__main__":
    # app.run(debug=True, ssl_context='adhoc') #run app
    app.run(debug=True)  # run app