from inference import predict_hiring_probability

def generate_explanation(features, probability):
    explanation = []

    if features["skills_match"] < 60:
        explanation.append("Low skill match with job requirements.")
    else:
        explanation.append("Good alignment with required skills.")

    if features["projects"] < 2:
        explanation.append("Add more real-world projects.")
    else:
        explanation.append("Sufficient project experience.")

    if features["internships"] == 0:
        explanation.append("No internships found.")
    else:
        explanation.append("Internship experience strengthens profile.")

    if features["github"] == 0:
        explanation.append("GitHub profile missing.")
    else:
        explanation.append("GitHub profile adds credibility.")

    explanation.append(f"Overall hiring probability estimated at {probability}%.")

    return explanation


def run_hiring_pipeline(features):
    probability = predict_hiring_probability(features)
    explanation = generate_explanation(features, probability)

    return {
        "hiring_probability": probability,
        "features_used": features,
        "explanation": explanation
    }


# ---------------------------
# Test pipeline
# ---------------------------
from feature_extraction import extract_features
from inference import predict_hiring_probability

def generate_explanation(features, probability):
    explanation = []

    if features["skills_match"] < 60:
        explanation.append("Low skill match with job requirements.")
    else:
        explanation.append("Good alignment with required skills.")

    if features["projects"] < 2:
        explanation.append("Add more real-world projects.")
    else:
        explanation.append("Sufficient project experience.")

    if features["internships"] == 0:
        explanation.append("No internships found.")
    else:
        explanation.append("Internship experience strengthens profile.")

    if features["github"] == 0:
        explanation.append("GitHub profile missing.")
    else:
        explanation.append("GitHub profile adds credibility.")

    explanation.append(f"Overall hiring probability estimated at {probability}%.")

    return explanation


def run_resume_pipeline(resume_path, required_skills):
    # Extract features from resume
    features = extract_features(
        resume_input=resume_path,
        required_skills=required_skills,
        pdf=False   # change to True for PDF
    )

    # Predict hiring probability
    probability = predict_hiring_probability(features)

    # Generate explanation
    explanation = generate_explanation(features, probability)

    return {
        "features": features,
        "hiring_probability": probability,
        "explanation": explanation
    }
