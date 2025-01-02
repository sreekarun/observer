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
    collection = mongo.db.mycollection
    payload = request.json
    name = payload.get('name')
    try:
        data_id = collection.insert_one({'name': name}).inserted_id
        new_data = collection.find_one({'_id': ObjectId(data_id)})
        result = {'name': new_data['name']}
        return jsonify({'result': result}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete data
@app.route('/api/data/<id>', methods=['DELETE'])
def delete_data(id):
    collection = mongo.db.mycollection
    try:
        data = collection.find_one({'_id': ObjectId(id)})
        if data:
            collection.delete_one({'_id': ObjectId(id)})
            return jsonify({'result': 'Data deleted successfully'})
        else:
            return jsonify({'result': 'No data found'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Api to get a specific data by id 
# Endpoint to get data by id
# http://localhost:5001/api/data/5f1b1b3b7b3b3b3b3b3b3b3b


@app.route('/api/data/<id>', methods=['PUT'])
def update_data_by_id(id):
    collection = mongo.db.mycollection
    data = request.json
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'no changes or no data found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)