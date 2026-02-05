from pipeline import run_resume_pipeline

required_skills = [
    "python",
    "sql",
    "machine learning",
    "flask",
    "data analysis"
]

resume_path = "resumes/resume_sample.txt"

result = run_resume_pipeline(resume_path, required_skills)

print("\n=== Resume-Based Hiring Evaluation ===")
print("Extracted Features:", result["features"])
print("Hiring Probability:", result["hiring_probability"], "%")
print("\nExplanation:")
for line in result["explanation"]:
    print("-", line)
