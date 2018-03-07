from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def name():
	data = {
		"name": 'AlexSheu'
	}
	return jsonify(data)
# jsonify includes also the headers, extra information

@app.route('/hello/<name>', methods=['GET'])
def helloName(name):
	hello = {
		'message': 'Hello there {0}'.format(name)
	}
	return jsonify(hello)

@app.route('/distance', methods=['POST'])
def getDist():
	# global variable called requests for handler functions
	r = request.get_json()
	distance = ((r['a'][0] - r['b'][0])**2 + (r['a'][1] - r['b'][1])**2)**0.5
	res = {
		'distance': distance
	}

	return jsonify(res)
