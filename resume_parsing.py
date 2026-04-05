import pdfplumber
import docx
import os


def extract_text(file_path: str) -> str:
    """
    Extracts and returns lowercased text from a resume file.
    Supports: .pdf, .docx, .txt
    """
    text = ""

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Resume file not found: {file_path}")

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        raise ValueError(f"Unsupported file type: {file_path}. Use .pdf, .docx, or .txt")

    return text.lower()
