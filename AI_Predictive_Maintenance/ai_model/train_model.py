from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder

import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "dataset" / "dataset.csv"
MODEL_DIR = BASE_DIR / "model"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATASET_PATH)

X = df[[
"Temperature",
"RPM"
]]

encoder = LabelEncoder()

y = encoder.fit_transform(df["Status"])

X_train,X_test,y_train,y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model = RandomForestClassifier(

n_estimators=200,

max_depth=10,

random_state=42

)

model.fit(X_train,y_train)

accuracy=model.score(X_test,y_test)

print("Accuracy:",accuracy)

joblib.dump(model, MODEL_DIR / "motor_rf_model.pkl")

joblib.dump(encoder, MODEL_DIR / "label_encoder.pkl")

print(f"Model Saved to {MODEL_DIR}")