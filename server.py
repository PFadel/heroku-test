import os

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5000))


@app.route('/hello')
def hello():
    return jsonify({"message": "I'm cool and all"})


app.run(host='0.0.0.0', threaded=True, port=port)
