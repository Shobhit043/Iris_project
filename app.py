# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import pickle

# Create a Flask app
app = Flask(__name__)

user_inputs = {'sepal_length': None, 'sepal_width': None,'petal_length': None, 'petal_width': None }
predicted_output = None
model = pickle.load(open('iris_model','rb'))

@app.route('/')
def home():
    return render_template('index.html', predicted_output=predicted_output)

@app.route('/iris_profile')
def iris_profile():
    return render_template('iris_profile.html')

@app.route('/', methods=['POST'])
def predict():

    try:
        user_inputs['sepal_length'] = float(request.form['sepal_length'])
        user_inputs['sepal_width'] = float(request.form['sepal_width'])
        user_inputs['petal_length'] = float(request.form['petal_length'])
        user_inputs['petal_width'] = float(request.form['petal_width'])

    
    predicted_output = model.predict(pd.DataFrame(user_inputs,index=[0]))
    
    if(predicted_output==0):predicted_output='setosa'
    elif(predicted_output==1):predicted_output='virginica'
    elif(predicted_output==2):predicted_output='versicolor'

    return render_template('result.html', user_inputs=user_inputs, predicted_output=predicted_output[0])

if __name__ == '__main__':
    app.run(debug=False)
