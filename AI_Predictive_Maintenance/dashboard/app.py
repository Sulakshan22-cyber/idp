import json
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, render_template

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_PATH = BASE_DIR / "raspberry_pi" / "motor_log.csv"
LATEST_PATH = BASE_DIR / "raspberry_pi" / "latest.json"

app = Flask(__name__, template_folder=str(BASE_DIR / "dashboard" / "templates"))


def get_latest_reading():
    if LATEST_PATH.exists():
        try:
            with open(LATEST_PATH, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
                return {
                    "temp": payload.get("Temperature", 0),
                    "vib": payload.get("Vibration", 0),
                    "current": payload.get("Current", 0),
                    "rpm": payload.get("RPM", 0),
                    "status": payload.get("Status", "No data"),
                }
        except Exception:
            pass

    if LOG_PATH.exists() and LOG_PATH.stat().st_size > 0:
        try:
            df = pd.read_csv(LOG_PATH)
            if not df.empty:
                latest = df.iloc[-1]
                return {
                    "temp": latest.get("Temperature", 0),
                    "vib": latest.get("Vibration", 0),
                    "current": latest.get("Current", 0),
                    "rpm": latest.get("RPM", 0),
                    "status": latest.get("Status", "No data"),
                }
        except Exception:
            pass

    return {
        "temp": 0,
        "vib": 0,
        "current": 0,
        "rpm": 0,
        "status": "No data",
    }


@app.route("/")
def home():
    data = get_latest_reading()
    return render_template(
        "index.html",
        temp=data["temp"],
        vib=data["vib"],
        current=data["current"],
        rpm=data["rpm"],
        status=data["status"],
    )


@app.route("/api/latest")
def latest():
    return jsonify(get_latest_reading())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)