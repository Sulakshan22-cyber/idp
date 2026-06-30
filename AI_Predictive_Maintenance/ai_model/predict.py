from pathlib import Path
import argparse
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "motor_rf_model.pkl"
ENCODER_PATH = BASE_DIR / "model" / "label_encoder.pkl"


def predict(sample):
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    features = pd.DataFrame([sample], columns=["Temperature", "Vibration", "Current", "RPM"])
    prediction = model.predict(features)
    return encoder.inverse_transform(prediction)[0]


def main():
    parser = argparse.ArgumentParser(description="Predict motor health status")
    parser.add_argument("--temp", type=float, default=42.5)
    parser.add_argument("--vibration", type=float, default=0.82)
    parser.add_argument("--current", type=float, default=1.6)
    parser.add_argument("--rpm", type=int, default=1450)
    args = parser.parse_args()

    sample = [args.temp, args.vibration, args.current, args.rpm]
    print(predict(sample))


if __name__ == "__main__":
    main()