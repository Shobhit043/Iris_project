# Iris_project
This project is dedicated to analyze the dataset and create a ML model to predict the species of iris flower based on its features
# Overview
This project aims to predict the species of iris flowers based on features such as sepal length, sepal
width, petal length, and petal width. The prediction is done using machine learning models trained on
the famous Iris dataset.

# Installation
To run this project locally, follow these steps:
1. Clone the repository:
bash
git clone https://github.com/Shobhit043/Iris_project.git

3. Install the required dependencies:
bash
pip install -r requirements.txt

# Usage
1. Navigate to the project directory:
bash
cd iris_dataset_prediction
2. Run the prediction script:
bash
python app.py
This will load the trained model and make predictions on a sample input.

# Dataset
The Iris dataset used for this project is a classic dataset in machine learning. It consists of 150
samples of iris flowers, each belonging to one of three species: setosa, versicolor, or virginica. The
dataset is included in the data directory.
For more information about the dataset, refer to UCI Machine Learning Repository - Iris Dataset.

# Models
Two machine learning models were trained on the Iris dataset:
1. Decision Tree Classifier
2. Random Forest Classifier
3. Logistic Regression
4. MultinomialNB
5. SVC
6. Linear SVC
7. Bagging Classifier

Random Forest Classifier performed the best thus we choose it.
These results may vary based on the dataset split and hyperparameters used.

# License
This project is licensed under the MIT License - see the LICENSE file for details
