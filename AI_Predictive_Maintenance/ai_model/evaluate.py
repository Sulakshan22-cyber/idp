import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../dataset/dataset.csv")

X = df[["Temperature","Vibration","Current","RPM"]]

encoder = LabelEncoder()

y = encoder.fit_transform(df["Status"])

X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42)

model = joblib.load("../model/motor_rf_model.pkl")

prediction = model.predict(X_test)

print(classification_report(y_test,prediction))

cm = confusion_matrix(y_test,prediction)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=encoder.classes_
)

disp.plot()

plt.show()