import re
import pdfplumber

# -----------------------------
# 1. Extract resume text
# -----------------------------
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text.lower()


def extract_text_from_string(text):
    return text.lower()


# -----------------------------
# 2. Split resume into sections
# -----------------------------
def split_into_sections(text):
    sections = {
        "skills": "",
        "projects": "",
        "experience": "",
        "certifications": ""
    }

    current_section = None

    for line in text.split("\n"):
        line = line.strip()

        if "skill" in line:
            current_section = "skills"
        elif "project" in line:
            current_section = "projects"
        elif "experience" in line or "intern" in line:
            current_section = "experience"
        elif "certificat" in line:
            current_section = "certifications"

        if current_section:
            sections[current_section] += " " + line

    return sections


# -----------------------------
# 3. Smarter skill matching
# -----------------------------
def calculate_skill_match(sections, required_skills):
    score = 0

    for skill in required_skills:
        skill = skill.lower()

        if skill in sections["skills"]:
            score += 2    # strong signal
        elif skill in sections["projects"]:
            score += 1.5
        elif skill in sections["experience"]:
            score += 1

    max_score = len(required_skills) * 2
    return int((score / max_score) * 100) if max_score else 0


# -----------------------------
# 4. Smarter counters
# -----------------------------
def count_projects(project_text):
    return len(re.findall(r"\bproject\b", project_text))


def count_internships(exp_text):
    return len(re.findall(r"\bintern\b", exp_text))


def count_certifications(cert_text):
    return len(re.findall(r"certificat", cert_text))


def has_github(text):
    return 1 if "github.com" in text else 0


# -----------------------------
# 5. Improved resume score
# -----------------------------
def calculate_resume_score(features):
    score = (
        features["skills_match"] * 0.5 +
        min(features["projects"], 5) * 7 +
        min(features["internships"], 3) * 10 +
        min(features["certifications"], 3) * 6 +
        features["github"] * 8
    )
    return min(int(score), 100)


# -----------------------------
# 6. Main feature extractor
# -----------------------------
def extract_features(resume_input, required_skills, pdf=True):
    if pdf:
        text = extract_text_from_pdf(resume_input)
    else:
        text = extract_text_from_string(resume_input)

    sections = split_into_sections(text)

    features = {}
    features["skills_match"] = calculate_skill_match(sections, required_skills)
    features["projects"] = count_projects(sections["projects"])
    features["internships"] = count_internships(sections["experience"])
    features["certifications"] = count_certifications(sections["certifications"])
    features["github"] = has_github(text)
    features["resume_score"] = calculate_resume_score(features)

    return features


# -----------------------------
# 7. Test locally
# -----------------------------
if __name__ == "__main__":
    sample_resume = """
    SKILLS
    Python, SQL, Machine Learning, Flask

    PROJECTS
    Resume Analyzer Project
    Data Analysis Dashboard Project

    EXPERIENCE
    Internship at Tech Startup

    CERTIFICATIONS
    Data Science Certification

    GitHub: https://github.com/example
    """

    required_skills = ["python", "sql", "machine learning", "flask"]

    features = extract_features(sample_resume, required_skills, pdf=False)
    print(features)
