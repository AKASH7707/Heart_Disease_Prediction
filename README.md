# Heart_Disease_Prediction

## 1. Introduction

The dataset is taken from kaggle "https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction"

### 1.1 Problem Statement

The leading cause of death in the developed world is heart disease. Therefore there needs to be work done to help prevent the risks of of having a heart attack or stroke.Use this dataset to predict which patients are most likely to suffer from a heart disease in the near future using the features given.

### 1.2 Goals and Objectives

- The goal here is to creata a machine learning model to find the heart disease based on the datas given.
- Then deploy the model in a website for easier access for the users.

### 1.3 Importance of the Project

This project will help doctors to make sure whether the patient have heart disease or not.It can play a crucile role in saving people life.

---
## 2. Project Structure

```
my_project/
├── app.py                   # Main Flask application file
├── requirements.txt         # Python dependencies needed to run the app
├── templates/               # HTML templates for the web pages
│   └── index.html           # Main HTML template for user input and displaying results
├── static/                  # Static files (e.g., CSS, JavaScript)
│   └── styles.css           # Styling for the web interface
│   └── script.js            # javascript for the web interface
├── models/                  # Contains saved models and preprocessing objects
│   ├── heart_disease_model.pkl   # Trained model file
│   └── model_metadata         # meta data about model
└── README.md                # Documentation file describing the project
```

---
## 3. Features
- **Input fields:** Allows users to enter details such as 'Sex', 'Chest pain type', 'Exercise angina', etc.
- **Prediction:** Provides information about a person have Heart disease present or not.
- **User-Friendly Interface:** Interactive and visually appealing UI with input sliders and dynamic feedback.

---

## 4. Installation

### 4.1 Prerequisites

- **Python 3.11.5 or later**
- **pip** (Python package manager)

### 4.2 **Clone the repository:**

    git clone <repository-url>
    cd Heart_Disease_Prediction

### 4.3 **Install dependencies:**

    pip install -r requirements.txt

### 4.3 Run the Flask App:

    flask run

---

## 5. Usage

   - After running the Flask app, open a web browser and go to http://localhost:5000.
   - Enter the relevant input values.
   - Click on the "Predict" button to view your estimated probability of admission.

---

## 6. Model Information

This project uses a Logistic Regression machine learning model trained to estimate heart disease present or not. The model was developed using scikit-learn and saved as heart_disease_model.pkl.

--- 

## 7. License

This project is licensed under the **MIT License**. See LICENSE for more information.

---