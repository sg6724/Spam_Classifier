import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

## Firstly let's load the models
model = pickle.load(open('models/model.pkl','rb'))
encoder = pickle.load(open('models/encoder.pkl','rb'))
vectorize = pickle.load(open('models/vectorize.pkl','rb'))

## working
## 1. Getting input from the user
## 2. vectorize it
## 3. predict the output using model 
## 4. return spam or ham by invert_transforming the label encoder

@app.route('/', methods=['GET'])
def homePage():
    if request.method == 'GET':
      return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        email_message = request.form.get("email_message")
        if not email_message:
            return render_template("home.html", message="Please enter the email message")
        else:
            # Transform the input text to a feature vector
            message_vector = vectorize.transform([email_message])
            
            # Convert sparse matrix to dense array - this is the key fix
            message_vector_dense = message_vector.toarray()
            
            # Make prediction using the dense array
            prediction = model.predict(message_vector_dense)
            prediction = encoder.inverse_transform(prediction)
            
            # Convert prediction array to string for display
            result = prediction[0]
            return render_template("home.html", prediction=result)
    except Exception as e:
        # Log the actual error for debugging
        print(f"Error: {str(e)}")
        return render_template("home.html", message="Something went wrong. Please try again")
  
if __name__ == '__main__':
    app.run(debug=True)