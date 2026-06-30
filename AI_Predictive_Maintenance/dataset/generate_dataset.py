from pathlib import Path
import pandas as pd
import random

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "dataset.csv"

rows = []

for _ in range(5000):

    temp = round(random.uniform(25,80),2)
    vibration = round(random.uniform(0.1,4.0),2)
    current = round(random.uniform(0.5,4.5),2)
    rpm = random.randint(800,1800)

    if temp < 45 and vibration < 1.0 and current < 2.0:
        status = "Healthy"

    elif temp < 60 and vibration < 2.5 and current < 3.0:
        status = "Warning"

    else:
        status = "Fault"

    rows.append([temp,vibration,current,rpm,status])

df = pd.DataFrame(rows,
columns=[
"Temperature",
"Vibration",
"Current",
"RPM",
"Status"
])

df.to_csv(OUTPUT_PATH,index=False)

print(df.head())
print(f"Saved dataset to {OUTPUT_PATH}")