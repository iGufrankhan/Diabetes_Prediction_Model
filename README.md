🩺 Diabetes Prediction Model
A Machine Learning-based Diabetes Prediction System that uses health metrics to predict whether a person is likely to have diabetes. This model was built, trained, and evaluated with an accuracy of 77%, making it a helpful tool for early prediction and awareness.

🚀 Project Overview
This project aims to provide an intelligent and simple way to predict diabetes using a supervised learning model. Given input features like glucose level, BMI, age, and other health indicators, the model predicts the likelihood of diabetes.
Model Performance:

✅ Training Accuracy: 78%
✅ Test Accuracy: 77%

🔗 Live Demo: https://diabetes-prediction-model-mauve.vercel.app/

🧠 Machine Learning Model

Type: Supervised Classification
Model Used: Logistic Regression / SVM
Libraries: scikit-learn, pandas, numpy, matplotlib, seaborn


📸 Screenshots
<img src="screenshort/front.png" alt="Diabetes Prediction GUI" width="800"/>

📊 Dataset Details
The model is trained using the Pima Indians Diabetes Dataset, which is publicly available and widely used for binary classification tasks.

Source: Kaggle - Pima Indians Diabetes Database
Records: 768 instances
Features:

FeatureDescriptionPregnanciesNumber of times pregnantGlucosePlasma glucose concentrationBloodPressureDiastolic blood pressure (mm Hg)SkinThicknessTriceps skin fold thickness (mm)Insulin2-Hour serum insulin (mu U/ml)BMIBody mass index (weight in kg/(height in m)²)DiabetesPedigreeFunctionDiabetes pedigree functionAgeAge in yearsOutcomeClass variable (0 = Non-diabetic, 1 = Diabetic)

💻 Quick Start - Single Command Installation
Prerequisites

Python 3.7+
pip package manager

One-Line Setup & Run
For Windows (PowerShell/CMD):
bashgit clone https://github.com/iGufrankhan/Diabetes_Prediction_Model.git && cd Diabetes_Prediction_Model && pip install -r requirements.txt && python app.py
For Linux/macOS (Terminal):
bashgit clone https://github.com/iGufrankhan/Diabetes_Prediction_Model.git && cd Diabetes_Prediction_Model && pip install -r requirements.txt && python app.py
Using Python3 explicitly:
bashgit clone https://github.com/iGufrankhan/Diabetes_Prediction_Model.git && cd Diabetes_Prediction_Model && pip3 install -r requirements.txt && python3 app.py
```

### What This Command Does:
1. ✅ Clones the repository from GitHub
2. ✅ Navigates into the project directory
3. ✅ Installs all required dependencies
4. ✅ Runs the application

The application will start on `http://localhost:5000` (or your configured port).

---

## 🎯 Features

- ✨ **Real-time Prediction**: Instant diabetes risk assessment
- 📊 **Interactive UI**: User-friendly interface for entering health metrics
- 🔍 **Data Visualization**: Visual insights into model performance
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🚀 **Fast Inference**: Quick prediction results using optimized ML model

---

## 🏗️ Project Structure
```
Diabetes_Prediction_Model/
│
├── app.py                      # Main application file
├── model.pkl                   # Trained ML model
├── diabetes.csv                # Dataset
├── requirements.txt            # Python dependencies
├── screenshort/
│   └── front.png              # UI screenshot
├── templates/
│   └── index.html             # Frontend template
├── static/
│   ├── css/                   # Stylesheets
│   └── js/                    # JavaScript files
└── README.md                  # Project documentation

🧪 Model Training
The model was trained using:

Data Preprocessing: Handling missing values, feature scaling
Train-Test Split: 80-20 ratio
Model Selection: Comparison between Logistic Regression and SVM
Hyperparameter Tuning: Grid search for optimal parameters
Evaluation Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC


📈 Results
MetricScoreTraining Accuracy78%Test Accuracy77%Precision75%Recall72%F1-Score73%

🐛 Troubleshooting
If you encounter any issues:
bash# Check Python version
python --version

# Upgrade pip
pip install --upgrade pip

# Install dependencies with verbose output
pip install -r requirements.txt -v

# Run with debug mode
python app.py --debug

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/improvement)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/improvement)
Create a Pull Request


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Gufran Khan

GitHub: @iGufrankhan
LinkedIn: Your LinkedIn Profile


⚠️ Disclaimer
This tool is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

🙏 Acknowledgments

Pima Indians Diabetes Dataset from UCI Machine Learning Repository
scikit-learn community for excellent ML libraries
All contributors and supporters of this project


📧 Contact
For questions or feedback, please open an issue or reach out via email.

⭐ If you find this project useful, please consider giving it a star!
