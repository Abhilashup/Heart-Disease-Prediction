# Imports
from flask import Flask, request, render_template
import sklearn
import pickle
import numpy as np

# Loading the model
model = pickle.load(open('new_rf_model.pkl','rb'))
# Create the application
app  = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # All the entries in the form of a list
    features = [float(i) for i in request.form.values()]
    # Convert them into an array
    array_features = [np.array(features)]
    # Make the prediction
    prediction = model.predict(array_features)

    output = prediction

    if output == 0:
        return render_template('prediction.html',prediction = output)
    else:
        return render_template('prediction.html', prediction = output)


if __name__ == '__main__':
    app.run(debug=True)
