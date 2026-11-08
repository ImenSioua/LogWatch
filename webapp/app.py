import os

from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32).hex()
csrf = CSRFProtect(app)


@app.route("/")
def hello():
    return "Hello LogWatch !"


@app.route("/health")
def health():
    return jsonify(status="ok", service="webapp")


if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_HOST", "127.0.0.1"), port=8000)
