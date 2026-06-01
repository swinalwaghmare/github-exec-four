from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from CI/CD demo!", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})