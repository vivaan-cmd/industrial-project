import joblib
import numpy as np
import pandas as pd

# Load trained model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_hiring_probability(features: dict):
    """
    features = {
        "skills_match": 75,
        "projects": 3,
        "internships": 1,
        "certifications": 2,
        "github": 1,
        "resume_score": 80
    }
    """

    # Convert input to DataFrame (keeps feature names)
    feature_df = pd.DataFrame([features])

    # Scale features
    feature_array_scaled = scaler.transform(feature_df)

    # Predict probability (class 1 = hired)
    probability = model.predict_proba(feature_array_scaled)[0][1]

    return round(probability * 100, 2)


# Test the function
if __name__ == "__main__":
    sample_input = {
        "skills_match": 70,
        "projects": 2,
        "internships": 1,
        "certifications": 1,
        "github": 1,
        "resume_score": 78
    }

    result = predict_hiring_probability(sample_input)
    print(f"Hiring Probability: {result}%")
