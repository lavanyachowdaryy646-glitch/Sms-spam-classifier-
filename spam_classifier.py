import joblib

model = joblib.load("spam_classifier_model.pkl")

def predict_spam(message):
    prediction = model.predict([message])[0]
    return "SPAM" if prediction == "spam" else "NOT SPAM"

if __name__ == "__main__":
    message = input("Enter an SMS message: ")
    print("Prediction:", predict_spam(message))
