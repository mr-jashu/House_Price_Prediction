<!-- # HousePricePrediction

This project provides a modular machine learning pipeline for house price prediction with a Streamlit interface.

## Project Structure

- `data/raw` for raw datasets
- `notebooks` for EDA notebooks
- `src` for source modules (components, pipeline, entity)
- `artifacts` for trained model and preprocessor files
- `app.py` for Streamlit app entrypoint

## Run

1. Train the model artifacts:

```bash
python src/pipeline/training_pipeline.py
```

2. Start Streamlit app:

```bash
streamlit run app.py
``` -->

# HousePricePrediction

### Instructions:
1.  Create a file named `README.md` in your root folder (`HousePricePrediction`).
2.  Paste the content below into that file.

```markdown
# 🏠 End-to-End House Price Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-1.3.0-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red?style=for-the-badge&logo=streamlit)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7.6-green?style=for-the-badge&logo=xgboost)

An industry-grade, production-ready Machine Learning application that predicts house prices based on various features. This project demonstrates a complete ML lifecycle, from data ingestion and transformation to model training and web application deployment.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)

---

## 🎯 Project Overview

This project solves a regression problem: predicting house prices. Unlike typical notebook-based projects, this application is built with a **modular coding structure**, making it scalable, maintainable, and ready for production environments.

The pipeline handles:
1.  **Synthetic Data Generation:** Generates realistic data if raw data is missing.
2.  **Data Transformation:** Imputation and scaling using `sklearn` pipelines.
3.  **Model Training:** Evaluates Linear Regression, Random Forest, and XGBoost.
4.  **Hyperparameter Tuning:** Automatically selects the best model using `GridSearchCV`.
5.  **Web Interface:** A user-friendly frontend built with Streamlit.

---

## 🛠 Tech Stack

- **Language:** Python 3.10
- **Framework:** Streamlit
- **ML Libraries:** Scikit-learn, XGBoost, Pandas, NumPy
- **Deployment:** Render
- **Logging & Exception:** Custom implemented Python logging

---

## 🏗 Project Architecture

The project follows a modular design pattern often used in enterprise MLOps:

1.  **Data Ingestion:** Reads/generates data and splits it into train/test sets.
2.  **Data Transformation:** Creates a preprocessing pipeline (Imputation + Scaling) and saves it as a pickle file.
3.  **Model Trainer:** Trains multiple models, tunes hyperparameters, and saves the best model.
4.  **Prediction Pipeline:** Loads the saved model and preprocessor to make real-time predictions on user input.

---

## ✨ Features

- **Modular Code:** Clean separation of concerns (`components`, `pipeline`, `entity`).
- **Custom Logging:** Robust logging system to track execution flow and errors.
- **Custom Exception Handling:** Detailed error messages for debugging.
- **Production Ready:** Easily deployable on cloud platforms like Render or AWS.
- **Interactive UI:** Sliders and input fields for easy data entry.

---

## 💻 Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/HousePricePrediction.git
cd HousePricePrediction
```

### 2. Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Run the Training Pipeline
This command initiates the data ingestion, transformation, and model training. It will generate the `artifacts` folder containing your trained model (`model.pkl`) and preprocessor (`preprocessor.pkl`).

```bash
python src/pipeline/training_pipeline.py
```

### Step 2: Run the Streamlit App
Once the model is trained, launch the web application:

```bash
streamlit run app.py
```

The application should open automatically in your default web browser at `http://localhost:8501`.

---

## 🌐 Deployment

This project is configured for deployment on **Render**.

1.  Push your code to a GitHub repository.
2.  Log in to [Render.com](https://render.com) and create a new **Web Service**.
3.  Connect your GitHub repository.
4.  Set the **Build Command**:
    ```bash
    pip install -r requirements.txt
    ```
5.  Set the **Start Command**:
    ```bash
    streamlit run app.py
    ```
6.  Click **Deploy Web Service**.

---

## 📂 Project Structure

```text
HousePricePrediction/
│
├── artifacts/               # Generated model files (model.pkl, preprocessor.pkl)
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── test.csv
│   └── train.csv
│
├── logs/                    # Log files for tracking runs
│
├── notebooks/               # Jupyter notebooks for EDA
│   └── EDA.ipynb
│
├── src/                     # Source Code
│   ├── components/          # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── entity/              # Configuration entities
│   │   └── config_entity.py
│   │
│   ├── pipeline/            # Execution scripts
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── exception.py         # Custom exception class
│   ├── logger.py            # Logging configuration
│   └── utils.py             # Utility functions
│
├── app.py                   # Streamlit Application Entry Point
├── requirements.txt         # Project Dependencies
├── setup.py                 # Package Setup
└── README.md                # Project Documentation
```

---

## 👨‍💻 Author

**Your Name**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/your-username)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```