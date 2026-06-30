# Predictive Maintenance System for an Electrical Motor

This project demonstrates a predictive maintenance workflow for an electrical motor using a Raspberry Pi 4. It generates synthetic sensor data, trains a machine learning classifier, runs a monitoring loop, logs readings, and serves a simple dashboard.

## Features
- Synthetic dataset generation for motor health states
- Random Forest classifier training
- Real-time monitoring loop with simulated or hardware-backed sensors
- Logging to CSV for historical analysis
- Flask dashboard to view the latest motor status

## Hardware
- Raspberry Pi 4
- DS18B20 temperature sensor
- ADXL345 vibration sensor
- ACS712 current sensor
- ADS1115 analog input board
- IR RPM sensor
- 20x4 LCD display
- Buzzer
- LEDs

## Setup
Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Run the project
Generate the dataset:

```bash
python dataset/generate_dataset.py
```

Train the model:

```bash
python ai_model/train_model.py
```

Run one monitoring cycle (demo mode):

```bash
python raspberry_pi/main.py --demo
```

Run the continuous monitoring loop:

```bash
python raspberry_pi/main.py
```

Start the dashboard:

```bash
python dashboard/app.py
```

Open the dashboard at:

```text
http://localhost:5000
```

## Prediction example
You can also test a single prediction manually:

```bash
python ai_model/predict.py --temp 42.5 --vibration 0.8 --current 1.6 --rpm 1450
```