from flask import Flask, request, jsonify
from flask import *
app = Flask(__name__)
from collections import *


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    if "first" in data and "second" in data:
        first = data["first"]
        second = data["second"]
        result = first + second
        return jsonify({"result": result}), 200
    else:
        return jsonify({"error": "Missing 'first' or 'second' in request data"}), 400


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if "first" in data and "second" in data:
        first = data["first"]
        second = data["second"]
        result = first - second
        return jsonify({"result": result}), 200
    else:
        return jsonify({"error": "Missing 'first' or 'second' in request data"}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')