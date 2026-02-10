from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from resume_parsing import extract_text
from feature_extraction import extract_features_from_text
from inference import predict_hiring_probability

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "resume_uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "Resume Hiring Prediction API is Running!"


@app.route("/upload_resume", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # 1️⃣ Extract text
    text = extract_text(file_path)

    # 2️⃣ Extract features
    features = extract_features_from_text(text)

    # 3️⃣ Predict probability
    probability = predict_hiring_probability(features)

    return jsonify({
        "features_extracted": features,
        "hiring_probability": probability
    })


if __name__ == "__main__":
    app.run(debug=True)

