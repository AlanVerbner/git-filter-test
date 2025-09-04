from flask import Flask, jsonify
from main import hello, calculate

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'API is running'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/hello')
def hello_endpoint():
    return jsonify({'message': hello()})

@app.route('/calculate/<int:x>/<int:y>')
def calc_endpoint(x, y):
    return jsonify({'result': calculate(x, y)})