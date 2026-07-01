import json
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, render_template

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_PATH = BASE_DIR / "raspberry_pi" / "motor_log.csv"
LATEST_PATH = BASE_DIR / "raspberry_pi" / "latest.json"

app = Flask(__name__, template_folder=str(BASE_DIR / "dashboard" / "templates"))


def get_latest_reading():
    """Get the latest sensor reading from JSON file (most recent)"""
    if LATEST_PATH.exists():
        try:
            with open(LATEST_PATH, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
                return {
                    "temp": float(payload.get("Temperature", 0)),
                    "rpm": float(payload.get("RPM", 0)),
                    "status": payload.get("Status", "No data"),
                }
        except Exception as e:
            print(f"Error reading latest.json: {e}")

    if LOG_PATH.exists() and LOG_PATH.stat().st_size > 0:
        try:
            df = pd.read_csv(LOG_PATH)
            if not df.empty:
                latest = df.iloc[-1]
                return {
                    "temp": float(latest.get("Temperature", 0)),
                    "rpm": float(latest.get("RPM", 0)),
                    "status": latest.get("Status", "No data"),
                }
        except Exception as e:
            print(f"Error reading CSV: {e}")

    return {
        "temp": 0,
        "rpm": 0,
        "status": "No data",
    }


@app.route("/")
def home():
    """Render the main dashboard page"""
    data = get_latest_reading()
    return render_template(
        "index.html",
        temp=data["temp"],
        rpm=data["rpm"],
        status=data["status"],
    )


@app.route("/api/latest")
def latest():
    """API endpoint for real-time data (no caching)"""
    response = jsonify(get_latest_reading())
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route("/api/history")
def history():
    """API endpoint for historical data (last 100 readings)"""
    if LOG_PATH.exists() and LOG_PATH.stat().st_size > 0:
        try:
            df = pd.read_csv(LOG_PATH)
            # Return last 100 rows
            recent = df.tail(100).to_dict(orient='records')
            return jsonify({"success": True, "data": recent})
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500

    return jsonify({"success": True, "data": []})


if __name__ == "__main__":
    print("🚀 Starting AI Predictive Maintenance Dashboard...")
    print("📊 Dashboard available at http://localhost:5000")
    print("🔌 API endpoint at http://localhost:5000/api/latest")
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)