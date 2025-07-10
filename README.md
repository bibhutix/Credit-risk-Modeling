🧠 Credit Risk Modeling using Machine Learning
This project focuses on predicting credit risk categories using machine learning techniques. By analyzing data from both bureau sources and internal product data, the model classifies credit applicants into different risk levels, helping financial institutions make data-driven lending decisions.

🚀 Project Highlights
✅ Processed and analyzed 50,000+ records with 35+ features from diverse sources.

📊 Conducted exploratory data analysis (EDA) to uncover trends, outliers, and correlations.

🤖 Achieved 92% accuracy using machine learning with multiclass classification.

🧪 Applied hyperparameter tuning to boost model performance.

🌐 Deployed using Flask, turning the model into a web application.

📂 Project Structure
php
Copy
Edit
credit-risk-model/
│
├── static/                   # Static assets (CSS, images, etc.)
├── templates/                # HTML templates for Flask app
├── models/                   # Serialized model files (.pkl, .joblib)
├── app.py                    # Flask app script
├── credit_risk_model.ipynb   # Full EDA + model training notebook
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview (this file)
└── utils.py                  # Helper functions (optional)


📈 Machine Learning Pipeline
1) Data Collection
Integrated data from credit bureau and internal product sources.

2) Data Preprocessing

Handled missing values.

Encoded categorical variables.

Feature scaling and engineering.

3) Exploratory Data Analysis (EDA)

Distribution plots, correlation heatmaps.

Feature importance analysis.

4) Modeling

Trained multiple classifiers (Logistic Regression, Random Forest, etc.).

Selected best model based on accuracy and validation performance.

5) Hyperparameter Tuning

Used GridSearchCV / RandomizedSearchCV for optimization.

6) Deployment

Built a simple web interface using Flask.

Users can input credit data and get risk category predictions.
