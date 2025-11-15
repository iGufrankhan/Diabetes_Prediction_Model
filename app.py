from flask import Flask, render_template, request
import numpy as np
import pickle  

app = Flask(__name__)

with open("classifier.pkl", "rb") as file:
    classifier = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[key]) for key in request.form]
        data = np.array([features])
        prediction = classifier.predict(data)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template('result.html', result=result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
