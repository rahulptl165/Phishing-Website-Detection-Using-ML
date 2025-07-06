from flask import Flask, render_template, request
import joblib
from feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load('../model/neural_network_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    prediction = model.predict([features])[0]
    proba = model.predict_proba([features])[0]
    print("Probabilities:", proba)

    result = 'Phishing Website' if prediction == 1 else 'Legitimate Website'
    return render_template('index.html', url=url, prediction=result, features=features)

if __name__ == '__main__':
    app.run(debug=True)
