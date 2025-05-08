from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Smart Health Tracker Backend is Running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Received Data:", data)  # Debugging log

        # Ensure keys exist before accessing them
        age = int(data.get("age", 0))
        bmi = float(data.get("bmi", 0))
        activity_level = int(data.get("activity_level", 0))  # Correct key name
        smoking = int(data.get("smoking", 0))
        alcohol = int(data.get("alcohol", 0))
        diet = int(data.get("diet", 0))
        exercise = int(data.get("exercise", 0))

        # Dummy prediction logic (Replace with real model)
        risk = "High Risk" if bmi > 35 else "Low Risk"

        return jsonify({"prediction": risk})

    except Exception as e:
        print("Error:", str(e))  # Print the error in console
        return jsonify({"error": "Invalid data format", "details": str(e)}), 400

import os

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_ENV") == "development"
    app.run(debug=debug_mode)
