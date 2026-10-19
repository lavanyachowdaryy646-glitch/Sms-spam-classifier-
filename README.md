# SMS Spam Classifier Using Machine Learning

## Project Description
This project uses Machine Learning to classify SMS messages as Spam or Not Spam.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Naive Bayes
- CountVectorizer
- Joblib

## How It Works
1. Load the SMS dataset.
2. Split the data into training and testing sets.
3. Convert text messages into numerical features.
4. Train a Naive Bayes classification model.
5. Predict whether new SMS messages are spam or not spam.
6. Evaluate the model using accuracy.

## Files
- spam_classifier.py: Python prediction program.
- spam_classifier_model.pkl: Trained machine learning model.
- README.md: Project documentation.

## How to Run
Install the required packages:
pip install pandas scikit-learn joblib

Then run:
python spam_classifier.py
