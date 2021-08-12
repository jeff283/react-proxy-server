from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route("/")
def index():
    return "Welcome, this Proxy Server"

@app.route("/<lang>/<word>")
def home(lang, word):
    resp = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/{lang}/{word}").json()
    return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)