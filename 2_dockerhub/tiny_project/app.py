from flask import Flask, jsonify
import socket
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Hello from Video 2 — Docker Hub",
        "image": "sergeiusynin/docker-demo:1.0",
        "container_hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
