from flask import Flask, render_template, request, jsonify
import os,sys,requests, json
from random import randint
from flask_cors import CORS, cross_origin


app = Flask(__name__)


app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources=r'/api/*')

@app.route('/api/')
def home():
  return render_template('index.html')


@app.route('/api/parse', methods=['POST'])
def send_message():
    data = request.json
    user_message = data['user_message']
    response = requests.post("http://http://0.0.0.0:5005//webhook", json={"message": user_message})
    return jsonify(response.json()), 200


if __name__ == "__main__":
 
  app.run(debug=True)