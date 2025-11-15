# 🩺 Diabetes Prediction Model

A Machine Learning-based **Diabetes Prediction System** that uses key health metrics to determine whether a person is at risk of diabetes. This project leverages supervised learning techniques and provides an interactive, user-friendly interface for real-time predictions.

---

## 🚀 Project Overview

This project provides an intelligent and simple way to predict diabetes using essential medical parameters like **glucose level, BMI, blood pressure, and age**. It uses a trained machine learning model and offers a clean UI for easy input and prediction.

### 📌 Model Performance

* **Training Accuracy:** 78%
* **Test Accuracy:** 77%

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge)](https://diabetes-prediction-model-mauve.vercel.app/)

---

## 🧠 Machine Learning Model

* **Task Type:** Supervised Classification
* **Algorithms Used:** Logistic Regression / SVM
* **Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`

---

## 📸 Screenshots

<img src="screenshort/front.png" alt="Diabetes Prediction GUI" width="800"/>

---

## 📊 Dataset Details

This system is trained on the **Pima Indians Diabetes Dataset**, a widely used dataset for binary diabetes prediction.

### 🔍 Dataset Summary

* **Source:** Kaggle – Pima Indians Diabetes Database
* **Total Records:** 768
* **Type:** Binary Classification

### 📂 Features

| Feature                  | Description                      |
| ------------------------ | -------------------------------- |
| Pregnancies              | Number of times pregnant         |
| Glucose                  | Plasma glucose concentration     |
| BloodPressure            | Diastolic blood pressure (mm Hg) |
| SkinThickness            | Triceps skin fold thickness (mm) |
| Insulin                  | 2-hour serum insulin (mu U/ml)   |
| BMI                      | Body Mass Index                  |
| DiabetesPedigreeFunction | Diabetes pedigree function       |
| Age                      | Age in years                     |
| Outcome                  | 0 = Non-diabetic, 1 = Diabetic   |

---

## 💻 Quick Start – Single Command Installation

### ✅ Prerequisites

* Python 3.7+
* `pip` package manager

### 🖥️ One-Line Setup & Run

#### **Windows (PowerShell / CMD):**

```
git clone https://github.com/iGufrankhan/Diabetes_Prediction_Model.git && cd Diabetes_Prediction_Model && pip install -r requirements.txt && python app.py
```

#### **Linux / macOS:**

```
git clone https://github.com/iGufrankhan/Diabetes_Prediction_Model.git && cd Diabetes_Prediction_Model && pip install -r requirements.txt && python app.py
```

#### **Using Python3 explicitly:**

```
git clone https://github.com/iGufrankhan/Diabetes_Prediction_Model.git && cd Diabetes_Prediction_Model && pip3 install -r requirements.txt && python3 app.py
```

### 📍 What This Command Does

1. Clones the repository
2. Navigates into the project directory
3. Installs all dependencies
4. Runs the application

➡️ App starts at **[http://localhost:5000](http://localhost:5000)**

---

## 🎯 Features

* ✨ **Real-time Prediction** with instant results
* 🎨 **Clean & Interactive UI**
* 📊 **Data Visualization**
* 📱 **Responsive Layout**
* ⚡ **Fast Model Inference**

---

## 🏗️ Project Structure

```
Diabetes_Prediction_Model/
│
├── app.py                  # Main application file
├── model.pkl               # Trained ML model
├── diabetes.csv            # Dataset
├── requirements.txt        # Dependencies
├── screenshort/
│   └── front.png           # Screenshot
├── templates/
│   └── index.html          # Frontend template
├── static/
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
└── README.md               # Project documentation
```

---

## 🧪 Model Training Pipeline

* **Preprocessing:** Handling missing values, scaling
* **Split:** 80% training, 20% testing
* **Model Comparison:** Logistic Regression vs SVM
* **Hyperparameter Tuning:** Grid Search
* **Metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC

### 📈 Performance Summary

| Metric            | Score |
| ----------------- | ----- |
| Training Accuracy | 78%   |
| Test Accuracy     | 77%   |
| Precision         | 75%   |
| Recall            | 72%   |
| F1-Score          | 73%   |

---

## 🐛 Troubleshooting

Common commands:

```
python --version
pip install --upgrade pip
pip install -r requirements.txt -v
python app.py --debug
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Add improvements
4. Commit changes
5. Submit a Pull Request

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Gufran Khan**

* GitHub: @iGufrankhan
* LinkedIn: *(Add your LinkedIn profile link)*

---

## ⚠️ Disclaimer

> This project is for **educational and informational** purposes only and should not be used as a substitute for professional medical advice.

---

## 🙏 Acknowledgments

* Pima Indians Diabetes Dataset
* scikit-learn community
* All supporters & contributors

---

## 📧 Contact

Have questions? Found an issue?
Feel free to reach out or open a GitHub issue.
