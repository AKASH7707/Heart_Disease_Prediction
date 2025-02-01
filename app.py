from flask import Flask, request, render_template
from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import json
import numpy as np

app = Flask(__name__)

with open("models/model_metadata.json", "r") as f:
    metadata = json.load(f)
print("Expected feature names:", metadata["feature_names"])

# Load the model, LOR mean, scaler, and encoder for prediction
model = joblib.load("models/heart_disease_model.pkl")
print("Model loaded successfully")

# Home route
@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Example raw data (replace with actual values for prediction) 
        data = [[request.form['sex'], request.form['chest_pain_type'], request.form['exercise_angina'], request.form['slope_of_st'], request.form['vessels_fluro'], request.form['thallium']]]
        # Ensure the input data is a DataFrame with the same columns as the training data
        columns = metadata["feature_names"]
        df = pd.DataFrame(data, columns=columns)

        # Use the loaded model to make predictions
        prediction = model.predict(df)  # Preprocessing is handled automatically
        probability = model.predict_proba(df)

        # Display probabilities for clarity
        prob_class_0 = probability[0][0] * 100
        prob_class_1 = probability[0][1] * 100
        # Display the prediction
        if prediction[0] == 1:
            prediction_text = f"The person is likely to have heart disease. Probability of heart disease : {prob_class_1:.2f} %"
        else:
            prediction_text = f"The person is unlikely to have heart disease. Probability of no heart disease : {prob_class_0:.2f} %"
   
        
        return render_template('index.html', prediction_text=prediction_text)
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
