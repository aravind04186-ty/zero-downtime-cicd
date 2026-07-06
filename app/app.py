from flask import Flask, render_template
import socket
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        version=VERSION
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)