# 🏥 Annual Health Insurance Premium Prediction

A **Machine Learning web application** that predicts the **annual health insurance premium** based on personal, financial, and health-related factors.
The application is built using **Python, Scikit-learn, and Streamlit** and provides an interactive interface for users to estimate insurance premiums.

---

# 🚀 Project Overview

Health insurance companies calculate premiums based on multiple risk factors such as age, medical history, lifestyle, and income.
This project uses **machine learning models** to estimate an individual's **annual insurance premium** based on these parameters.

The application allows users to:

* Input personal details
* Select lifestyle and health conditions
* Predict the **estimated annual insurance premium**

---

# ⚙️ Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **Streamlit**

---

# 🧠 Machine Learning Approach

The project uses **two separate models** based on age groups:

| Model       | Age Group |
| ----------- | --------- |
| Young Model | Age ≤ 25  |
| Rest Model  | Age > 25  |

### Feature Engineering

The following transformations were applied:

1. **Medical History Risk Score**

   * Diseases are mapped to a risk score.
   * The score is normalized between **0 and 1**.

| Disease             | Risk Score |
| ------------------- | ---------- |
| Diabetes            | 6          |
| Heart Disease       | 8          |
| High Blood Pressure | 6          |
| Thyroid             | 5          |
| No Disease          | 0          |

2. **Categorical Encoding**

   * One-hot encoding for categorical variables.

3. **Feature Scaling**

   * Numerical features scaled using **MinMaxScaler**.

---

# 📊 Input Features

The model uses the following features:

### Personal Information

* Age
* Gender
* Region
* Marital Status

### Health Information

* BMI Category
* Smoking Status
* Medical History
* Genetic Risk Score

### Financial Information

* Income (Lakhs)
* Income Level
* Number of Dependants
* Insurance Plan

---

# 💻 Web Application

The project includes a **Streamlit web application** where users can:

* Enter personal details
* Select health conditions
* Choose insurance plan
* Predict annual premium

Example output:

```
Estimated Annual Premium: ₹18,620
```

---

# 📂 Project Structure

```
insurance-premium-predictor
│
├── artifacts
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
│
├── app
│   ├── main.py
│   └── prediction_helper.py
│
├── notebooks
│   └── model_training.ipynb
│
├── requirements.txt
└── README.md
```

---

# ▶️ Running the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/insurance-premium-predictor.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```
streamlit run main.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# 📈 Example Prediction

Input:

```
Age: 27
Gender: Male
Region: Northwest
BMI Category: Obesity
Smoking Status: Occasional
Medical History: High Blood Pressure
Income: 6 Lakhs
Dependants: 3
Insurance Plan: Silver
```

Output:

```
Predicted Annual Premium: ₹18,620
```
# 🧠 Machine Learning Model

This project uses a **hybrid machine learning approach** where different models are used for different age groups to improve prediction accuracy.

## Model Strategy

Two separate models are trained:

| Age Group | Model Used |
|-----------|-----------|
| Age ≤ 25 | Linear Regression |
| Age > 25 | XGBoost Regressor |

### Why Two Models?

Insurance pricing patterns vary significantly with age.  
Younger individuals generally have fewer medical risks, and the relationship between features and premium tends to be **more linear**.

For older individuals, multiple complex factors such as medical history, lifestyle, and dependents influence the premium.  
Therefore, a **tree-based model (XGBoost)** is used to capture non-linear relationships.

---

## Feature Engineering

Several feature engineering techniques were applied before training the models.

### 1. Medical History Risk Score

Medical conditions are converted into a **numerical risk score**.

| Disease | Risk Score |
|--------|-----------|
| Diabetes | 6 |
| Heart Disease | 8 |
| High Blood Pressure | 6 |
| Thyroid | 5 |
| No Disease | 0 |

If a user has multiple diseases (example: `diabetes & high blood pressure`), the scores are added and then **normalized between 0 and 1**.


---

### 2. Categorical Encoding

Categorical variables are converted using **One-Hot Encoding**, including:

- Gender
- Region
- BMI Category
- Smoking Status
- Employment Status
- Marital Status

---

### 3. Feature Scaling

Numerical features are scaled using **MinMaxScaler** before being passed to the models.

Features scaled include:

- Age
- Income
- Number of Dependants
- Normalized Medical Risk Score
- Genetic Risk Score

---

## Prediction Pipeline

The prediction process works as follows:

1. User enters personal and health details.
2. Data is preprocessed and converted into model features.
3. Medical history is converted into a normalized risk score.
4. Features are scaled using the saved scaler.
5. Based on age:
   - **Age ≤ 25 → Linear Regression model**
   - **Age > 25 → XGBoost model**
6. The model outputs the **predicted annual insurance premium**.

---





