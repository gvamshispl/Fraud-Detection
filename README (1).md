---
title: Fraud Detection
emoji: 🦀
colorFrom: green
colorTo: red
sdk: docker
pinned: false
short_description: Credit card fraud detection
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

💳 Credit Card Fraud Detection System
A Machine Learning web application that detects fraudulent financial transactions using a trained Random Forest model. The application is deployed using Streamlit + Docker on Hugging Face Spaces.

🚀 Live Application
🔗 Deployed on Hugging Face:
https://your-space-name.hf.space

📌 Project Overview
Financial fraud detection is a highly imbalanced classification problem where fraudulent transactions represent a very small portion of total transactions.
This project:
Builds a supervised ML model to detect fraud
Handles class imbalance effectively
Optimizes model performance
Deploys the model as a web application
Containerizes the application using Docker

📊 Dataset Information
Dataset Name: Credit Card Fraud Detection Dataset
Dataset Characteristics:
~6+ million transaction records
Highly imbalanced target variable
Binary classification problem (isFraud)

Key Features Used:
Feature	Description
step	Time step of transaction
type	Type of transaction (CASH_OUT, TRANSFER, etc.)
amount	Transaction amount
oldbalanceOrg	Sender balance before transaction
newbalanceOrig	Sender balance after transaction
oldbalanceDest	Receiver balance before transaction
newbalanceDest	Receiver balance after transaction
isFraud	Target variable (1 = Fraud, 0 = Legitimate)

⚙️ Model Details
Algorithm Used: Random Forest Classifier
Hyperparameters:
n_estimators
max_depth
min_samples_split
min_samples_leaf
class_weight="balanced"

Why Random Forest?
Handles nonlinear relationships
Works well with tabular financial data
Robust to overfitting (when tuned properly)
Handles feature importance interpretation

📈 Evaluation Metrics
Because fraud detection is imbalanced, we focused on:
Precision
Recall
F1-Score
Confusion Matrix
Precision-Recall Curve
These metrics ensure the model correctly detects fraud while minimizing false alarms.

🧠 Model Training Pipeline
Data Cleaning (drop nulls & duplicates)
Label Encoding for transaction type
Feature Selection
Train-Test Split (Stratified)
Model Training
Performance Evaluation
Model Serialization using joblib

🖥️ Web Application
Built using Streamlit, allowing users to:
Enter transaction details
Get fraud probability
View prediction result instantly

🐳 Deployment
The application is deployed using:
Docker
Hugging Face Spaces
CPU Basic environment

🛠️ Tech Stack
Python
Pandas
Scikit-learn
Streamlit
Docker
Hugging Face Spaces
Joblib
