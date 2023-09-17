from flask import Flask, request, jsonify
from db_system import DB

# https://flask.palletsprojects.com/en/2.3.x/quickstart/#about-responses

app = Flask(__name__)
db = DB()

@app.route('/get_entries', methods=['GET'])
def get_entries():
    washrooms = db.get_entries()
    return jsonify(washrooms)

@app.route('/get_entry/<int:id>', methods=['GET'])
def get_entry(id):
    washroom = db.get_entry(id)
    return jsonify(washroom)

@app.route('/create_entry', methods=['POST'])
def create_entry():
    data = request.json
    cleaniness = data['cleaniness']
    address = data['address']
    hours = data['hours']
    photo = data.get('photo')
    active = data.get('active')
    review = data.get('review')

    if db.create_entry(cleaniness, address, hours, photo, active, review):
        return jsonify({"message": "Entry created successfully"}), 201
    else:
        return jsonify({"message": "Invalid data"}), 400

@app.route('/update_entry/<int:id>', methods=['PUT'])
def update_entry(id):
    data = request.json
    cleaniness = data.get('cleaniness')
    address = data.get('address')
    hours = data.get('hours')
    photo = data.get('photo')
    active = data.get('active')
    review = data.get('review')

    if db.update_entry(id, cleaniness,address, hours, photo, active, review):
        return jsonify({"message": f"Entry with ID {id} updated successfully"}), 200
    else:
        return jsonify({"message": "Invalid data or ID"}), 400

@app.route('/review_cleaniness/<int:id>', methods=['PUT'])
def review_cleaniness(id):
    data = request.json

    cleaniness = data.get('cleaniness')

    if db.review_cleaniness(id, cleaniness):
        return jsonify({"message": f"Entry with ID {id} updated successfully"}), 200
    else:
        return jsonify({"message": "Invalid data or ID"}), 400

if __name__ == "__main__":
    app.run()