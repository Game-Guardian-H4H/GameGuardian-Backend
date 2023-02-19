from flask import Flask           # import flask
import sqlite3

app = Flask(__name__)

in_memory_datastore = {
    "Max_mins": {"max": "60"}
}



@app.route('/gameSafe/maxMins', methods=['GET'])
def get_time():
    return {"MaxMins": list(in_memory_datastore.values())}


@app.route('/update', methods=['POST'])
def update_time():
    # Get the updated data from the request body
    updated_data = request.get_json()

    # Update the original data with the new data
    for key, value in updated_data.items():
        my_data[key] = value

    # Return a success message
    return 'Time updated successfully!'


if __name__ == '__main__':
    app.run(debug=True)
