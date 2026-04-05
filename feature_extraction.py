import re

# Default skills — used only if no custom skills are provided
DEFAULT_REQUIRED_SKILLS = [
    "python",
    "java",
    "c++",
    "machine learning",
    "data science",
    "sql",
    "flask",
    "numpy",
    "pandas"
]

def extract_features_from_text(text: str, required_skills: list = None) -> dict:
    """
    Converts resume text into ML-ready numerical features.
    
    Args:
        text: Raw resume text (lowercased)
        required_skills: List of skills to match against. Falls back to defaults.
    """

    if required_skills is None:
        required_skills = DEFAULT_REQUIRED_SKILLS

    features = {}

    # 1. Skills Match Percentage
    matched_skills = [skill for skill in required_skills if skill in text]
    features["skills_match"] = int(
        (len(matched_skills) / len(required_skills)) * 100
    ) if required_skills else 0

    # 2. Projects Count
    features["projects"] = len(re.findall(r"\bproject\b", text))

    # 3. Internships Count
    features["internships"] = len(re.findall(r"\bintern(ship)?\b", text))

    # 4. Certifications Count
    features["certifications"] = len(re.findall(r"\b(certification|certified)\b", text))

    # 5. GitHub Presence
    features["github"] = 1 if "github.com" in text else 0

    # 6. Resume Score (Composite)
    resume_score = (
        features["skills_match"] * 0.5 +
        features["projects"] * 5 +
        features["internships"] * 5 +
        features["certifications"] * 3 +
        features["github"] * 5
    )
    features["resume_score"] = int(min(resume_score, 100))

    return features
