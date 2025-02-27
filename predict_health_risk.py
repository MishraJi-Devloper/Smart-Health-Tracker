import pickle
import numpy as np
import pandas as pd

# Load the trained model and scaler
try:
    with open("health_risk_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    print("✅ Model and scaler loaded successfully")
except Exception as e:
    print(f"❌ Error loading model or scaler: {e}")
    exit()

# Get user input with validation
def get_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"❌ Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

user_input = {
    "age": get_input("Enter Age", 1, 120),
    "bmi": get_input("Enter BMI", 10, 50),
    "activity_level": get_input("Enter Activity Level", 0, 5),
    "smoking": get_input("Enter Smoking (0-No, 1-Yes)", 0, 1),
    "alcohol": get_input("Enter Alcohol (0-No, 1-Yes)", 0, 1),
    "diet": get_input("Enter Diet Quality (1-Bad to 5-Excellent)", 1, 5),
    "exercise": get_input("Enter Exercise Frequency per Week", 0, 5),
}

# Convert input to DataFrame with correct feature names
user_data_df = pd.DataFrame([user_input])

# Normalize the input
user_data_scaled = scaler.transform(user_data_df)

# Predict
risk_score = model.predict_proba(user_data_scaled)[0][1]  # Probability of High Risk
threshold = 0.45  # Adjust threshold for better prediction
prediction = 1 if risk_score >= threshold else 0

risk = "High Risk ❌" if prediction == 1 else "Low Risk ✅"
print(f"🔍 Health Risk Prediction: {risk}")
