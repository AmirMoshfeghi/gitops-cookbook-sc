from flask import Flask, request, jsonify
import os

app = Flask(__name__)

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == USERNAME and data['password'] == PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Login failed"}), 401

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)