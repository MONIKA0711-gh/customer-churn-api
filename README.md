# ChurnIQ – Customer Churn Prediction System

ChurnIQ is an end-to-end customer churn prediction application that uses Machine Learning to estimate whether a customer is likely to leave a service.

The project combines Machine Learning, Python backend development, REST APIs, MySQL database integration, and a web-based frontend into a single application.

---

## 📌 Project Overview

Customer churn is an important business problem where identifying customers who are likely to leave can help organizations take appropriate retention actions.

ChurnIQ accepts customer demographic, service, contract, and billing information and uses a trained Machine Learning model to predict:

- Whether the customer is likely to churn
- The probability of churn
- The prediction history stored in MySQL

The application provides a web interface for entering customer information and viewing prediction results.

---

## 🎯 Problem Statement

Customer churn can negatively affect business revenue and customer retention.

The objective of this project is to develop a Machine Learning-based system that can analyze customer information and predict the likelihood of churn through a REST API and web interface.

---

## 🎯 Objectives

- Clean and preprocess customer data
- Perform exploratory data analysis
- Train and compare multiple Machine Learning models
- Evaluate models using classification metrics
- Analyze classification thresholds
- Build a reusable Machine Learning pipeline
- Develop a REST API using FastAPI
- Validate API requests using Pydantic
- Store prediction results in MySQL
- Develop a frontend using HTML, CSS, and JavaScript
- Display churn probability and prediction history

---

## 🚀 Features

### Machine Learning

- Data cleaning and preprocessing
- Categorical feature encoding
- Numerical feature handling
- Model training and evaluation
- Logistic Regression
- Random Forest
- XGBoost
- ROC-AUC evaluation
- Threshold analysis
- Saved Scikit-learn pipeline

### Backend

- FastAPI REST API
- Pydantic request validation
- ML prediction endpoint
- Health-check endpoint
- Prediction history endpoint
- CORS configuration
- SQLAlchemy database integration

### Database

- MySQL database
- Prediction history storage
- Customer information storage
- Churn probability storage

### Frontend

- Responsive web interface
- Customer information form
- Churn probability visualization
- Prediction result page
- Prediction history table
- API integration using JavaScript Fetch API

---

## 🛠️ Technology Stack

### Programming

- Python
- JavaScript
- HTML
- CSS
- SQL

### Machine Learning

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib

### Backend

- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- PyMySQL

### Database

- MySQL

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Inspection
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preparation
   ↓
Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Threshold Analysis
   ↓
Select Final Model
   ↓
Save ML Pipeline
   ↓
FastAPI Prediction Service
📊 Dataset

The project uses the IBM Telco Customer Churn dataset.

Dataset Size

Original dataset:

7043 rows × 21 columns

After data cleaning:

7010 rows × 20 columns

The customerID column was removed because it does not provide useful predictive information.

Missing values in TotalCharges were handled after converting the column to numeric format.

Target Variable

The target variable is:

Churn

where:

0 → Customer stays
1 → Customer churns
🤖 Model Evaluation

Three Machine Learning models were evaluated:

Model	Accuracy	Precision	Recall	F1 Score	ROC-AUC
Logistic Regression	81.55%	68.65%	55.83%	61.58%	85.12%
Random Forest	79.74%	66.09%	48.29%	55.81%	82.86%
XGBoost	79.84%	65.65%	50.09%	56.82%	84.67%

Based on the evaluation performed in this project, Logistic Regression was selected as the final prediction model.

The complete preprocessing and model pipeline was saved using Joblib and loaded by the FastAPI backend during prediction.

🎚️ Threshold Analysis

The default classification threshold of 0.50 was analyzed to understand how different thresholds affect precision, recall, and F1 score.

  Threshold	 Precision	Recall	F1 Score
    0.30	   54.02%	75.94%	63.13%
    0.35	   57.22%	71.81%	63.69%
    0.40	   59.87%	65.35%	62.49%
    0.45	   64.44%	60.50%	62.41%
    0.50	   68.65%	55.83%	61.58%

A threshold of 0.35 was selected for the application because it produced the highest F1 score among the tested thresholds.

The threshold is applied in the prediction service rather than modifying the trained model itself.

🔌 API Endpoints
Root
GET /

Returns a message confirming that the API is running.

Health Check
GET /health

Used to check whether the backend service is healthy.

Predict Churn
POST /predict-churn

Accepts customer information and returns the churn prediction and probability.

Example response:

{
  "churn_prediction": 1,
  "churn_probability": 0.8199,
  "result": "Customer is likely to churn"
}
Prediction History
GET /predictions

Returns previously stored prediction records from MySQL.

🗄️ Database

The application uses MySQL to store prediction history.

Database
customer_churn_db
Main Table
predictions

The table stores information including:

Customer gender
Tenure
Contract
Internet service
Online security
Technical support
Payment method
Monthly charges
Total charges
Churn prediction
Churn probability
Paperless billing

🏗️ Project Structure

customer-churn-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   │
│   ├── schemas/
│   │   └── prediction.py
│   │
│   └── services/
│       └── prediction_service.py
│
├── artifacts/
│   └── churn_pipeline.joblib
│
├── data/
│   ├── raw/
│   └── processed/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── ml/
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── eda.py
│   ├── prepare_data.py
│   ├── preprocessing.py
│   ├── test_preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── threshold_analysis.py
│   └── save_model.py
│
├── .gitignore
├── README.md
└── requirements.txt

⚙️ Installation and Setup

1. Clone the Repository

Clone the GitHub repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>

Navigate into the project:

cd customer-churn-api

2. Create a Virtual Environment

For Windows:

python -m venv .venv

Activate the virtual environment:

.venv\Scripts\activate

3. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

4. Set Up MySQL

Create the database in MySQL:

CREATE DATABASE customer_churn_db;

The application uses MySQL through SQLAlchemy and PyMySQL.

5. Configure the Database

Configure the database connection according to your local MySQL setup.

Do not commit database passwords, API keys, or other credentials to GitHub.

6. Start the FastAPI Backend

From the project root, run:

uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

Swagger API Documentation

FastAPI automatically provides interactive API documentation at:
http://127.0.0.1:8000/docs

7. Run the Frontend

Open the frontend/index.html file using a local development server such as the VS Code Live Server extension.

The frontend communicates with the FastAPI backend to submit customer information and receive predictions.

🔄 Application Flow

User
  ↓
Frontend Form
  ↓
JavaScript Fetch API
  ↓
FastAPI /predict-churn
  ↓
Pydantic Validation
  ↓
ML Preprocessing Pipeline
  ↓
Logistic Regression Model
  ↓
Churn Probability
  ↓
Threshold = 0.35
  ↓
Prediction Result
  ↓
MySQL
  ↓
Prediction History

🔮 Future Enhancements

Deploy the application for public access
Add authentication and authorization
Add customer-level analytics
Add interactive business dashboards
Add model monitoring
Add automated model retraining
Improve frontend filtering and search
Add cloud deployment

📌 Current Status

The application currently supports:

Machine Learning-based customer churn prediction
FastAPI REST APIs
Pydantic request validation
MySQL prediction storage
Frontend customer input
Churn probability visualization
Prediction result display
Prediction history

The application is currently configured for local execution.

👩‍💻 Author

Monika
B.Tech – Computer Science and Engineering (AI & ML)