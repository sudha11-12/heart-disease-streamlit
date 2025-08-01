



import pandas as pd
df=pd.read_csv('heart disease-csv file.csv')
df

from sklearn.preprocessing import LabelEncoder, StandardScaler
data = df.copy()
data = data.dropna()
le = LabelEncoder()
data["sex"] = le.fit_transform(data["sex"])
scaler = StandardScaler()
df_scaled = scaler.fit_transform(data[["age", "chol"]])
df

import seaborn as sns
import matplotlib.pyplot as plt
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
X = data.drop("target", axis=1)
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

importance = model.coef_[0]
for i, col in enumerate(X.columns):
    print(f"{col}: {importance[i]}")

import matplotlib.pyplot as plt
importance = model.coef_[0]
plt.barh(X.columns, importance)
plt.xlabel("Importance")
plt.title("Feature Importance (Logistic Regression)")
plt.show()

import streamlit as st
st.title("Disease Prediction")
age = st.number_input("Enter Age")
chol = st.number_input("Enter Cholesterol")
if st.button("Predict"):
    input_data = scaler.transform([[age, chol]])
    result = model.predict(input_data)
    st.write("Prediction:", "Positive" if result[0]==1 else "Negative")




