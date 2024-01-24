from flask import Flask, jsonify, request, Response
from pymongo import MongoClient, errors
from bson import ObjectId
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)

client = MongoClient("mongodb+srv://mongo:mongo@cluster0.bll8kuf.mongodb.net/?retryWrites=true&w=majority")
db = client["students"]
students_collection = db["std_info"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
