from resume_parsing import extract_text
from feature_extraction import extract_features_from_text
from inference import predict_hiring_probability


def generate_explanation(features: dict, probability: float) -> list:
    """
    Generates a human-readable explanation of the hiring decision.
    """
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


def run_hiring_pipeline(features: dict) -> dict:
    """
    Runs the hiring pipeline given pre-extracted features.
    Use this when you already have features (e.g. from the API).
    """
    probability = predict_hiring_probability(features)
    explanation = generate_explanation(features, probability)

    return {
        "hiring_probability": probability,
        "features_used": features,
        "explanation": explanation
    }


def run_resume_pipeline(resume_path: str, required_skills: list) -> dict:
    """
    Full end-to-end pipeline: reads a resume file, extracts features,
    predicts hiring probability, and explains the result.
    
    Args:
        resume_path: Path to .pdf, .docx, or .txt resume file
        required_skills: List of skills relevant to the job role
    """
    # Step 1: Extract raw text from resume file
    text = extract_text(resume_path)

    # Step 2: Extract features using job-specific required skills
    features = extract_features_from_text(text, required_skills=required_skills)

    # Step 3: Predict hiring probability
    probability = predict_hiring_probability(features)

    # Step 4: Generate explanation
    explanation = generate_explanation(features, probability)

    return {
        "features": features,
        "hiring_probability": probability,
        "explanation": explanation
    }
