from flask import Flask, request, jsonify
from inference import predict_hiring_probability

app = Flask(__name__)

@app.route("/")
def home():
    return "Hiring Probability API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    probability = predict_hiring_probability(data)

    return jsonify({
        "hiring_probability": probability
    })

if __name__ == "__main__":
    app.run(debug=True)

