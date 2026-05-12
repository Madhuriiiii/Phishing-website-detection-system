from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("phishing_model.pkl")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    features = []

    # Collect input values
    for i in range(31):
        value = request.form[f'feature{i}']
        features.append(int(value))

    # Convert to numpy array
    final_features = np.array(features).reshape(1, -1)

    # Prediction
    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "Legitimate Website"
    else:
        result = "Phishing Website"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)