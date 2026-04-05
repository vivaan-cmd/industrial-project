import joblib
import numpy as np
import pandas as pd

# Load trained model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_hiring_probability(features: dict) -> float:
    """
    Predicts the probability of a candidate being hired.

    Args:
        features (dict): {
            "skills_match": int,       # 0-100 percentage
            "projects": int,           # count of projects
            "internships": int,        # count of internships
            "certifications": int,     # count of certifications
            "github": int,             # 1 if GitHub present, else 0
            "resume_score": int        # composite score 0-100
        }

    Returns:
        float: Hiring probability as a percentage (e.g. 78.45)
    """

    # Convert to DataFrame to preserve feature names for the scaler
    feature_df = pd.DataFrame([features])

    # Scale features using the saved scaler
    feature_array_scaled = scaler.transform(feature_df)

    # Predict probability of class 1 (hired)
    probability = model.predict_proba(feature_array_scaled)[0][1]

    return round(probability * 100, 2)


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
