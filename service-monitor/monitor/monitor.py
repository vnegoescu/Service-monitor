import json
import os
import sys
import time

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

mongo_client = MongoClient(os.environ['DB'], 27017)
db = mongo_client.db

@app.route('/upd', methods=['POST'])
def monitor():
	data = request.get_json()
	db.services.update_one({'name':data['name']}, {'$set':{'time':time.time()}}, upsert = True)
	
	return jsonify({'message': 'Ping received'}), 200

@app.route('/info', methods=['GET'])
def info():
	query = request.get_json()
	data = db.services.find_one(query)
	
	data['_id'] = str(data['_id'])

	diff = (time.time() - data['time'])
	if diff > 5:
		return jsonify({'msg': 'writer is not alive'}), 200

	return jsonify({'name': data['name'], 'timestamp': data['time']}), 200

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5000, debug = True)