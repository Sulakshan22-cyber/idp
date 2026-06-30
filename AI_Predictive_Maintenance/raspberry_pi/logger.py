import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / "motor_log.csv"
LATEST_FILE = BASE_DIR / "latest.json"


def save(temp, vib, current, rpm, status):
    needs_header = not FILE.exists() or FILE.stat().st_size == 0

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if needs_header:
            writer.writerow([
                "Temperature",
                "Vibration",
                "Current",
                "RPM",
                "Status"
            ])

        writer.writerow([
            temp,
            vib,
            current,
            rpm,
            status
        ])

    payload = {
        "Temperature": temp,
        "Vibration": vib,
        "Current": current,
        "RPM": rpm,
        "Status": status,
    }

    with open(LATEST_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return FILE