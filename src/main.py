# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load env vars from a .env file if present (useful for local dev)
load_dotenv()

app = Flask(__name__)

# CORS: allow any origin; advertise only GET as allowed
CORS(
    app,
    resources={r"/products": {"origins": "*"}},
    methods=["GET"]
)

@app.route("/products", methods=["GET"])
def products():
    return jsonify([
        {"id": 1, "name": "Dog Food",   "price": 19.99},
        {"id": 2, "name": "Cat Food",   "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ])

if __name__ == "__main__":
    port = int(os.getenv("PORT", "3030"))
    # Bind to 0.0.0.0 like your Rust version
    app.run(host="0.0.0.0", port=port)
