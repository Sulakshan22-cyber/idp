import argparse
import sys
import time
from pathlib import Path

import joblib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from raspberry_pi.temperature import get_temperature
from raspberry_pi.vibration import get_vibration
from raspberry_pi.current import get_current
from raspberry_pi.rpm import get_rpm
from raspberry_pi.lcd import display
from raspberry_pi.leds import healthy, warning, fault
from raspberry_pi.buzzer import on, off
from raspberry_pi.logger import save

MODEL_PATH = PROJECT_ROOT / "model" / "motor_rf_model.pkl"
ENCODER_PATH = PROJECT_ROOT / "model" / "label_encoder.pkl"


def load_model():
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder


def run_cycle(model, encoder):
    temp = get_temperature()
    vib = get_vibration()
    curr = get_current()
    rpm = get_rpm()

    sample = [[temp, vib, curr, rpm]]
    prediction = model.predict(sample)
    status = encoder.inverse_transform(prediction)[0]

    print("--------------------------------")
    print("Temperature :", temp)
    print("Vibration   :", vib)
    print("Current     :", curr)
    print("RPM         :", rpm)
    print("Status      :", status)

    if status == "Healthy":
        healthy()
        off()
    elif status == "Warning":
        warning()
        off()
    else:
        fault()
        on()

    display(temp, vib, curr, rpm, status)
    save(temp, vib, curr, rpm, status)
    return status


def main():
    parser = argparse.ArgumentParser(description="Run the motor monitoring loop")
    parser.add_argument("--demo", action="store_true", help="Run a single cycle and exit")
    args = parser.parse_args()

    model, encoder = load_model()
    print("AI Predictive Maintenance Started...")

    if args.demo:
        run_cycle(model, encoder)
        return

    while True:
        run_cycle(model, encoder)
        time.sleep(1)


if __name__ == "__main__":
    main()