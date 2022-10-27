from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json
import waitress
app = Flask(__name__)

dotenv_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)

database_filename = os.getenv('DATABASE_NAME')
cors = CORS(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route("/", methods=["GET"])
def index():
    return jsonify(
        { "slackUsername": "Nimi", 
            "backend": True,
            "age": 23,
            "bio":  "I am Alabi Yetunde. A backend HNG intern. I'm passionate about software development."
        }, sort_keys=False)

@app.route("/user", methods=["GET"])
def user():
    name = request.args.get("slackUsername", type=str)
    backend = request.args.get("backend", default=False, type=lambda v: v.upper() == "true")
    age = request.args.get("age", type=int)
    bio = request.args.get("bio", type=str)
    return jsonify(
        { "slackUsername": name, 
            "backend": backend,
            "age": age,
            "bio": bio 
        })

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)
