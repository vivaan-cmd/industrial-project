from flask import Flask, request, jsonify
from resume_parsing import extract_text
from feature_extraction import extract_features
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/parse_resume", methods=["POST"])
def parse_resume():
    file = request.files["resume"]
    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    text = extract_text(path)
    features = extract_features(text)

    return jsonify(features)
