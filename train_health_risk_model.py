import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Load dataset
try:
    data = pd.read_csv("health_data.csv")
    print("✅ Dataset Loaded Successfully")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

# Define features and target
X = data[["age", "bmi", "activity_level", "smoking", "alcohol", "diet", "exercise"]]
y = data["high_risk"]  # 1 = High Risk, 0 = Low Risk

# Handle Imbalanced Data
smote = SMOTE(random_state=42)
X, y = smote.fit_resample(X, y)

# Normalize Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
accuracy = model.score(X_test, y_test) * 100
print(f"🎯 Model Accuracy: {accuracy:.2f}%")

# Feature Importance
feature_names = ["age", "bmi", "activity_level", "smoking", "alcohol", "diet", "exercise"]
print("📊 Feature Importances:", dict(zip(feature_names, model.feature_importances_)))

# Save Model & Scaler
with open("health_risk_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model and Scaler Saved Successfully!")
