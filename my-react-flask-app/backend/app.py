import os
from bson import ObjectId
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB configuration with credentials from environment variable
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongo:27017/mydatabase")
mongo = PyMongo(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = mongo.db.mycollection.find()
    result = []
    for item in data:
        result.append({'id': str(item['_id']), 'name': item['name']})
    return jsonify(result)

# Endpoint to update mongo with data
@app.route('/api/data', methods=['POST'])
def add_data():
    data = mongo.db.mycollection
    payload = request.json
    name = payload.get('name')
    try:
        data_id = data.insert_one({'name': name}).inserted_id
        new_data = data.find_one({'_id': ObjectId(data_id)})
        result = {'name': new_data['name']}
        return jsonify({'result': result}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)