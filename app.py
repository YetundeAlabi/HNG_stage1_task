from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json
import waitress
app = Flask(__name__)

dotenv_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


cors = CORS(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route("/")
def index():
    return json.dumps(
        { "slackUsername": "Nimi", 
            "backend": True,
            "age": 23,
            "bio":  "I am Alabi Yetunde. A backend HNG intern. I'm passionate about software development."
        }, sort_keys=False), 200, {"content-type": "application/json"}

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)
