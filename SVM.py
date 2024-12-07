# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # Support Vector Machine
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('Bhuvneshwar 2022.csv')  # Replace with your dataset path

# Inspect the dataset (uncomment to check)
# print(data.head())
# print(data.info())

# Check for missing values and handle them (if any)
if data.isnull().sum().sum() > 0:
    data.fillna(method='ffill', inplace=True)

# Define the features (X) and the target (y)
# Replace 'Temperature', 'Windspeed', 'Humidity', 'Flood' with your actual column names
X = data[['temp', 'windspeed', 'humidity']]  # Features
y = data['FLOOD']  # Target (binary: 1 if flood occurred, 0 otherwise)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the features (important for SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the SVM model
svm_model = SVC(kernel='linear', random_state=42)  # You can also use 'rbf' for non-linear cases
svm_model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(X_test_scaled)

# Evaluate the model
print("SVM Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the trained model for use in the backend
import joblib
joblib.dump(svm_model, 'flood_risk_svm_model.pkl')
print("Model saved as 'flood_risk_svm_model.pkl'")
