import pandas as pd
import random

rows = []

for _ in range(500):
    skills_match = random.randint(30, 100)
    projects = random.randint(0, 6)
    internships = random.randint(0, 4)
    certifications = random.randint(0, 5)
    github = random.choice([0, 1])
    resume_score = random.randint(40, 100)

    # Hiring logic (hidden rule for ML to learn)
    hired = 1 if (
        skills_match > 65 and
        resume_score > 70 and
        (projects + internships) >= 3
    ) else 0

    rows.append([
        skills_match,
        projects,
        internships,
        certifications,
        github,
        resume_score,
        hired
    ])

df = pd.DataFrame(rows, columns=[
    "skills_match",
    "projects",
    "internships",
    "certifications",
    "github",
    "resume_score",
    "hired"
])

df.to_csv("data/synthetic_hiring_data.csv", index=False)

print("CSV dataset created successfully!")
