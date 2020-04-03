import json
import requests
import sys
import threading
import time

from flask import Flask, jsonify, request

app = Flask(__name__)
l = [False]

class SendPing(object):
	def __init__(self, interval = 3):

		self.interval = interval
		thread = threading.Thread(target = self.run)
		thread.daemon = True
		thread.start()

	def run(self):
		url = 'http://monitor:5000/upd'
		info = {'name':'writer'}

		while not l[0]:
			time.sleep(self.interval)
			requests.post(url = url, json = info)

@app.route('/', methods=['POST'])
def monitor():
	data = request.get_json()
	
	with open("data/logfile.txt", "a+") as file:
		text = data.get('text', None)

		if text == 'exit':
			l[0] = True
			sys.exit()

		text += '\n'
		file.write(text)

	return jsonify({'message': 'Message received'}), 200


if __name__== "__main__":
	tmp = SendPing()

	app.run(host = '0.0.0.0', port = 6000, debug = True, threaded=True)
