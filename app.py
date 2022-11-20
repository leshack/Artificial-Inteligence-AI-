from flask import Flask,request,jsonify
import numpy as np
import pickle
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()] 
    features = [np.array(int_features)] 
    prediction = model.predict(features)  
    result = round(prediction[0], 2)
    return jsonify({'prediction':str(result)})
if __name__ == '__main__':
    app.run()