import os

from flask import Flask, jsonify

from app.calc import uptime_percent

app = Flask(__name__)


@app.get("/")
def index():
    version = os.environ.get("APP_VERSION", "dev")
    return f"Hello from build #{version}. Sample uptime: {uptime_percent(97, 100)}%\n"


@app.get("/health")
def health():
    if not os.environ.get("APP_SECRET"):
        return jsonify(status="error", reason="APP_SECRET missing"), 503
    return jsonify(status="ok", version=os.environ.get("APP_VERSION", "dev"))


if __name__ == "__main__":
    if not os.environ.get("APP_SECRET"):
        print("WARNING: APP_SECRET is not set, /health will return 503", flush=True)
    app.run(host="0.0.0.0", port=5000)
