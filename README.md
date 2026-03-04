# ❤️ Heart Disease Prediction Web App

A Machine Learning web application that predicts the risk of heart disease based on patient health parameters such as age, blood pressure, cholesterol level, ECG results, and heart rate.

The project demonstrates the **complete Machine Learning workflow** from data preprocessing to building an interactive web application using **Streamlit**.

---

# 🚀 Live Demo

https://heart-disease-predictor-rnp5jktjbbulijqwh465yk.streamlit.app/

---

# 📸 Application Preview

### 🖥️ Dashboard

![Heart Disease App](images/app_dashboard.png)


# 🧠 Machine Learning Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
Model Training (Logistic Regression)
      ↓
Model Evaluation
      ↓
Streamlit Web App Deployment
```

---

# 📊 Model Performance

| Metric           | Score |
| ---------------- | ----- |
| Accuracy         | 86%   |
| ROC-AUC Score    | 0.93  |
| Cross Validation | 0.84  |

These metrics show the model performs well in distinguishing between patients with and without heart disease.

---

# 🧾 Input Features

The model predicts heart disease risk using the following health parameters:

* Age
* Blood Pressure
* Cholesterol Level
* Fasting Blood Sugar
* Maximum Heart Rate
* ST Depression (Oldpeak)
* Gender
* Chest Pain Type
* Resting ECG Result
* Exercise Induced Angina
* ST Slope

---

# 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

# 📂 Project Structure

```text
Heart-Disease-Predictor
│
├── heartapp.py
├── heart_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
└── notebook.ipynb
```

---

# ▶️ Installation & Running the App

### 1️⃣ Clone the repository

```bash
git clone https://github.com/johaibakhtar/Heart-Disease-Predictor.git
```

### 2️⃣ Navigate to project folder

```bash
cd Heart-Disease-Predictor
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run heartapp.py
```

---

# 📈 Future Improvements

* Add advanced ML models (Random Forest, XGBoost)
* Improve UI/UX design
* Deploy the application online
* Add health insights visualization

---

# ⚠️ Disclaimer

This tool is created for **educational purposes only** and should not be used as a substitute for professional medical advice.

---

# 👨‍💻 Author

**Johaib Akhtar**

If you like this project, consider giving it a ⭐ on GitHub!
