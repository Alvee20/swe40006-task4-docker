import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "<h1>Hello from Shahbaz's Flask container!</h1>"
        "<p>SWE40006 Deployment Portfolio - Task 4.2</p>"
        f"<p>Served by container ID: {socket.gethostname()}</p>"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
