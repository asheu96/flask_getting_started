from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def name():

        """function creates dictionary data and changes it to a json file to be placed on the flask server
        :returns: data, in json format"""
	data = {
		"name": 'AlexSheu'
	}
	return jsonify(data)
# jsonify includes also the headers, extra information

@app.route('/hello/<name>', methods=['GET'])
def helloName(name):
        
        """function helloName() creates dictionary hello with the name placed into the name() function above
        :returns: hello, in json format"""
	hello = {
		'message': 'Hello there {0}'.format(name)
	}
	return jsonify(hello)

@app.route('/distance', methods=['POST'])
def getDist():
	
        """function getDist() creates a dictionary of the values posted onto the Flask server and the distance between the points
        :returns: res, a dictionary with a, b, and the distance between the points in json format"""
        # global variable called requests for handler functions
	
        r = request.get_json()
        distance = ((r['a'][0] - r['b'][0])**2 + (r['a'][1] - r['b'][1])**2)**0.5
        res = {'distance': distance, 'a':r['a'], 'b':r['b']}
        return jsonify(res)

def returnDist():

        """functions that allows for testing of distance calculations
        :returns: distance calculations based on the given distances"""
        r = request.get_json()
        distance = ((r['a'][0] - r['b'][0])**2 + (r['a'][1] - r['b'][1])**2)**0.5
        return distance
